def customers(main_frame):
    for widget in main_frame.winfo_children():
        widget.destroy()