import os
import shutil
from tkinter import Tk, Label, Button, Entry, StringVar, messagebox
import uuid
import json
from PIL import Image, ImageTk

run_id = str(uuid.uuid4())
os.mkdir(f"labeled_{run_id}")
db_file = f'labeldb_{run_id}.json'

class ImageLabeler:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Labeler")
        self.root.geometry("600x600")
        
        self.source_folder = 'faceimg'
        self.dest_folder = f'labeled_{run_id}'

        self.images = [f for f in os.listdir(self.source_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        self.current_index = 0

        if not self.images:
            messagebox.showerror("Error! No image found.", "No image found in the 'faceimg' folder. Please close this window.")
            self.root.quit()
            return

        self.label_var = StringVar()
        
        self.image_display = Label(root)
        self.image_display.pack()

        self.entry_label = Label(root, text="Enter Full Name:")
        self.entry_label.pack()

        self.name_entry = Entry(root, textvariable=self.label_var)
        self.name_entry.pack()
        self.name_entry.bind("<Return>", self.handle_enter)
        self.name_entry.focus()

        self.next_button = Button(root, text="Next", command=self.next_image)
        self.next_button.pack()

        self.show_image()

    def show_image(self):
        if self.current_index < len(self.images):
            image_path = os.path.join(self.source_folder, self.images[self.current_index])
            image = Image.open(image_path)
            image.thumbnail((500, 500))
            photo_image = ImageTk.PhotoImage(image)
            self.image_display.config(image=photo_image)
            self.image_display.image = photo_image

    def next_image(self):
        label = self.label_var.get().strip()
        if label:
            image_name = self.images[self.current_index]
            source_path = os.path.join(self.source_folder, image_name)
            new_id = label + "__" + str(uuid.uuid1())
            dest_path = os.path.join(self.dest_folder, f"{new_id}.png")
            
            if os.path.exists(db_file):
                with open(db_file, 'r') as file:
                    data = json.load(file)
            else:
                data = []
                
            new_entry = [{"full_name": label, "filepath": f"labeled_{run_id}/{new_id}.png"}]
            data.extend(new_entry)
            
            with open(db_file, 'w') as file:
                json.dump(data, file, indent=4)
                
            print(f"New entries have been added to {db_file}")
            shutil.move(source_path, dest_path)
            self.label_var.set("")
            self.current_index += 1
            
            if self.current_index < len(self.images):
                self.show_image()
            else:
                self.root.quit()

    def handle_enter(self, event):
        self.next_image()

if __name__ == "__main__":
    root = Tk()
    app = ImageLabeler(root)
    root.mainloop()
