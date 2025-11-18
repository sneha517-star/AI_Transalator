import gradio as gr
from deep_translator import GoogleTranslator

def translate(text, direction):
    if direction == "English → Tamil":
        return GoogleTranslator(source="en", target="ta").translate(text)
    else:
        return GoogleTranslator(source="ta", target="en").translate(text)

interface = gr.Interface(
    fn=translate,
    inputs=[
        gr.Textbox(label="Enter text"),
        gr.Radio(["English → Tamil", "Tamil → English"], label="Translation Direction")
    ],
    outputs=gr.Textbox(label="Translated Output"),
    title="AI Translator - English ↔ Tamil",
    description="Translate text between English and Tamil using Deep-Translator."
)

interface.launch()
