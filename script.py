import assemblyai as aai
import google.generativeai as genai

def audioTranscribe(audio_file,translation):
    
  genai.configure(api_key="GEMINI_API_KEY")

  model = genai.GenerativeModel("gemini-1.5-pro-002")

  aai.settings.api_key = "AAI_API_KEY"
  transcriber = aai.Transcriber()
  transcript = transcriber.transcribe(audio_file)

  if translation == "French":

    prompt = "I want you to simply translate this text into French. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])

  elif translation == "Spanish":
    prompt = "I want you to simply translate this text into Spanish. Do not elaborate on the text"

    response = model.generate_content([transcript.text,prompt])
  
  elif translation == "German":
    prompt = "I want you to simply translate this text into German. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])

  elif translation == "Italian":
    prompt = "I want you to simply translate this text into Italian. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])

  elif translation == "Japanese":
    prompt = "I want you to simply translate this text into Japanese. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])
    
  elif translation == "Portuguese":
    prompt = "I want you to simply translate this text into Portuguese. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])
    
  elif translation == "Dutch":
    prompt = "I want you to simply translate this text into Dutch. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])

  elif translation == "Korean":
    prompt = "I want you to simply translate this text into Korean. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])

  elif translation == "Hindi":
    prompt = "I want you to simply translate this text into Hindi. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])

  elif translation == "Igbo":
    prompt = "I want you to simply translate this text into Igbo. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])
    
  elif translation == "Yoruba":
    prompt = "I want you to simply translate this text into Yoruba. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])
  
  elif translation == "Polish":
    prompt = "I want you to simply translate this text into Polish. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])
    
  elif translation == "Swahili":
    prompt = "I want you to simply translate this text into Swahili. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])
    
  elif translation == "Turkish":
    prompt = "I want you to simply translate this text into Turkish. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])
    
  elif translation == "Hausa":
    prompt = "I want you to simply translate this text into Hausa. Do not elaborate on the text."

    response = model.generate_content([transcript.text,prompt])


  return [transcript.text, response.text]

