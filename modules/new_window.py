import customtkinter as ctk
from PIL import Image
from modules import sound
from tkinterdnd2 import TkinterDnD, DND_ALL


class Tk(ctk.CTkToplevel, TkinterDnD.DnDWrapper):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.TkdndVersion = TkinterDnD._require(self)


def open_new():
    new_window = Tk()
    new_window.title("New Lecture")

    new_window.grid_rowconfigure(0, weight=1)  # make row 0 expandable
    new_window.grid_columnconfigure(0, weight=1)  # make column 0 expandable

    # thread container for record thread
    thread_container = [None]

    # images for buttons
    start_image = ctk.CTkImage(
        Image.open("./data/images/rec-button.png"), size=(50, 50)
    )
    stop_image = ctk.CTkImage(
        Image.open("./data/images/stop-button.png"), size=(50, 50)
    )

    # buttons
    stop_rec_button = ctk.CTkButton(
        new_window,
        width=30,
        height=30,
        text="",
        fg_color="transparent",
        hover_color="#242424",
        image=stop_image,
    )

    start_rec_button = ctk.CTkButton(
        new_window,
        width=30,
        height=30,
        text="",
        fg_color="transparent",
        hover_color="#242424",
        image=start_image,
        command=lambda: sound.start_rec(
            start_rec_button, stop_rec_button, thread_container, new_window
        ),
    )

    def get_path(event):
        print(event.data)

    # drop down frame
    dnd_frame = ctk.CTkFrame(new_window, width=500, height=500)
    dnd_frame.drop_target_register(DND_ALL)
    dnd_frame.dnd_bind("<<Drop>>", get_path)
    dnd_frame.grid_propagate(False)

    dnd_label = ctk.CTkLabel(dnd_frame, text="Drop Audio Files Here")
    dnd_label.pack(expand=True, fill="both", padx=100, pady=100)

    start_rec_button.grid(row=0, column=0, sticky="nsew", pady=(10, 0))
    dnd_frame.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

    new_window.mainloop()
