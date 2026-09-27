# PT TALAHOME AI Knowledge Assistant (RAG System)

Sistem asisten AI internal berbasis Retrieval-Augmented Generation (RAG) untuk staf operasional dan quality control PT TALAHOME Jepara (manufaktur dan eksportir furnitur kayu).

---

## 1. Fitur Utama
- **Anti-Halusinasi (Strict Context Grounding)**: Menjawab hanya berdasarkan SOP dan dokumen internal resmi PT TALAHOME.
- **Rujukan Halaman Presisi**: Setiap jawaban menyertakan nomor halaman dan skor relevansi embedding.
- **Dual Interface**:
  - **Telegram Bot (`@talahomeRAG_bot`)**: Digunakan mandor dan staf QC langsung di lini produksi / gudang pabrik.
  - **Web Dashboard**: Digunakan HRD / Admin untuk mengunggah dokumen SOP PDF dan mengaudit log pertanyaan.
- **Vektor Database Cloud**: Menggunakan Supabase PostgreSQL dengan ekstensi `pgvector` dan cosine similarity search.
- **Audit Trail**: Setiap pertanyaan, jawaban, dan sumber tercatat di tabel `chat_logs` Supabase.

---

## 2. Tech Stack
- **Backend**: Python 3.11, FastAPI, Uvicorn, HTTPX, PyPDF
- **Model LLM & Embedding**:
  - Embedding: Google `gemini-embedding-001` (768 dimensi)
  - Generator: Google `gemini-flash-latest`
- **Database**: Supabase PostgreSQL + `pgvector`
- **Bot Gateway**: `python-telegram-bot` (long-polling asynchronous)
- **Frontend**: HTML5, Tailwind CSS (Single Page App terintegrasi)
- **Deployment**: Docker, Docker Compose, GitHub Actions CI

---

## 3. Struktur Direktori
```text
talahome-rag/
├── .github/workflows/
│   └── ci.yml               # Pipeline CI GitHub Actions
├── data/
│   └── SOP_Standar_Finishing_Ekspor_TALAHOME.pdf  # Contoh SOP uji coba
├── static/
│   └── index.html           # Web Dashboard minimalis (upload & chat simulator)
├── .env                     # Variabel lingkungan (Supabase, Gemini, Telegram)
├── .env.example             # Template konfigurasi
├── core.py                  # Pipeline RAG (ingestion, embedding, Supabase vector search, LLM)
├── main.py                  # Server FastAPI & background Telegram bot worker
├── requirements.txt         # Daftar pustaka Python
├── Dockerfile               # Konfigurasi container Docker
├── docker-compose.yml       # Orkestrasi container
└── README.md                # Dokumentasi sistem
```

---

## 4. Cara Menjalankan

### Opsi A: Lokal (Tanpa Docker)
```bash
# Masuk ke folder project
cd "C:/Users/M RIZKY/talahome-rag"

# Install dependensi
pip install -r requirements.txt

# Jalankan server FastAPI + Telegram Bot
python main.py
```
- Akses Web Dashboard di browser: `http://localhost:8000`
- Chat via Telegram: buka `@talahomeRAG_bot` lalu ketik `/start`.

### Opsi B: Menggunakan Docker
```bash
docker compose up -d --build
```

---

## 5. Skenario Demo 5 Menit di Depan Interviewer

1. **Menit 1-2 (Arsitektur & Konsep)**:
   - Jelaskan bahwa sistem ini memecahkan masalah salah komunikasi SOP dan standar ekspor di lantai produksi mebel.
   - Perlihatkan arsitektur: Dokumen PDF -> Chunking -> Vector Embedding (Gemini) -> Supabase pgvector -> Dual Gateway (Web & Telegram).

2. **Menit 3 (Web Dashboard & Upload Dokumen)**:
   - Buka `http://localhost:8000` di laptop.
   - Tunjukkan daftar dokumen yang sudah aktif (`SOP_Standar_Finishing_Ekspor_TALAHOME.pdf`).
   - Coba upload PDF SOP baru melalui fitur drag-and-drop.

3. **Menit 4 (Live Demo Bot Telegram via HP)**:
   - Ambil HP di depan interviewer.
   - Buka bot Telegram `@talahomeRAG_bot`.
   - Tanyakan: *"Berapa standar kadar air kayu untuk ekspor?"*
   - Tunjukkan jawaban bot yang instan dan presisi: 8-12% dengan sitasi halaman 1.
   - Tanyakan pertanyaan di luar SOP: *"Bagaimana resep nasi goreng?"*
   - Bot akan menolak menjawab karena berpegang teguh pada konteks dokumen (anti-halusinasi).

4. **Menit 5 (Audit Trail Database & Validasi Teknis)**:
   - Buka tab Supabase di browser, masuk ke tabel `chat_logs`.
   - Tunjukkan baris log pertanyaan yang baru saja ditanyakan lewat Telegram sudah tercatat secara real-time.
