import customtkinter as ctk
from PIL import Image


def open_new():
    root = ctk.CTkToplevel()

    # window scaling
    root.geometry("700x400")
    root.title("New Lecture")

    # button
    start_rec_button = ctk.CTkButton(
        root,
        width=30,
        corner_radius=360,
        height=30,
        text="",
        fg_color="transparent",
        hover_color="#2b2b2b",
        image=ctk.CTkImage(Image.open("./data/images/rec-button.png"), size=(50, 50)),
        command=button_click,
    )

    # drag and drop
    start_rec_button.pack()
    root.mainloop()
