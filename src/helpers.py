from PIL import Image, ImageTk
import tkinter as tk

def set_background(widget, image_file_path):
    """This function sets the background image for a given widget."""
    img = Image.open(image_file_path)
    photo = ImageTk.PhotoImage(img)
    label = tk.Label(widget, image=photo)
    label.image = photo  # To prevent garbage collection
    label.place(x=0, y=0, relwidth=1, relheight=1)

def clear_widgets(root):
    """This function will destroy any widgets you created."""
    for i in root.winfo_children():
        i.destroy()
