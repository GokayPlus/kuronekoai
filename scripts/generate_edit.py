from diffusers import StableDiffusionImg2ImgPipeline
import torch
from PIL import Image
import os

# Modeli yükle
pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
).to("cuda")

def edit_image(image_path, prompt):
    init_image = Image.open(image_path).convert("RGB").resize((512, 512))
    edited_image = pipe(prompt=prompt, image=init_image, strength=0.75, guidance_scale=7.5).images[0]
    return edited_image
