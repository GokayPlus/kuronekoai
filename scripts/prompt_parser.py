def parse_command(user_input):
    # Gelişmiş versiyonda burada chat_engine ile OpenChat'e sorulacak
    # Şimdilik sabit dönüş
    if "Teto" in user_input:
        return {
            "prompt": "girl with pink twin tails",
            "lora": "KasaneTeto"
        }
    elif "şapka" in user_input or "hat" in user_input:
        return {
            "prompt": "girl with a stylish hat",
            "lora": "HatAddon"
        }
    else:
        return {
            "prompt": "anime girl portrait",
            "lora": None
        }
