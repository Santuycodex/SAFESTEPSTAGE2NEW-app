import streamlit as st
import requests

API_KEY = "MASUKKAN_API_KEY_KAMU_DI_SINI"
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"

def tanya_gemini(pesan):
    headers = {"Content-Type": "application/json"}
    body = {
        "contents": [{
            "parts": [{
                "text": pesan
            }]
        }]
    }
    response = requests.post(f"{GEMINI_URL}?key={API_KEY}", headers=headers, json=body)
    if response.status_code == 200:
        result = response.json()
        return result["candidates"][0]["content"]["parts"][0]["text"]
    else:
        return f"❌ Error: {response.status_code}"

st.set_page_config(page_title="AI Sensor Chat", layout="centered")
st.title("🤖 AI Klasifikasi Jarak & Chatbot Gemini")

st.subheader("🔍 Analisis Otomatis dari Sensor")

distance = st.slider("Pilih Jarak (cm)", 1, 200, 75)

if st.button("Analisis AI (Jarak)"):
    with st.spinner("Menghubungi Gemini..."):
        prompt_jarak = f"Jarak objek adalah {distance:.2f} cm. Jelaskan klasifikasinya seperti 'terlalu dekat', 'aman', atau 'terlalu jauh'."
        hasil = tanya_gemini(prompt_jarak)
        st.success("AI menjawab:")
        st.write(hasil)

st.divider()

st.subheader("💬 Chatbot AI (dengan info jarak)")

chat_input = st.text_input("Tulis pertanyaan kamu:")

if st.button("Kirim Pertanyaan ke AI"):
    if chat_input.strip() != "":
        with st.spinner("AI sedang mengetik..."):
            # Gabungkan pertanyaan dengan jarak
            pesan = f"Jarak objek saat ini adalah {distance:.2f} cm. {chat_input}"
            jawaban = tanya_gemini(pesan)
            st.success("AI menjawab:")
            st.write(jawaban)
    else:
        st.warning("Pertanyaan tidak boleh kosong ya broo!")
