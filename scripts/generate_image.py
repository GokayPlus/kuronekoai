from diffusers import StableDiffusionPipeline, StableDiffusionImg2ImgPipeline
import torch
import os
from PIL import Image

# Model yolu
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "models", "stable-diffusion-v1-5")

txt2img_pipe = None
img2img_pipe = None

def init_pipes():
    global txt2img_pipe, img2img_pipe
    if txt2img_pipe is None:
        print("[Kuroneko] Loading txt2img model...")
        txt2img_pipe = StableDiffusionPipeline.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            local_files_only=True
        )
        txt2img_pipe.to("cuda" if torch.cuda.is_available() else "cpu")
    
    if img2img_pipe is None:
        print("[Kuroneko] Loading img2img model...")
        img2img_pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
            local_files_only=True
        )
        img2img_pipe.to("cuda" if torch.cuda.is_available() else "cpu")

def generate_image(prompt: str):
    init_pipes()
    result = txt2img_pipe(prompt)
    return result.images[0]

def edit_image(prompt: str, init_image: Image.Image, strength: float = 0.75, guidance: float = 7.5):
    init_pipes()
    init_image = init_image.convert("RGB").resize((512, 512))
    result = img2img_pipe(prompt=prompt, image=init_image, strength=strength, guidance_scale=guidance)
    return result.images[0]
