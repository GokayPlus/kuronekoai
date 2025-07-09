import requests

def ask_ai(prompt):
    formatted = (
    "<|system|>\n"
    "You are Kuroneko, a cute anime catgirl assistant who ends sentences with nya~.\n"
    "<|user|>\n" + prompt.strip() + "\n<|Kuroneko|>\n"
)

    try:
        response = requests.post(
    "http://127.0.0.1:5000/v1/completions",
    json={
        "prompt": formatted,
        "max_tokens": 200,
        "temperature": 0.7,
        "stop": ["<|user|>"]
    }
)
        raw_text = response.json()["choices"][0]["text"]
        cleaned = raw_text.strip().split("<|user|>")[0].strip()
        return cleaned  # 🔥 sadece cevabı döndür, tag'ları değil
    except Exception as e:
        return f"[LLM Hatası] {e}"
