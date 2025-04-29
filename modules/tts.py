import requests
import os
from playsound import playsound

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")  # set to a specific voice from your ElevenLabs account


def speak_text(text, filename="response.mp3"):
    print("[TTS] Sending text to ElevenLabs...")
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{VOICE_ID}"
    headers = {
        "xi-api-key": ELEVENLABS_API_KEY,
        "Content-Type": "application/json",
    }
    payload = {
        "text": text,
        "voice_settings": {
            "stability": 0.75,
            "similarity_boost": 0.75
        }
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()

    with open(filename, "wb") as f:
        f.write(response.content)

    print(f"[TTS] Playing {filename}...")
    playsound(filename)
