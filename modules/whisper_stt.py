import openai
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()

# Make sure you set your OpenAI API key in the environment or load it securely
openai.api_key = os.getenv("OPENAI_API_KEY")

def transcribe_audio(audio_file_path: str) -> str:
    audio_path = Path(audio_file_path)

    with audio_path.open("rb") as audio_file:
        transcript = openai.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file,
        )
    return transcript.text

