import tkinter as tk

# Create window
root = tk.Tk()
root.title("Sorry Slide")
root.geometry("800x500")
root.configure(bg="#f7d9e3")

# Main message
title = tk.Label(
    root,
    text="I'm Sorry 💗",
    font=("Arial", 50, "bold"),
    fg="#c2185b",
    bg="#f7d9e3"
)
title.pack(pady=80)

# Apology message
message = tk.Label(
    root,
    text="I didn't mean to hurt you.\nPlease forgive me.",
    font=("Arial", 24),
    fg="#5a3d46",
    bg="#f7d9e3"
)
message.pack(pady=20)

# Button
button = tk.Button(
    root,
    text="Forgive Me ❤️",
    font=("Arial", 18, "bold"),
    bg="#c2185b",
    fg="white",
    padx=20,
    pady=10,
    command=root.destroy
)
button.pack(pady=30)

root.mainloop()