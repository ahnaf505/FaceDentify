import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import pickle
from PIL import Image, ImageTk
import sys
import json
import os
from db import *
from compare import *

class ImageTextDialog(simpledialog.Dialog):
    def __init__(self, parent, title=None, image_path=None, text=None):
        self.image_path = image_path
        self.text = text
        self.image_label = None
        self.max_width = 400
        self.max_height = 400
        super().__init__(parent, title)

    def body(self, master):
        if self.image_path:
            self.original_image = Image.open(self.image_path)
            self.image_label = tk.Label(master)
            self.image_label.pack(pady=10)

        if self.text:
            text_label = tk.Label(master, text=self.text)
            text_label.pack(pady=10)

        # Update image initially
        self.update_image(self.max_width, self.max_height)

        # Bind the configure event for resizing
        master.bind("<Configure>", self.resize_event)

    def update_image(self, width, height):
        if self.image_label:
            # Maintain aspect ratio
            aspect_ratio = self.original_image.width / self.original_image.height

            # Calculate new dimensions based on the max size constraints
            new_width = min(self.max_width, self.original_image.width)
            new_height = int(new_width / aspect_ratio)

            if new_height > self.max_height:
                new_height = self.max_height
                new_width = int(new_height * aspect_ratio)

            # Use Image.Resampling.LANCZOS for resizing
            resized_image = self.original_image.resize((new_width, new_height), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(resized_image)
            
            self.image_label.config(image=photo)
            self.image_label.image = photo  # Keep a reference to prevent garbage collection

    def buttonbox(self):
        # Override buttonbox to only include an "OK" button
        box = tk.Frame(self)

        ok_button = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        ok_button.pack(side=tk.LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)

        box.pack()

    def apply(self):
        # Logic for when OK is pressed (if needed)
        pass

    def ok(self, event=None):
        # Close the dialog when "OK" is clicked or Enter is pressed
        self.apply()
        self.destroy()

    def resize_event(self, event):
        if self.winfo_exists():
            # Update the image size based on the current window size
            self.update_image(event.width, event.height)

def show_image_text_dialog(parent, title, image_path, text):
    ImageTextDialog(parent, title, image_path, text)


def run_operation(operation_number):
    try:
        if operation_number == 1:  # Insert Single Face
            filepath = filedialog.askopenfilename(title="Select Image")
            if not filepath:
                return
            faceencode = encode_face(filepath)
            if str(faceencode) == "False":
                log_output("No face detected in image or invalid image file!")
                return
            face_uuid = gen_id()
            save_face(faceencode, face_uuid)
            fullname = simple_input_dialog("Please input subject's Full Name")
            new_face(face_uuid, fullname)
            save_copy(filepath, face_uuid)
            log_output(f"New face added to the database with ID: {face_uuid}, and Full Name: {fullname}")

        elif operation_number == 2:  # Insert List of Faces
            jsonfilemname = filedialog.askopenfilename(title="Select JSON File", filetypes=[("JSON Files", "*.json")])
            if not jsonfilemname:
                return
            with open(jsonfilemname, 'r') as f:
                peoples = json.load(f)

            for i, people in enumerate(peoples):
                log_output(f"Processing JSON file record number: [{i+1}]")
                faceencode = encode_face(people['filepath'])
                if str(faceencode) == "False":
                    log_output(f"No face detected in image or invalid image file!, Full Name: {people['full_name']}")
                    return
                face_uuid = gen_id()
                save_face(faceencode, face_uuid)
                fullname = people['full_name']
                new_face(face_uuid, fullname)
                save_copy(people['filepath'], face_uuid)
                log_output(f"New face added with ID: {face_uuid}, Full Name: {fullname}")
                root.update_idletasks()

        elif operation_number == 3:  # Query Face from Image
            filename = filedialog.askopenfilename(title="Select Image")
            if not filename:
                return
            facencode = encode_face(filename)
            if str(facencode) == "False":
                log_output("No face detected in image or invalid image file!")
                return
            
            resultfound = False
            faces_dir = os.listdir("facedb")
            log_output("Searching db for similar faces...")
            for facedir in faces_dir:
                with open("facedb/"+facedir, 'rb') as f:
                    currencode = pickle.load(f)
                if comparewithtuple(filename, currencode):
                    log_output(f"Matched with Face ID:{facedir[:-5]}, Searching for full name...")
                    log_output(f"Matched Face ID: {facedir[:-5]} with Full Name: {search_fullname(facedir[:-5])[0]['fullname']}")
                    log_output(f"Database face image on path: imgfacedb/{facedir[:-5]}.png")
                    show_image_text_dialog(root, "Candidate Data", f"imgfacedb/{facedir[:-5]}.png", "Full Name: "+search_fullname(facedir[:-5])[0]['fullname'])
                    resultfound = True
                    break
            if not resultfound:
                log_output("No result found after going through the entire database!")

        elif operation_number == 4:  # Query Face by ID
            faceid = simple_input_dialog("Input Face ID")
            log_output("Searching db for similar faces...")
            if not faceid:
                return
            if search_fullname(faceid):
                log_output(f"Full Name: {search_fullname(faceid)[0]['fullname']}")
                log_output(f"Raw face image path: faceimgdb/{faceid}.png/jpg")
                show_image_text_dialog(root, "Candidate Data", f"imgfacedb/{faceid}.png", "Full Name: "+search_fullname(faceid)[0]['fullname'])
            else:
                log_output("No record found for the given ID!")

        elif operation_number == 5:  # Delete Face by Image
            filename = filedialog.askopenfilename(title="Select Image")
            if not filename:
                return
            facencode = encode_face(filename)
            if str(facencode) == "False":
                log_output("No face detected in image or invalid image file!")
                return
            
            resultfound = False
            faces_dir = os.listdir("facedb")
            log_output("Searching db for similar faces...")
            for facedir in faces_dir:
                with open("facedb/"+facedir, 'rb') as f:
                    currencode = pickle.load(f)
                if comparewithtuple(filename, currencode):
                    log_output(f"Matched with Face ID:{facedir[:-5]}, Searching for full name...")
                    log_output(f"Matched Face ID: {facedir[:-5]} with Full Name: {search_fullname(facedir[:-5])[0]['fullname']}")
                    resultfound = True
                    log_output("Deleting data related to the detected face...")
                    deleteface(facedir[:-5])
                    log_output("Successfully deleted all data related to the face!")
                    break
            if not resultfound:
                log_output("No result found after going through the entire database!")

        elif operation_number == 6:  # Delete Face by ID
            faceid = simple_input_dialog("Input Face ID to delete")
            if not faceid:
                return
            deleteface(faceid)
            log_output("Successfully deleted all data related to the face!")

        elif operation_number == 7:  # Clear Entire Database
            confirmation = messagebox.askyesno("Dangerous Operation", "This will completely delete the entire database. Are you sure?")
            if confirmation:
                confirmation2 = simple_input_dialog("Type 'COMPLETELYDELETE' to confirm")
                if confirmation2 == "COMPLETELYDELETE":
                    clearalldb()
                    log_output("Database cleared successfully.")
                else:
                    log_output("Database clear operation cancelled.")
            else:
                log_output("Database clear operation cancelled.")

    except Exception as e:
        log_output(f"Error: {str(e)}")

def log_output(message):
    print(message)  # Terminal output for logging
    log_area.config(state=tk.NORMAL)
    log_area.insert(tk.END, message + "\n")
    log_area.see(tk.END)
    log_area.config(state=tk.DISABLED)

def simple_input_dialog(prompt):
    return simpledialog.askstring("Input", prompt, parent=root)

# Tkinter UI Setup
root = tk.Tk()
root.title("FaceDentify")
root.geometry("500x500")


frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

# Buttons for each operation with numerical labels
operations = [
    (1, "Insert Single Face"),
    (2, "Insert List of Faces"),
    (3, "Query Face from Image"),
    (4, "Query Face by ID"),
    (5, "Delete Face by Image"),
    (6, "Delete Face by ID"),
    (7, "Clear Entire Database")
]

for number, operation in operations:
    btn = tk.Button(frame, text=f"{number}. {operation}", width=30, command=lambda num=number: run_operation(num))
    btn.pack(pady=5)

# Log area
log_area = tk.Text(root, height=10, width=50, state=tk.DISABLED)
log_area.pack(padx=10, pady=10)

check_filestrcture()
root.mainloop()
