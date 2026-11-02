# 🤖 Skripsi RAG Chatbot dengan LangGraph & Google Gemini

Aplikasi Chatbot pintar berbasis **Retrieval-Augmented Generation (RAG)** yang mampu membaca, memahami, dan menjawab pertanyaan secara interaktif berdasarkan dokumen Skripsi format Microsoft Word (`.docx`).

## 🚀 Fitur Utama
- **LangGraph Workflow**: Mengatur alur logika pencarian dan sintesis jawaban menggunakan sistem Multi-Node terstruktur (`retriever` & `generate`).
- **ChromaDB Vector Store**: Penyimpanan data semantik lokal yang efisien.
- **Google Gemini API**: Menggunakan model embedding `gemini-embedding-001` dan LLM terbaru `gemini-3.8-flash` untuk hasil jawaban yang cerdas dan kontekstual.
- **Interactive Terminal Chat**: Fitur perulangan chat langsung dari terminal keyboard pengguna.

## 🛠️ Cara Instalasi & Menjalankan

1. **Clone Repositori ini:**
   ```bash
   git clone https://github.com/YusufCahyo-lgtm/skripsi-rag-chatbot.git
   cd skripsi-rag-chatbot
   ```

2. **Install Dependensi Pustaka:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup Environment Variables:**
   Buat file `.env` di folder utama dan masukkan API Key Gemini Anda:
   ```env
   GOOGLE_API_KEY=isi_api_key_gemini_anda
   ```

4. **Siapkan Dokumen Skripsi:**
   Taruh file skripsi `.docx` Anda di dalam folder `./skripsi/Skripsi Uji. - Copy.docx`.

5. **Jalankan Ingest & Aplikasi:**
   ```bash
   # Langkah 1: Penyerapan data ke database
   python ingest.py

   # Langkah 2: Jalankan Chatbot interaktif
   python main.py
   ```
