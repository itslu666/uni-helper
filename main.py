import customtkinter as ctk
import os
from modules import frames

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
txt_frame = ctk.CTkFrame(root)

# make button for each lecture folder
for name in os.listdir("./data"):
    if name.endswith("_lecture") and os.path.isdir(os.path.join("./data", name)):
        # button test
        summary_button = ctk.CTkButton(
            nav_frame,
            corner_radius=0,
            height=40,
            width=180,
            border_spacing=10,
            text=name.split("_")[0],
            fg_color="transparent",
            text_color=("gray10", "gray90"),
            hover_color=("gray70", "gray30"),
            anchor="w",
            command=lambda: frames.select_frame_by_name(name, summary_button),
        )

new_button = ctk.CTkButton(
    root,
    corner_radius=0,
    height=40,
    width=180,
    border_spacing=10,
    text="New",
    fg_color="transparent",
    text_color=("gray10", "gray90"),
    hover_color=("gray70", "gray30"),
    anchor="w",
)


# show widgets
nav_frame.grid(row=0, column=0, sticky="nsew", pady=10, padx=(10, 5))
txt_frame.grid(row=0, column=1, sticky="nsew", pady=10, padx=(5, 10))
summary_button.grid(row=0, column=0, sticky="ew")
new_button.grid(row=1, column=0, sticky="nsew", pady=(0, 10), padx=(10, 5))

root.mainloop()
