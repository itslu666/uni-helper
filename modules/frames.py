import customtkinter as ctk


def show_files(
    file_visibility,
    name,
    lecture_folder_button,
    summary_button,
    quiz_button,
    cards_button,
    row,
):
    # Toggle the visibility state
    file_visibility[name] = not file_visibility[name]

    # Update button appearance based on visibility state
    if file_visibility[name]:
        lecture_folder_button.configure(fg_color=("gray75", "gray25"))
        # Show the files
        summary_button.grid(row=row + 1, column=0, sticky="ew")
        quiz_button.grid(row=row + 2, column=0, sticky="ew")
        cards_button.grid(row=row + 3, column=0, sticky="ew")
    else:
        lecture_folder_button.configure(fg_color="transparent")
        # Hide the files
        summary_button.grid_remove()
        quiz_button.grid_remove()
        cards_button.grid_remove()


def summary_frame(txt_frame):
    summary_frame = ctk.CTkFrame(txt_frame, border_width=0)

    ctk.CTkButton(summary_frame).pack()

    summary_frame.pack()
