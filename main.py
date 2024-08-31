import tkinter as tk
from tkinter import ttk, filedialog as fileDialog, messagebox as msgBox, simpledialog as simpleDialog
import pickle as pickleLib
from PIL import Image as ImageLib, ImageTk as ImageTkLib
import sys as sysLib
import json as jsonLib
import os as osLib
from db import *
from compare import *

class FaceInfoDialog(simpleDialog.Dialog):
    def __init__(self, parentWindow, dialogTitle=None, imageFilePath=None, infoText=None):
        self.imageFilePath = imageFilePath
        self.infoText = infoText
        self.imageLabel = None
        self.maxWidth = 400
        self.maxHeight = 400
        super().__init__(parentWindow, dialogTitle)

    def body(self, dialogFrame):
        if self.imageFilePath:
            self.originalImage = ImageLib.open(self.imageFilePath)
            self.imageLabel = tk.Label(dialogFrame)
            self.imageLabel.pack(pady=10)
        if self.infoText:
            textLabel = tk.Label(dialogFrame, text=self.infoText)
            textLabel.pack(pady=10)
        self.updateImage(self.maxWidth, self.maxHeight)
        dialogFrame.bind("<Configure>", self.onResize)

    def updateImage(self, width, height):
        if self.imageLabel:
            aspectRatio = self.originalImage.width / self.originalImage.height
            newWidth = min(self.maxWidth, self.originalImage.width)
            newHeight = int(newWidth / aspectRatio)
            if newHeight > self.maxHeight:
                newHeight = self.maxHeight
                newWidth = int(newHeight * aspectRatio)
            resizedImage = self.originalImage.resize((newWidth, newHeight), ImageLib.Resampling.LANCZOS)
            photoImage = ImageTkLib.PhotoImage(resizedImage)
            self.imageLabel.config(image=photoImage)
            self.imageLabel.image = photoImage

    def buttonbox(self):
        buttonFrame = tk.Frame(self)
        okButton = tk.Button(buttonFrame, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        okButton.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        buttonFrame.pack()

    def apply(self):
        pass

    def ok(self, event=None):
        self.apply()
        self.destroy()

    def onResize(self, event):
        if self.winfo_exists():
            self.updateImage(event.width, event.height)

def showFaceInfoDialog(parentWindow, dialogTitle, imageFilePath, infoText):
    FaceInfoDialog(parentWindow, dialogTitle, imageFilePath, infoText)

def executeOperation(operationCode):
    try:
        if operationCode == 1:
            selectedFilePath = fileDialog.askopenfilename(title="Select Image")
            if not selectedFilePath:
                return
            encodedFace = encode_face(selectedFilePath)
            if str(encodedFace) == "False":
                logMessage("No face detected in image or invalid image file!")
                return
            faceId = gen_id()
            save_face(encodedFace, faceId)
            fullName = promptUserInput("Please input subject's Full Name")
            new_face(faceId, fullName)
            save_copy(selectedFilePath, faceId)
            logMessage(f"New face added to the database with ID: {faceId}, and Full Name: {fullName}")

        elif operationCode == 2:
            jsonFilePath = fileDialog.askopenfilename(title="Select JSON File", filetypes=[("JSON Files", "*.json")])
            if not jsonFilePath:
                return
            with open(jsonFilePath, 'r') as jsonFile:
                peopleData = jsonLib.load(jsonFile)
            for i, person in enumerate(peopleData):
                logMessage(f"Processing JSON file record number: [{i+1}]")
                encodedFace = encode_face(person['filepath'])
                if str(encodedFace) == "False":
                    logMessage(f"No face detected in image or invalid image file!, Full Name: {person['full_name']}")
                    return
                faceId = gen_id()
                save_face(encodedFace, faceId)
                fullName = person['full_name']
                new_face(faceId, fullName)
                save_copy(person['filepath'], faceId)
                logMessage(f"New face added with ID: {faceId}, Full Name: {fullName}")
                root.update_idletasks()

        elif operationCode == 3:
            selectedImagePath = fileDialog.askopenfilename(title="Select Image")
            if not selectedImagePath:
                return
            encodedFace = encode_face(selectedImagePath)
            if str(encodedFace) == "False":
                logMessage("No face detected in image or invalid image file!")
                return
            foundMatch = False
            faceDbFiles = osLib.listdir("facedb")
            logMessage("Searching db for similar faces...")
            for faceFile in faceDbFiles:
                with open("facedb/"+faceFile, 'rb') as dbFile:
                    currentEncodedFace = pickleLib.load(dbFile)
                if comparewithtuple(selectedImagePath, currentEncodedFace):
                    logMessage(f"Matched with Face ID:{faceFile[:-5]}, Searching for full name...")
                    logMessage(f"Matched Face ID: {faceFile[:-5]} with Full Name: {search_fullname(faceFile[:-5])[0]['fullname']}")
                    logMessage(f"Database face image on path: imgfacedb/{faceFile[:-5]}.png")
                    showFaceInfoDialog(root, "Candidate Data", f"imgfacedb/{faceFile[:-5]}.png", "Full Name: "+search_fullname(faceFile[:-5])[0]['fullname'])
                    foundMatch = True
                    break
            if not foundMatch:
                logMessage("No result found after going through the entire database!")

        elif operationCode == 4:
            faceIdInput = promptUserInput("Input Face ID")
            logMessage("Searching db for similar faces...")
            if not faceIdInput:
                return
            if search_fullname(faceIdInput):
                logMessage(f"Full Name: {search_fullname(faceIdInput)[0]['fullname']}")
                logMessage(f"Raw face image path: faceimgdb/{faceIdInput}.png/jpg")
                showFaceInfoDialog(root, "Candidate Data", f"imgfacedb/{faceIdInput}.png", "Full Name: "+search_fullname(faceIdInput)[0]['fullname'])
            else:
                logMessage("No record found for the given ID!")

        elif operationCode == 5:
            selectedImagePath = fileDialog.askopenfilename(title="Select Image")
            if not selectedImagePath:
                return
            encodedFace = encode_face(selectedImagePath)
            if str(encodedFace) == "False":
                logMessage("No face detected in image or invalid image file!")
                return
            foundMatch = False
            faceDbFiles = osLib.listdir("facedb")
            logMessage("Searching db for similar faces...")
            for faceFile in faceDbFiles:
                with open("facedb/"+faceFile, 'rb') as dbFile:
                    currentEncodedFace = pickleLib.load(dbFile)
                if comparewithtuple(selectedImagePath, currentEncodedFace):
                    logMessage(f"Matched with Face ID:{faceFile[:-5]}, Searching for full name...")
                    logMessage(f"Matched Face ID: {faceFile[:-5]} with Full Name: {search_fullname(faceFile[:-5])[0]['fullname']}")
                    foundMatch = True
                    logMessage("Deleting data related to the detected face...")
                    deleteface(faceFile[:-5])
                    logMessage("Successfully deleted all data related to the face!")
                    break
            if not foundMatch:
                logMessage("No result found after going through the entire database!")

        elif operationCode == 6:
            faceIdInput = promptUserInput("Input Face ID to delete")
            if not faceIdInput:
                return
            deleteface(faceIdInput)
            logMessage("Successfully deleted all data related to the face!")

        elif operationCode == 7:
            confirmClearDb = msgBox.askyesno("Dangerous Operation", "This will completely delete the entire database. Are you sure?")
            if confirmClearDb:
                finalConfirmation = promptUserInput("Type 'COMPLETELYDELETE' to confirm")
                if finalConfirmation == "COMPLETELYDELETE":
                    clearalldb()
                    logMessage("Database cleared successfully.")
                else:
                    logMessage("Database clear operation cancelled.")
            else:
                logMessage("Database clear operation cancelled.")
    except Exception as e:
        logMessage(f"Error: {str(e)}")

def logMessage(messageText):
    print(messageText)
    logTextArea.config(state=tk.NORMAL)
    logTextArea.insert(tk.END, messageText + "\n")
    logTextArea.see(tk.END)
    logTextArea.config(state=tk.DISABLED)

def promptUserInput(promptText):
    return simpleDialog.askstring("Input", promptText, parent=root)

root = tk.Tk()
root.title("FaceDentify")
root.geometry("500x500")

mainFrame = tk.Frame(root)
mainFrame.pack(padx=10, pady=10)

operationsList = [
    (1, "Insert Single Face"),
    (2, "Insert List of Faces"),
    (3, "Query Face from Image"),
    (4, "Query Face by ID"),
    (5, "Delete Face by Image"),
    (6, "Delete Face by ID"),
    (7, "Clear Entire Database")
]

for operationCode, operationName in operationsList:
    operationButton = tk.Button(mainFrame, text=f"{operationCode}. {operationName}", width=30, command=lambda code=operationCode: executeOperation(code))
    operationButton.pack(pady=5)

logTextArea = tk.Text(root, height=10, width=50, state=tk.DISABLED)
logTextArea.pack(padx=10, pady=10)

check_filestrcture()
root.mainloop()
