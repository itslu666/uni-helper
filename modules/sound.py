import customtkinter as ctk
import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
import wave
import threading
from modules import files_management
import os


def start_rec(start_button, stop_button, thread_container, new_window):
    print("start recording")

    # show stop button
    stop_button.grid(row=0, column=0, pady=(10, 0))
    start_button.destroy()

    audio_data = []
    is_recording = [True]

    def rec_audio():
        def callback(indata, frames, time, status):
            if status:
                print(status)
            if is_recording[0]:
                print(f"Received {frames} frames of audio data.")
                audio_data.append(indata.copy())

        with sd.InputStream(samplerate=44100, channels=2, callback=callback):
            while is_recording[0]:
                sd.sleep(100)

    def stop_rec():
        print("stopping")
        is_recording[0] = False
        thread_container[0].join()
        show_file_naming_win(audio_data, new_window)

    stop_button.configure(command=stop_rec)

    recording_thread = threading.Thread(target=rec_audio)
    thread_container[0] = recording_thread
    recording_thread.start()


def save_audio(filename, audio_data, new_window):
    if not audio_data:
        print("No audio data to save.")
        return

    print("creating new folder...")
    lecture_name = files_management.get_new_foldername(filename)
    os.mkdir(os.path.join("./data/lectures", lecture_name))

    print("saving audio...")
    audio_np = np.concatenate(audio_data, axis=0)
    print(f"Audio data shape: {audio_np.shape}, dtype: {audio_np.dtype}")

    if audio_np.size == 0:
        print("Audio data is empty after concatenation.")
        return

    with wave.open(
        "./data/lectures/" + lecture_name + f"/{lecture_name}_audio" + ".wav", "wb"
    ) as wf:
        wf.setnchannels(2)
        wf.setsampwidth(2)
        wf.setframerate(44100)
        wf.writeframes(audio_np.astype(np.int16).tobytes())

        new_window.destroy()
        print("new_window destroyed")


def show_file_naming_win(audio_data, new_window):
    frame = ctk.CTkFrame(new_window)

    input_field = ctk.CTkEntry(frame)
    save_button = ctk.CTkButton(
        frame,
        text="Save",
        command=lambda: save_audio(f"{input_field.get()}", audio_data, new_window),
    )

    input_field.pack(expand=True, fill="both", pady=(0, 5))
    save_button.pack(expand=True, fill="both")
    frame.grid(row=0, column=0, padx=10, pady=10)
