import customtkinter as ctk


def show_files(lecture_folder_button, summary_button, quiz_button, cards_button):
    lecture_folder_button.configure(
        fg_color=("gray75", "gray25") if name == "test" else "transparent"
    )
    
    # show files
    summary_button.grid(row=row + 1, column=0, sticky="ew")
    quiz_button.grid(row=row + 2, column=0, sticky="ew")
    cards_button.grid(row=row + 3, column=0, sticky="ew")


def summary_frame(txt_frame):
    summary_frame = ctk.CTkFrame(txt_frame, border_width=0)

    ctk.CTkButton(summary_frame).pack()

    summary_frame.pack()
