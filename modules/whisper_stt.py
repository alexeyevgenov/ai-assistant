import openai
import os

# Make sure you set your OpenAI API key in the environment or load it securely
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(file_path):
    print("[Whisper] Sending audio for transcription...")
    with open(file_path, "rb") as audio_file:
        transcript = openai.Audio.transcribe("whisper-1", audio_file)
    return transcript['text']
