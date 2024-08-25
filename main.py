print("Initializing...")
from db import *
import pickle
import sys
import json
from compare import *
isvalidfile = check_filestrcture()
if isvalidfile:
    print("Proper file structure detected!")
else:
    print("Invalid file structure detected!")
    print("Fixing file structure...")
S
# Simple debug menu.
print("FaceDentify\n")
print("1. Insert new single face into database")
print("2. Insert a lists of faces into database")
print("3. Query face from biometric recognition")
print("4. Query face from Face ID")
print("5. Delete face from biometric recognition")
print("6. Delete face from Face ID")
print("7. Clear entire database CAUTION!!! REALLY DANGEROUS OPERATION")

# User menu input field.
menu = input("Please select menu ==> ")

if menu == "1":
    filepath = input("\nInput image candidate filename ==> ")
    faceencode = encode_face(filepath)
    if str(faceencode) == "False":
        print("No face detected in image or invalid image file!")
        sys.exit()
    face_uuid = gen_id()
    save_face(faceencode, face_uuid)
    fullname = input("Please input subject's Full Name ==> ")
    new_face(face_uuid, fullname)
    save_copy(filepath, face_uuid)
    print(f"New face added to the database with ID: {face_uuid}, and Full Name: {fullname}")

elif menu == "2":
    print("Please format the json file using the following format:")
    print("""   [
        {
            "full_name": "Will Smith",
            "filepath": "directory/9400248.png"
        },
        {
            "full_name": "Will John",
            "filepath": "directory/9489848.png"
        },
        {
            "full_name": "Willyam Dan",
            "filepath": "directory/9499048.png"
        }
    ]\n\n""")
    jsonfilemname = input("JSON filename ==> ")
    with open(jsonfilemname, 'r') as f:
        peoples = json.load(f)
    
    for i, people in enumerate(peoples):
        print(f"Processing json file record number: [{i+1}]")
        faceencode = encode_face(people['filepath'])
        if str(faceencode) == "False":
            print(f"No face detected in image or invalid image file!, Full Name: {people['full_name']}")
            sys.exit()
        face_uuid = gen_id()
        save_face(faceencode, face_uuid)
        fullname = people['full_name']
        new_face(face_uuid, fullname)
        save_copy(people['filepath'], face_uuid)
        print(f"\nNew face added to the database with ID: {face_uuid}, and Full Name: {fullname}")
elif menu == "3":
    filename = input("\nInput candidate image file name ==> ")
    facencode = encode_face(filename)
    if str(facencode) == "False":
        print("No face detected in image or invalid image file!")
        sys.exit()
    
    resultfound = False
    faces_dir = os.listdir("facedb")
    print("Searching db for similar faces...")
    for facedir in faces_dir:
        with open("facedb/"+facedir, 'rb') as f:
            currencode = pickle.load(f)
        if comparewithtuple(filename, currencode) == True:
            print(f"Matched with Face ID:{facedir[:-5]} Searching for full name...")
            print(f"Matched Face ID: {facedir[:-5]} with Full Name: {search_fullname(facedir[:-5])[0]['fullname']}")
            resultfound = True
            break
    if resultfound == False:
        print("No result found after going through the entire database!")
    
elif menu == "4":
    faceid = input("Input Face ID ==> ")
    if search_fullname(faceid):
        print(f"Full Name: {search_fullname(faceid)[0]['fullname']}")
        print(f"Raw face image path: {search_fullname(faceid)[0]['faceid']}.png/jpg")
    else:
        print("No record found from the given ID!")

elif menu == "5":
    filename = input("\nInput candidate image file name ==> ")
    facencode = encode_face(filename)
    if str(facencode) == "False":
        print("No face detected in image or invalid image file!")
        sys.exit()
    
    resultfound = False
    faces_dir = os.listdir("facedb")
    print("Searching db for similar faces...")
    for facedir in faces_dir:
        with open("facedb/"+facedir, 'rb') as f:
            currencode = pickle.load(f)
        if comparewithtuple(filename, currencode) == True:
            print(f"Matched with Face ID:{facedir[:-5]} Searching for full name...")
            print(f"Matched Face ID: {facedir[:-5]} with Full Name: {search_fullname(facedir[:-5])[0]['fullname']}")
            resultfound = True
            print("Deleting data related to the detected face...")
            deleteface(facedir[:-5])
            print("Succesfully deleted all data related to the face!")
            break
    if resultfound == False:
        print("No result found after going through the entire database!")

elif menu == "6":
    faceid= input("Input Face ID to delete ==> ")
    deleteface(faceid)
    print("Succesfully deleted all data related to the face!")

elif menu == "7":
    print("REALLY DANGEROUS OPERATION, THIS CANNOT BE UNDONE.")
    isdelete1 = input("Please type '9840nfd9' to continue ==> ")
    if isdelete1 == "9840nfd9":
        pass
    else:
        print("Database Clear operation cancelled...")
        sys.exit()
    isdelete2 = input("Type 'COMPLETELYDELETE' to completely delete the entire database ==> ")
    if isdelete2 == "COMPLETELYDELETE":
        clearalldb()
    else:
        print("Database Clear operation cancelled...")
        sys.exit()