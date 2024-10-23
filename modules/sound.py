import customtkinter as ctk
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import wave
import threading


def start_rec(start_button, stop_button, thread_container, root):
    print("start recording")

    # show stop button
    stop_button.grid(row=0, column=1)
    # change rec button image

    audio_data = []
    is_recording = [True]

    def rec_audio():
        def callback(indata, frames, time, status):
            if status:
                print(status)
            if is_recording[0]:
                audio_data.append(indata.copy())

        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            while is_recording[0]:
                sd.sleep(100)

    def stop_rec():
        print("stopping")
        is_recording[0] = False
        thread_container[0].join()
        show_file_naming_win(audio_data, root)

    stop_button.configure(command=stop_rec)

    recording_thread = threading.Thread(target=rec_audio)
    thread_container[0] = recording_thread
    recording_thread.start()


def save_audio(filename, audio_data, root):
    print("saving audio")
    audio_np = np.concatenate(audio_data, axis=0)
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(audio_np.astype(np.int16).tobytes())

        root.destroy()
        print("root destroyed")


def show_file_naming_win(audio_data, root):
    frame = ctk.CTkFrame(root)

    input_field = ctk.CTkEntry(frame)
    save_button = ctk.CTkButton(
        frame,
        text="Save",
        command=lambda: save_audio(f"{input_field.get()}.wav", audio_data, root),
    )

    frame.grid(row=1, column=0)
    input_field.pack()
    save_button.pack()
