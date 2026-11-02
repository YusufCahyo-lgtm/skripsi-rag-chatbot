# file: nodes.py
from langchain_google_genai import ChatGoogleGenerativeAI # 🆕 Ganti ke Google
from retriever import retriever

def mengambil(state):
    docs = retriever.invoke(state["question"])
    content = "\n\n".join([d.page_content for d in docs])
    return {"context": content}

# 🆕 Variabel llm sekarang menerima otak Gemini secara GRATIS
llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash") 

def hasilin(state):
    prompt = f"Gunakan info ini: {state['context']}\n\n Pertanyaan: {state['question']}"
    response = llm.invoke(prompt)
    return {"answer": response.content}
