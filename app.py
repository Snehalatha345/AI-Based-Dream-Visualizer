import gradio as gr
from model import generate_dream_image

def visualize_dream(prompt):
    image = generate_dream_image(prompt)
    return image

interface = gr.Interface(
    fn=visualize_dream,
    inputs=gr.Textbox(label="Describe your dream"),
    outputs=gr.Image(label="Generated Dream Image"),
    title="AI Dream Visualizer",
    description="Convert dream descriptions into AI generated images."
)

interface.launch()
