import sounddevice as sd
import soundfile as sf
import numpy as np
import queue
import time

q = queue.Queue()

def callback(indata, frames, time_info, status):
    if status:
        print(status)
    q.put(indata.copy())

def record_audio(filename, duration=3, samplerate=16000):
    print("[Recorder] Recording...")
    with sf.SoundFile(filename, mode='w', samplerate=samplerate, channels=1, subtype='PCM_16') as file:
        with sd.InputStream(samplerate=samplerate, channels=1, callback=callback):
            start_time = time.time()
            while time.time() - start_time < duration:
                file.write(q.get())
    print(f"[Recorder] Audio saved to {filename}")
    return filename
