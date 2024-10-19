import customtkinter as ctk

# initial root window
root = ctk.CTk()
root.title("Uni Helper")
root.geometry("800x500")

# configure grid layout for resizing
root.grid_rowconfigure(0, weight=1)  # make row 0 expandable
root.grid_columnconfigure(1, weight=1)  # make column 0 expandable

# make widgets
# frames
nav_frame = ctk.CTkFrame(root)

# tabview
tabview = ctk.CTkTabview(root)
tabview.add("Summary")
tabview.add("Quiz")
tabview.add("Flash Cards")

# button test
button = ctk.CTkButton(
    nav_frame,
    corner_radius=0,
    height=40,
    border_spacing=10,
    text="test",
    fg_color="transparent",
    text_color=("gray10", "gray90"),
    hover_color=("gray70", "gray30"),
    anchor="w",
)  # change fg color when clicked (change other buttons back to og color)

# show widgets
nav_frame.grid(row=0, column=0, sticky="nsew", pady=10, padx=(10, 5))
tabview.grid(row=0, column=1, sticky="nsew", pady=10, padx=(5, 10))
button.grid(row=0, column=0, sticky="ew")

root.mainloop()
