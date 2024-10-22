import customtkinter as ctk
from PIL import Image


def open_new():
    root = ctk.CTkToplevel()

    # window scaling
    root.geometry("700x400")
    root.title("New Lecture")

    # button
    button = ctk.CTkButton(
        root,
        width=30,
        height=30,
        text="",
        image=ctk.CTkImage(Image.open("./data/images/rec-button.png"), size=(50, 50)),
        command=button_click,
    )
    # drag and drop

    button.pack()
    root.mainloop()


# click for the rec button
def button_click():
    print("buttonclick")
    return saund()
    # nimmt dann auf


def saund():
    # recording of and aduio
    print("klappt noch nicht")
