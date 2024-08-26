import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import os

messagebox.

# Function to process the text input when Enter is pressed
def on_enter(event):
    label_text = textbox.get()
    print(f"Label entered: {label_text}")
    textbox.delete(0, tk.END)
    load_next_image()  # Load the next image after labeling

# Function to load and display the next image in the folder
def load_next_image():
    global current_image_index, images
    if current_image_index < len(images):
        image_path = os.path.join(image_folder, images[current_image_index])
        image = Image.open(image_path)
        image = image.resize((300, 300), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(image)
        image_label.config(image=img)
        image_label.image = img
        current_image_index += 1
    else:
        print("No more images to label.")
        root.quit()  # Exit the application when all images are labeled

# Set up the main window
root = tk.Tk()
root.title("Simple Image Labeler")

# Folder containing images
image_folder = 'path/to/your/image/folder'  # Replace with your folder path

# Get a list of images in the folder
images = [f for f in os.listdir(image_folder) if f.endswith(('.png', '.jpg', '.jpeg'))]
current_image_index = 0

# Label to display the image
image_label = tk.Label(root)
image_label.pack()

# Textbox for entering the label
textbox = tk.Entry(root)
textbox.pack()
textbox.bind("<Return>", on_enter)  # Bind Enter key to the on_enter function

# Load the first image
load_next_image()

# Start the Tkinter event loop
root.mainloop()
