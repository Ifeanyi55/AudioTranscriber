import gradio as gr
import assemblyai as aai
import google.generativeai as genai
from script import audioTranscribe

# app = gr.Interface(audioTranscribe,
#                    inputs=[gr.Audio(sources=["microphone"], type="filepath"),
#                            gr.Dropdown(["French","Spanish","German","Italian","Japanese"],
#                                        label="Languages",
#                                        multiselect=False,
#                                        value="French",
#                                        info="Translations")],
#                    outputs=[gr.Text(label="Transcription"),gr.Text(label="Translation")])
# app.launch(debug=True)

with gr.Blocks(theme = gr.themes.Soft()) as app:
  gr.Markdown("<center><strong><h3>Audio Transcription & Translation</h3></strong></center>")
  with gr.Column():
    with gr.Row():
      audio_file = gr.Audio(sources=["microphone"], type="filepath")
      translation = gr.Radio(choices=["French","Spanish","German","Italian","Japanese","Portuguese","Igbo","Korean","Hindi","Yoruba","Dutch","Hausa","Polish","Swahili","Turkish"],
                             label="Select Translate-To Language",
                             value="French",
                             interactive=True)
    with gr.Row():
      btn = gr.Button("Transcribe & Translate")
      clear_btn = gr.ClearButton(value="Clear")
    with gr.Column():
      gr.Markdown("<center><strong><h3>Transcription & Translation Output</h3></strong></center>")
    with gr.Row():
      transcription = gr.Text(label="Transcription")
      translation_text = gr.Text(label="Translation")


  btn.click(audioTranscribe, inputs=[audio_file,translation], outputs=[transcription,translation_text])
  clear_btn.click(lambda: (None, "French", "", ""), inputs=[], outputs=[audio_file, translation, transcription, translation_text], queue=False)

app.launch()