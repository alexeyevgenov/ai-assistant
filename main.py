import asyncio
import os
from modules.wake_word import WakeWordListener
from modules.voice_input import record_audio
from modules.whisper_stt import transcribe_audio
from modules.gpt_responder import get_gpt_response
from modules.tts import speak_text
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

async def main():
    print("[AI-Mentor] Initialized. Waiting for wake word...")
    wake_listener = WakeWordListener()

    while True:
        # await wake_listener.wait_for_wake_word()
        # print("[AI-Mentor] Wake word detected. Listening...")

        audio_file = record_audio("output.wav")
        print("[AI-Mentor] Audio recorded. Transcribing...")

        # text = transcribe_audio(audio_file)
        # print(f"[You]: {text}")

        text = "Which new features did you get with the latest update?"

        response = get_gpt_response(text)
        print(f"[AI-Mentor]: {response}")

        speak_text(response)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("[AI-Mentor] Shutdown requested. Goodbye!")
