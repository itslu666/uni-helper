import customtkinter as ctk
from tkinter import PhotoImage
def open_new():
    root = ctk.CTk()

    #window scaling
    root.geometry("700x400")
    root.title("New Lecture")
    #rec button
    img_rec_button = PhotoImage(file="data/images/rec-button.png")
    button = ctk.CTkButton(root, command=button_click,
                            border_color="red",
                            width=30,
                            height=30,
                            text="rec",
                            image=img_rec_button)
    button.grid(row=0, column=0, padx=20, pady=20)
    #drag and drop



    root.mainloop()
#click for the rec button
def button_click():
    print("buttonclick")
    return saund()
    #nimmt dann auf


def saund():
    #recording of and aduio
    print("klappt noch nicht")