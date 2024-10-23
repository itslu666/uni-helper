import customtkinter as ctk
import os
from modules import frames, new_window


def make_lecture_dropdowns(options, selected_option, name):
    lecture_label = ctk.CTkLabel(nav_frame, text=name)

    lecture_dropdown = ctk.CTkOptionMenu(
        nav_frame,
        command=lambda val: selected_option.set(val),
        variable=selected_option,
        values=options,
    )

    lecture_dropdown.grid(row=0, column=0)


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

# var for rows for nav buttons
row = 0

# var to track file visibility
file_visibility = {}


# make button for each lecture folder
for name in os.listdir("./data/lectures"):
    if name.endswith("_lecture") and os.path.isdir(
        os.path.join("./data/lectures", name)
    ):
        make_lecture_dropdowns(
            ["test", "test2", "test3"], ctk.StringVar(value="hallo"), name
        )

        # make summary button
        if os.path.isfile(os.path.join(f"./data/lectures/{name}/summary.txt")):
            summary_button = ctk.CTkButton(
                nav_frame,
                corner_radius=0,
                height=40,
                width=180,
                border_spacing=10,
                text="Summary",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                command=lambda: frames.summary_frame(txt_frame),
            )

        if os.path.isfile(os.path.join(f"./data/lectures/{name}/quiz.txt")):
            quiz_button = ctk.CTkButton(
                nav_frame,
                corner_radius=0,
                height=40,
                width=180,
                border_spacing=10,
                text="Quiz",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                command=lambda: frames.show_files(
                    file_visibility,
                    name,
                    lecture_folder_button,
                    summary_button,
                    quiz_button,
                    cards_button,
                    row,
                ),
            )

        if os.path.isfile(os.path.join(f"./data/lectures/{name}/flash_cards.txt")):
            cards_button = ctk.CTkButton(
                nav_frame,
                corner_radius=0,
                height=40,
                width=180,
                border_spacing=10,
                text="Flash Cards",
                fg_color="transparent",
                text_color=("gray10", "gray90"),
                hover_color=("gray70", "gray30"),
                command=lambda: frames.show_files(
                    file_visibility,
                    name,
                    lecture_folder_button,
                    summary_button,
                    quiz_button,
                    cards_button,
                    row,
                ),
            )

        # set name for file visibility
        file_visibility[name] = False

        # show buttons
        # lecture_folder_button.grid(row=row, column=0, sticky="ew")

        row += 1

new_button = ctk.CTkButton(
    root,
    corner_radius=4,
    height=40,
    width=180,
    border_spacing=10,
    text="New",
    fg_color="#2b2b2b",
    text_color=("gray10", "gray90"),
    hover_color=("gray70", "gray30"),
    anchor="w",
    command=new_window.open_new,
)


# show widgets
nav_frame.grid(row=0, column=0, sticky="nsew", pady=10, padx=(10, 5))
txt_frame.grid(row=0, column=1, sticky="nsew", pady=10, padx=(5, 10))
new_button.grid(row=1, column=0, sticky="nsew", pady=(0, 10), padx=(10, 5))

root.mainloop()
