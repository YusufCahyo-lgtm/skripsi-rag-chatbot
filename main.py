from dotenv import load_dotenv
# Memastikan API Key terbaca saat aplikasi dinyalakan, dan ini harus ditempatkan paling awal krna
#pembacaan file ".env" harus paling awal, Jika anda tdk meletakkan "load_dotenv() yg memuat file .env ini"
# maka file lain seperti "from workflow import build_app"akan dijalankan terlebih dahulu dan ini
#akan mengakibatkan terjadinya "masalah urutan pembacaan kode" dimana "GoogleGenerativeAIEmbeddings"
#akan memprotes karena merasa tidak diberikan kunci API.
load_dotenv()
from workflow import build_app

app = build_app()

def chat(tanya):
    inputs = {"question": tanya}
    final_answer = ""
    
    # Mengamankan data hasil stream dari node terakhir ("generate")
    for output in app.stream(inputs):
        if "generate" in output:
            raw_response = output["generate"]["answer"]
            
            if isinstance(raw_response, list) and len(raw_response) > 0:
                final_answer = raw_response[0].get('text', '')
            else:
                final_answer = raw_response
            
    return final_answer

if __name__ == "__main__":
    print("--- CHATBOT SKRIPSI SIAP (Ketik pertanyaan Anda) ---")
    
    #Untuk input pertanyaan, dapat dilakukan disini:
    pertanyaan = "Apa topik utama skripsi ini?"
    print(f"User: {pertanyaan}")
    
    jawaban = chat(pertanyaan)
    print(f"AI  : {jawaban}")
