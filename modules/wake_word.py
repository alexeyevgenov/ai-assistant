import pvporcupine
import pyaudio
import struct
import asyncio
import os

class WakeWordListener:
    def __init__(self, keyword="jarvis"):
        self.keyword = keyword
        # Initialize attributes to None
        self.porcupine = None
        self.pa = None
        self.stream = None

        access_key = os.getenv("PVPORCUPINE_ACCESS_KEY")
        if not access_key:
            raise ValueError("PVPORCUPINE_ACCESS_KEY environment variable not set.")

        try:
            self.porcupine = pvporcupine.create(
                access_key=access_key,
                keyword_paths=[
                    pvporcupine.KEYWORD_PATHS[keyword]
                ]
            )
        except pvporcupine.PorcupineActivationLimitError as e:
            print("[WakeWord] Porcupine activation limit reached. Please check your Picovoice Console and update your access key.")
            raise e

        self.pa = pyaudio.PyAudio()
        self.stream = self.pa.open(
            rate=self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    async def wait_for_wake_word(self):
        while True:
            pcm = self.stream.read(self.porcupine.frame_length, exception_on_overflow=False)
            pcm_unpacked = struct.unpack_from("h" * self.porcupine.frame_length, pcm)
            keyword_index = self.porcupine.process(pcm_unpacked)

            if keyword_index >= 0:
                return

    def __del__(self):
        if self.stream is not None:
            self.stream.close()
        if self.pa is not None:
            self.pa.terminate()
        if self.porcupine is not None:
            self.porcupine.delete()
