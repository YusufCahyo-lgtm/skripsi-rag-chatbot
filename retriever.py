# file: retriever.py
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()
# Harus menggunakan model embedding yang sama dengan saat ingest
vectorstore = Chroma(
    persist_directory="./chroma_data", 
    embedding_function=GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
)
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})
