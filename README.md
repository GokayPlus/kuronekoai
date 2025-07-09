# Kuroneko
**Kuroneko** is a personal hobby project created for learning and experimentation purposes. It says 'nya~' at the end of every sentence. You can upgrade it via other chat models or [enhance it with image models](https://civitai.com/models).

It’s a customizable AI assistant combining:

- 🧠 **Chat system** powered by [OpenChat 3.5](https://huggingface.co/TheBloke/OpenChat-3.5-GGUF) (GGUF format, runs locally via llama.cpp),
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

I didn't setup Whisper model but if you want you can set it up. - 
It has memory problems. It doesn't remember previous message(s).

---

## 🔧 Setup (Recommended Assets)

To run Kuroneko on your own device, you'll need:

* **Source code** from this GitHub repo - [git clone is requiring Git](https://git-scm.com/downloads)

  ```bash
  git clone https://github.com/GokayPlus/kuronekoai.git
  ```

* **Required large files, you don't have to use my files, but I recommend them because I used them when learning. (models + virtual environment)**
  Download and extract into the project root:

  👉 [Hugging Face – kuronekoassets](https://huggingface.co/CanPlus/kuronekoassets/tree/main)
  (Download `models.zip` and `venv.zip`.)

After extraction, your structure should look like:

```
kuronekoai/
├── models/        ← contains model files
├── venv/          ← contains virtual environment
└── <including the files cloned from the repo>
```

### ⚙️ GPU Acceleration (Optional)

Kuroneko can take advantage of NVIDIA GPUs if available.

To use CUDA acceleration:
1. Make sure you have an NVIDIA GPU
2. [Install latest drivers](https://www.nvidia.com/download/index.aspx/) and [CUDA](https://developer.nvidia.com/cuda-downloads) (11.8+ recommended)
3. Use [PyTorch](https://pytorch.org/get-started/locally/) with [CUDA](https://developer.nvidia.com/cuda-downloads) support:

```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```
If you don't have a NVIDIA GPU, Kuroneko will still work using CPU — just slower.
---

## 🚀 Running

Activate the venv and start the app:

```bash
# On Windows (PowerShell)
.\venv\Scripts\Activate


# Open another terminal tab and go to \models\
cd xx\kuronekoai\models\text-generation-webui
# Start server with this command.
py server.py --model OpenChat --model-dir models --loader llama --api

# Go to \webui\
cd xx\kuronekoai\webui
py kuroneko_chat_ui.py
--
# On Linux / macOS (Terminal)
source venv/bin/activate

# Open another terminal tab and go to /models/
cd /path/to/kuronekoai/models/text-generation-webui
# Start server with this command
python3 server.py --model OpenChat --model-dir models --loader llama --api

# Go to /webui/
cd /path/to/kuronekoai/webui
python3 kuroneko_chat_ui.py
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

GPL-3.0 |
I want to make it fully free it but it's my first project so if you use it on any project, please give credit to the project by name.


---

📚 **This is a personal, educational project.**
Feel free to explore, fork, adapt—and enjoy learning with it!
