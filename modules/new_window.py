import customtkinter as ctk
from PIL import Image
from modules import sound


def open_new():
    root = ctk.CTkToplevel()

    # window scaling
    root.geometry("700x400")
    root.title("New Lecture")

    # thread container for record thread
    thread_container = [None]

    # button
    start_rec_button = ctk.CTkButton(
        root,
        width=30,
        height=30,
        text="",
        fg_color="transparent",
        hover_color="#242424",
        image=ctk.CTkImage(Image.open("./data/images/rec-button.png"), size=(50, 50)),
        command=lambda: sound.start_rec(
            start_rec_button, stop_rec_button, thread_container, root
        ),
    )

    stop_rec_button = ctk.CTkButton(root, width=30, height=30, text="", image=ctk.CTkImage(Image.open("./data/images/stop2-button.png"), size=(50, 50))
    )

    # add drag and drop
    

    start_rec_button.grid(row=0, column=0, sticky="nsew")
    root.mainloop()
