import os
import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv

from core import (
    ingest_pdf,
    answer_query,
    get_documents_list,
    get_chat_logs
)

load_dotenv()
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

class QueryRequest(BaseModel):
    query: str

async def run_telegram_bot():
    """Background Telegram Bot listener"""
    if not TELEGRAM_BOT_TOKEN:
        print("[TELEGRAM] No token provided, skipping bot.")
        return

    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

    async def start_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(
            "Halo! Saya asisten AI resmi SOP PT TALAHOME.\n\n"
            "Silakan tanyakan standar finishing, moisture content, packing, atau SOP ekspor mebel. "
            "Saya akan menjawab berbasis dokumen SOP resmi."
        )

    async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_text = update.message.text
        if not user_text:
            return
        
        await update.message.chat.send_action("typing")
        try:
            loop = asyncio.get_running_loop()
            res = await loop.run_in_executor(None, answer_query, user_text)
            
            ans = res["answer"]
            sources = res.get("sources", [])
            
            reply_text = f"{ans}\n\n"
            if sources:
                reply_text += "Rujukan Dokumen:\n"
                seen = set()
                for s in sources:
                    doc_name = s.get("document_name", "SOP TALAHOME")
                    page = s.get("page", 1)
                    score = int(s.get("score", 0) * 100)
                    key = (doc_name, page)
                    if key not in seen:
                        seen.add(key)
                        reply_text += f"- {doc_name} (Halaman {page}) | Akurasi: {score}%\n"
            
            await update.message.reply_text(reply_text.strip())
        except Exception as e:
            await update.message.reply_text(f"Maaf, terjadi kendala saat memproses: {str(e)}")

    async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
        doc = update.message.document
        if not doc or not doc.file_name.lower().endswith(".pdf"):
            await update.message.reply_text("Silakan kirim file dokumen berformat PDF.")
            return

        status_msg = await update.message.reply_text(f"Menerima file {doc.file_name}...\nMengekstrak teks & menghitung vektor ke Supabase...")
        try:
            tg_file = await context.bot.get_file(doc.file_id)
            pdf_bytes = await tg_file.download_as_bytearray()
            
            loop = asyncio.get_running_loop()
            res = await loop.run_in_executor(None, ingest_pdf, bytes(pdf_bytes), doc.file_name)
            
            await status_msg.edit_text(
                f"SOP Berhasil Diserap!\n\n"
                f"Dokumen: {res['name']}\n"
                f"Total: {res['pages']} halaman ({res['chunks_count']} chunk tersimpan di pgvector).\n\n"
                f"Sistem sekarang siap menjawab pertanyaan dari dokumen baru ini."
            )
        except Exception as e:
            await status_msg.edit_text(f"Gagal memproses dokumen: {str(e)}")

    app_tg = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()
    app_tg.add_handler(CommandHandler("start", start_cmd))
    app_tg.add_handler(CommandHandler("help", start_cmd))
    app_tg.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app_tg.add_handler(MessageHandler(filters.Document.PDF, handle_document))

    print("[TELEGRAM] Bot starting polling...")
    await app_tg.initialize()
    await app_tg.start()
    await app_tg.updater.start_polling()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: run Telegram bot in background
    tg_task = asyncio.create_task(run_telegram_bot())
    yield
    # Shutdown
    tg_task.cancel()

app = FastAPI(title="TALAHOME RAG Assistant", lifespan=lifespan)

# Mount static folder
os.makedirs("static", exist_ok=True)
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    with open("static/index.html", "r", encoding="utf-8") as f:
        return f.read()

@app.get("/api/documents")
async def list_docs():
    return get_documents_list()

@app.get("/api/logs")
async def list_logs():
    return get_chat_logs()

@app.post("/api/upload")
async def upload_pdf(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Hanya file PDF yang didukung.")
    
    content = await file.read()
    res = ingest_pdf(content, file.filename)
    return res

@app.post("/api/query")
async def ask_rag(req: QueryRequest):
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Pertanyaan tidak boleh kosong.")
    return answer_query(req.query)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=False)
