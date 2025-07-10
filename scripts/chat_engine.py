import requests
from deep_translator import GoogleTranslator

# Chat modeliyle konuşmak için endpoint
API_URL = "http://localhost:5000/v1/completions"

def translate_input(text):
    return GoogleTranslator(source="auto", target="en").translate(text)

def translate_output(text):
    return GoogleTranslator(source="en", target="auto").translate(text)

def ask_ai(message):
    # 1. Girdi İngilizceye çevrilir
    translated_input = translate_input(message)

    # 2. OpenChat'e gönderilir
    payload = {
        "prompt": translated_input,
        "max_tokens": 3000, #change this
        "temperature": 0.7,
        "stop": ["<|end|>"]
    }

    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        result = response.json()["choices"][0]["text"]
    except Exception as e:
        return f"[Kuroneko] Chat error: {e}"

    # 3. Yanıt geri çevrilir
    return translate_output(result.strip())
