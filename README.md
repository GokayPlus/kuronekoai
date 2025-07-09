# Kuroneko
**Kuroneko** is a personal hobby project created for learning and experimentation purposes. So you can see it says nya~ at the every sentence. You can upgrade it via other chat models or [feeding with picture models](https://civitai.com/models).

It’s a customizable AI assistant combining:

- 🧠 **Chat system** powered by [OpenChat 3.5](https://huggingface.co/TheBloke/OpenChat-3.5-GGUF) (GGUF format, runs locally via server),
- 🧾 **Language understanding layer** using [Google's Flan-T5-Small](https://huggingface.co/google/flan-t5-small) for zero-shot intent recognition,
- 🖼️ **Image editing pipeline** built with [Stable Diffusion](https://github.com/CompVis/stable-diffusion) (img2img mode via Diffusers),
- 🌐 Optional online extensions (e.g., translations or internet search),
- 🔐 All running locally by design, with a focus on privacy, offline use, and user control.

Kuroneko was built as an educational playground to explore modern AI systems—LLMs, diffusion models, prompt processing—and how they can be integrated in a lightweight, privacy-respecting assistant.
---

## ⚠️ Disclaimer

This project is **not actively maintained**, and it is **not intended for production use**.
It was developed as a hobby to explore AI, local LLMs, image generation, and privacy-first interfaces.
There will be **no** regular updates or ongoing support.

I didn't setup Whisper model but if you want set it up.
It has memory problems. It doesn't remember previous message(s).

---

## 🔧 Setup (Recommended Assets)

To run Kuroneko on your own device, you'll need:

* **Source code** from this GitHub repo

  ```bash
  git clone https://github.com/GokayPlus/kuronekoai.git
  ```

* **Required large files, you don't have to use my files, but I recommend them because I used them when learning.(models + virtual environment)**
  Download and extract into the project root:

  👉 [Hugging Face – kuronekoassets](https://huggingface.co/CanPlus/kuronekoassets/tree/main)
  (Download `models.zip` and `venv.zip`.)

After extraction, your structure should look like:

```
kuronekoai/
├── models/        ← contains model files
├── venv/          ← contains virtual environment
└── <and the other files came from clone>
```

---

## 🚀 Running

Activate the venv and start the app:

```bash
# On Windows (PowerShell)
.\venv\Scripts\Activate

# Open another terminal tab and go to \models\
cd xx\kuronekoai\models\text-generation-webui
# Start server with this command.
python server.py --model OpenChat --model-dir models --loader llama --api

# Go to \webui\
cd xx\kuronekoai\webui
py kuroneko_chat_ui.py
```

Then open the local Gradio interface (URL shown in terminal) to chat or use img2img.

---

## 🛠️ Tech Stack

* **Python 3.10+**
* **OpenChat 3.5** (local GGUF model)
* **Stable Diffusion** for img2img
* **Gradio** UI
* **Transformers**, **Diffusers**, **llama.cpp**

---

## 📄 License

gpl-3.0
I want to make full free it but it's my first project so if you use it on any project please give my project's name.


---

📚 **This is a personal, educational project.**
Feel free to explore, fork, adapt—and enjoy learning with it!
