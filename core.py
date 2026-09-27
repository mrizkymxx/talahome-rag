import os
import io
import json
import httpx
from pypdf import PdfReader
from dotenv import load_dotenv

load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL", "").rstrip("/")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

EMBEDDING_MODEL = "gemini-embedding-001"
CHAT_MODEL = "gemini-flash-latest"

def _headers():
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "return=representation"
    }

def get_embedding(text: str) -> list[float]:
    """Gemini 768-dim vector embedding"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{EMBEDDING_MODEL}:embedContent?key={GEMINI_API_KEY}"
    payload = {
        "content": {"parts": [{"text": text[:2000]}]},
        "outputDimensionality": 768
    }
    with httpx.Client(timeout=30.0) as client:
        res = client.post(url, json=payload)
        res.raise_for_status()
        return res.json()["embedding"]["values"]

def search_documents(query_embedding: list[float], limit: int = 3) -> list[dict]:
    """RPC match_documents on Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/rpc/match_documents"
    payload = {
        "query_embedding": query_embedding,
        "match_count": limit
    }
    with httpx.Client(timeout=30.0) as client:
        res = client.post(url, headers=_headers(), json=payload)
        res.raise_for_status()
        return res.json()

def clean_plain_text(text: str) -> str:
    import re
    text = re.sub(r'\*{1,3}(.*?)\*{1,3}', r'\1', text)
    text = text.replace('*', '')
    text = re.sub(r'#+\s*', '', text)
    return text.strip()

def generate_answer(query: str, contexts: list[dict]) -> str:
    """Strict context-grounded response using Groq"""
    if not contexts:
        return "Informasi tidak ditemukan dalam dokumen SOP internal PT TALAHOME yang tersedia."

    context_str = "\n\n".join([
        f"[Halaman {c.get('page_number', 1)} | Similarity: {round(c.get('similarity', 0)*100, 1)}%]\n{c.get('content', '')}"
        for c in contexts
    ])

    system_prompt = (
        "Anda adalah asisten AI teknis internal PT TALAHOME (produsen & eksportir mebel kayu Jepara). "
        "Tugas Anda: Menjawab pertanyaan staf operasional berdasarkan konteks SOP di bawah ini.\n"
        "Aturan ketat:\n"
        "1. Jawab HANYA berdasarkan konteks yang diberikan. Jangan mengarang atau berhalusinasi.\n"
        "2. Jika konteks tidak memuat jawaban, katakan dengan jelas bahwa informasi belum tercantum di SOP.\n"
        "3. Sertakan rujukan nomor halaman jika relevan.\n"
        "4. Gunakan bahasa Indonesia profesional, ringkas, dan langsung ke poin teknis.\n"
        "5. PENTING: Tulis dalam teks polos (plain text). JANGAN gunakan karakter bintang atau tanda asterisk (** atau *) untuk menebalkan teks. Gunakan huruf kapital atau penomoran 1, 2, 3 jika perlu penekanan."
    )

    user_prompt = f"Konteks SOP:\n{context_str}\n\nPertanyaan: {query}\n\nJawaban:"

    # 1. Primary: Groq API
    if GROQ_API_KEY:
        try:
            url = "https://api.groq.com/openai/v1/chat/completions"
            headers = {
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json",
                "User-Agent": "TALAHOME-RAG/1.0"
            }
            payload = {
                "model": "openai/gpt-oss-120b",
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                "temperature": 0.1,
                "max_tokens": 800
            }
            with httpx.Client(timeout=30.0) as client:
                res = client.post(url, headers=headers, json=payload)
                if res.status_code == 200:
                    data = res.json()
                    raw = data["choices"][0]["message"]["content"]
                    return clean_plain_text(raw)
                elif res.status_code == 429:
                    # fallback to gpt-oss-20b
                    payload["model"] = "openai/gpt-oss-20b"
                    res2 = client.post(url, headers=headers, json=payload)
                    if res2.status_code == 200:
                        raw2 = res2.json()["choices"][0]["message"]["content"]
                        return clean_plain_text(raw2)
        except Exception as e:
            print(f"[GROQ_ERROR] {e}")

    # 2. Fallback: Gemini Flash
    url_gemini = f"https://generativelanguage.googleapis.com/v1beta/models/{CHAT_MODEL}:generateContent?key={GEMINI_API_KEY}"
    payload_gemini = {
        "contents": [{"parts": [{"text": f"{system_prompt}\n\n{user_prompt}"}]}],
        "generationConfig": {"temperature": 0.2, "maxOutputTokens": 800}
    }
    with httpx.Client(timeout=30.0) as client:
        res = client.post(url_gemini, json=payload_gemini)
        res.raise_for_status()
        raw_gemini = res.json()["candidates"][0]["content"]["parts"][0]["text"]
        return clean_plain_text(raw_gemini)

def save_chat_log(query: str, response: str, sources: list[dict]):
    """Audit log in Supabase"""
    url = f"{SUPABASE_URL}/rest/v1/chat_logs"
    payload = {
        "query": query,
        "response": response,
        "sources": sources
    }
    try:
        with httpx.Client(timeout=15.0) as client:
            client.post(url, headers=_headers(), json=payload)
    except Exception as e:
        print(f"[LOG_ERROR] {e}")

def get_chat_logs(limit: int = 15) -> list[dict]:
    url = f"{SUPABASE_URL}/rest/v1/chat_logs?select=*&order=created_at.desc&limit={limit}"
    with httpx.Client(timeout=15.0) as client:
        res = client.get(url, headers=_headers())
        if res.status_code == 200:
            return res.json()
        return []

def get_documents_list() -> list[dict]:
    url = f"{SUPABASE_URL}/rest/v1/documents?select=*&order=created_at.desc"
    with httpx.Client(timeout=15.0) as client:
        res = client.get(url, headers=_headers())
        if res.status_code == 200:
            return res.json()
        return []

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    chunks = []
    text = " ".join(text.split())
    if not text:
        return []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def ingest_pdf(file_bytes: bytes, filename: str) -> dict:
    """Ingest PDF: extract, chunk, embed, store in Supabase"""
    reader = PdfReader(io.BytesIO(file_bytes))
    
    # 1. Insert document
    url_doc = f"{SUPABASE_URL}/rest/v1/documents"
    with httpx.Client(timeout=30.0) as client:
        res_doc = client.post(url_doc, headers=_headers(), json={"name": filename})
        res_doc.raise_for_status()
        doc_record = res_doc.json()[0]
        doc_id = doc_record["id"]

    # 2. Extract & chunk per page
    chunks_to_insert = []
    total_pages = len(reader.pages)
    for page_idx, page in enumerate(reader.pages):
        page_num = page_idx + 1
        page_text = page.extract_text() or ""
        page_chunks = chunk_text(page_text, chunk_size=400, overlap=50)
        
        for ch in page_chunks:
            embedding = get_embedding(ch)
            chunks_to_insert.append({
                "document_id": doc_id,
                "content": ch,
                "page_number": page_num,
                "embedding": embedding
            })

    # 3. Batch insert chunks
    if chunks_to_insert:
        url_chunks = f"{SUPABASE_URL}/rest/v1/document_chunks"
        # batch per 20 chunks to avoid payload size limit
        batch_size = 20
        with httpx.Client(timeout=60.0) as client:
            for i in range(0, len(chunks_to_insert), batch_size):
                batch = chunks_to_insert[i:i+batch_size]
                res_ch = client.post(url_chunks, headers=_headers(), json=batch)
                res_ch.raise_for_status()

    return {
        "document_id": doc_id,
        "name": filename,
        "pages": total_pages,
        "chunks_count": len(chunks_to_insert)
    }

def answer_query(query: str) -> dict:
    """Complete RAG pipeline for user query"""
    q_clean = query.strip().lower()
    
    # 1. Quick bypass for short greeting / ping
    greetings = {"tes", "test", "halo", "hai", "ping", "pagi", "siang", "malam", "assalamualaikum", "halo bot"}
    if q_clean in greetings or len(q_clean) <= 3:
        return {
            "answer": "Sistem aktif dan siap melayani staf PT TALAHOME. Silakan ajukan pertanyaan seputar SOP finishing, kadar air kayu (MC), tahapan amplas, atau kemasan ekspor mebel.",
            "sources": []
        }

    q_emb = get_embedding(query)
    matches = search_documents(q_emb, limit=3)
    
    # Filter by similarity threshold (> 0.50)
    relevant = [m for m in matches if m.get("similarity", 0) >= 0.50]
    
    answer = generate_answer(query, relevant)
    
    # Check if answer indicates missing info; if so, suppress sources to avoid confusion
    negatives = ["tidak ditemukan", "belum tercantum", "tidak tercantum", "tidak memuat", "tidak disebutkan", "tidak ada dalam"]
    has_negative = any(neg in answer.lower() for neg in negatives)
    
    docs_map = {d['id']: d['name'] for d in get_documents_list()}
    
    sources = []
    if not has_negative:
        sources = [
            {
                "document_name": docs_map.get(m.get("document_id"), "SOP TALAHOME"),
                "content": m["content"],
                "page": m.get("page_number", 1),
                "score": round(m.get("similarity", 0), 3)
            }
            for m in relevant
        ]
    
    save_chat_log(query, answer, sources)
    return {"answer": answer, "sources": sources}
