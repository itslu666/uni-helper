def select_frame_by_name(name, summary_button):
    if name == "Summary":
        summary_button.configure(fg_color=("gray75", "gray25") if name == "Summary" else "transparent")
        print("select summary frame")
