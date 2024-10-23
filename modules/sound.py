import customtkinter as ctk
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import wave
import threading
from PIL import Image


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


def save_audio(filename, audio_data, win, root):
    print("saving audio")
    audio_np = np.concatenate(audio_data, axis=0)
    with wave.open(filename, "wb") as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(audio_np.astype(np.int16).tobytes())

        win.destroy()
        print("win destroyed")
        root.destroy()
        print("root destroyed")


def show_file_naming_win(audio_data, root):

    win = ctk.CTkToplevel()

    input_field = ctk.CTkEntry(win)
    save_button = ctk.CTkButton(
        win,
        text="Save",
        command=lambda: save_audio(f"{input_field.get()}.wav", audio_data, win, root),
    )

    input_field.pack()
    save_button.pack()

    win.mainloop()
