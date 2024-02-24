# transcriber.py
import pyaudio
import wave
import whisper
import os
import tempfile
from pynput import keyboard
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

def record_and_transcribe():
    CHUNK = 4096
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    audio = pyaudio.PyAudio()
    frames = []
    state = {"recording": False}

    def callback(in_data, frame_count, time_info, status):
        if state["recording"]:
            frames.append(in_data)
        return (in_data, pyaudio.paContinue)

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK,
                        stream_callback=callback)

    def on_press(key):
        try:
            if key == keyboard.Key.space:
                state["recording"] = not state["recording"]
                if state["recording"]:
                    print("Recording started...")
                    if not stream.is_active():
                        stream.start_stream()
                else:
                    print("Recording stopped.")
                    if stream.is_active():
                        stream.stop_stream()
        except Exception as e:
            print(f"Error occurred: {e}")

    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    print("Press spacebar to start/stop recording.")
    while listener.running:
        if not state["recording"] and not stream.is_active():
            listener.stop()

    stream.close()
    audio.terminate()

    with tempfile.NamedTemporaryFile(suffix='.wav', delete=False) as temp_audio:
        wf = wave.open(temp_audio.name, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        print("Transcribing the audio...")
        model = whisper.load_model("base")
        result = model.transcribe(temp_audio.name, language="en")
        transcription = result["text"]
        os.remove(temp_audio.name)  # Clean up the temporary file

    return transcription
