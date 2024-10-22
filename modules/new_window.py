import customtkinter as ctk
from PIL import Image
def open_new():
    root = ctk.CTk()

    #window scaling
    root.geometry("700x400")
    root.title("New Lecture")
    #load and rezize image
    img_rec_button = Image.open("./data/images/rec-button.png")
    #convert image in ctk compatible 
    #tk_image = ImageTk.PhotoImage(img_rec_button)
    button_image = ctk.CTkImage(img_rec_button)
    #button 
    button = ctk.CTkButton(root,
                            width=30,
                            height=30,
                            text="rec",
                            image=button_image,
                            command=button_click)
    #drag and drop


    button.pack()
    root.mainloop()
#click for the rec button
def button_click():
    print("buttonclick")
    return saund()
    #nimmt dann auf


def saund():
    #recording of and aduio
    print("klappt noch nicht")