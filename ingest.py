# file: ingest.py
import os
from dotenv import load_dotenv
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings # 🆕 Pakai Google
from langchain_community.document_loaders import Docx2txtLoader
load_dotenv()

# 1. Panggil file teks skripsi 50 halaman Anda
file_path= "./skripsi/Skripsi Uji. - Copy.docx"
loader = Docx2txtLoader(file_path)
docs = loader.load()

# 2. Potong teks menjadi chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
splits = text_splitter.split_documents(docs)

# 3. Simpan ke ChromaDB lokal menggunakan Embedding GRATIS dari Google
vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001"), # 🆕 Vektor Gratis
    persist_directory="./chroma_data" 
)

print(f"✅ Sukses! Skripsi dipotong jadi {len(splits)} bagian di chroma_data (Gratis).")
