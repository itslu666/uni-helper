import customtkinter as ctk

# initial root window
root = ctk.CTk()
root.title("Uni Helper")
root.geometry("800x500")

# make widgets
# tabview
tabview = ctk.CTkTabview(root)
tabview.add("Summary")
tabview.add("Quiz")
tabview.add("Flash Cards")

# show widgets
tabview.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()