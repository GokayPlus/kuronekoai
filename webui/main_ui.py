import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import gradio as gr
from scripts.prompt_parser import parse_command
from scripts.generate_image import generate_image

def process_input(image, user_text):
    parsed = parse_command(user_text)
    final_prompt = parsed["prompt"]
    result = generate_image(final_prompt)
    return result

with gr.Blocks() as demo:
    gr.Markdown("# 🐾 Kuroneko V1 – Test Panel")
    with gr.Row():
        input_img = gr.Image(label="Optional image (not used yet)")
        user_prompt = gr.Textbox(label="Your command")
    output_img = gr.Image(label="Generated Image")

    user_prompt.submit(process_input, inputs=[input_img, user_prompt], outputs=output_img)

demo.launch()
