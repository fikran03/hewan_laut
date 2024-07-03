import requests
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Memuat variabel lingkungan dari file .env
load_dotenv()

API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
instruction = (
    "Sekarang Anda adalah seorang ahli biologi kelautan yang memahami tentang hewan laut yang dilindungi di Papua. "
    "Dalam chat ini, berikan hanya jawaban tentang hewan laut yang dilindungi di Papua. "
    "Anda tidak boleh menjelaskan tentang hal yang lain selain hewan laut yang dilindungi di Papua. "
    "Jika kata yang dimasukkan hanya satu atau dua huruf atau bahkan tidak beraturan maka Anda harus meminta melengkapi kata."
)
print("Halo! Saya adalah Bot yang akan menjelaskan tentang hewan laut yang dilindungi di Papua.")
while True:
    question = input("Kamu: ")

    if "hewan laut" in question.lower() or "papua" in question.lower() or "dilindungi" in question.lower():
        # Menerapkan filter berdasarkan kata kunci "hewan laut", "Papua", dan "dilindungi"
        response_text = chat.send_message(instruction + question).text
        response = response_text
    else:
        response = chat.send_message(instruction + question).text

    print('\n')
    print(f"Ahli Biologi Kelautan: {response}")
    print('\n')
    instruction = ''
