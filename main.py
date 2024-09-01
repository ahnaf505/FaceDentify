import os
import sys
import json
import pickle
from db import *
from compare import *
from tqdm import tqdm

print("Initializing...")
if not check_filestrcture():
    print("Invalid file structure detected!")
    print("Fixing file structure...")

print("FaceDentify\n")
print("1. Insert new single face into database")
print("2. Insert a list of faces into database")
print("3. Query face from biometric recognition")
print("4. Query face from Face ID")
print("5. Delete face from biometric recognition")
print("6. Delete face from Face ID")
print("7. Clear entire database CAUTION!!! REALLY DANGEROUS OPERATION")

menu = input("Please select menu ==> ")

if menu == "1":
    filepath = input("\nInput image candidate filename ==> ")
    faceencode = encode_face(filepath)
    if faceencode is None or not faceencode.any():
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
    
    total_records = len(peoples)
    for i, people in enumerate(peoples):
        sys.stdout.write(f"\rProcessing json file record number: [{i+1}/{total_records}]")
        sys.stdout.flush()
        faceencode = encode_face(people['filepath'])
        if faceencode is None or not faceencode.any():
            print(f"\nNo face detected in image or invalid image file!, Full Name: {people['full_name']}")
            continue
        face_uuid = gen_id()
        save_face(faceencode, face_uuid)
        fullname = people['full_name']
        new_face(face_uuid, fullname)
        save_copy(people['filepath'], face_uuid)
        print(f"\nNew face added to the database with ID: {face_uuid}, and Full Name: {fullname}")

elif menu == "3":
    filename = input("\nInput candidate image file name ==> ")
    facencode = encode_face(filename)
    if facencode is None or not facencode.any():
        print("No face detected in image or invalid image file!")
        sys.exit()
    
    resultfound = False
    faces_dir = os.listdir("facedb")
    print("Searching db for similar faces...")
    
    with tqdm(faces_dir, desc="Progress", unit="face") as pbar:
        for facedir in pbar:
            with open(f"facedb/{facedir}", 'rb') as f:
                currencode = pickle.load(f)
            if comparewithtuple(filename, currencode):
                face_id = facedir[:-5]
                fullname = search_fullname(face_id)[0]['fullname']
                pbar.close()

                print(f"\nMatched with Face ID: {face_id} Searching for full name...")
                print(f"Matched Face ID: {face_id} with Full Name: {fullname}")
                print(f"Database face image on path: imgfacedb/{face_id}.png")
                resultfound = True
                break
    
    if not resultfound:
        print("\nNo result found after going through the entire database!")

elif menu == "4":
    faceid = input("Input Face ID ==> ")
    record = search_fullname(faceid)
    if record:
        fullname = record[0]['fullname']
        print(f"Full Name: {fullname}")
        print(f"Raw face image path: faceimgdb/{record[0]['faceid']}.png/jpg")
    else:
        print("No record found from the given ID!")

elif menu == "5":
    filename = input("\nInput candidate image file name ==> ")
    facencode = encode_face(filename)
    if facencode is None or not facencode.any():
        print("No face detected in image or invalid image file!")
        sys.exit()
    
    resultfound = False
    faces_dir = os.listdir("facedb")
    print("Searching db for similar faces...")
    
    with tqdm(total=len(faces_dir), desc="Progress", unit="face") as pbar:
        for facedir in faces_dir:
            with open(f"facedb/{facedir}", 'rb') as f:
                currencode = pickle.load(f)
    
            if comparewithtuple(filename, currencode):
                face_id = facedir[:-5]
                fullname = search_fullname(face_id)[0]['fullname']
    
                pbar.close()
                print(f"\nMatched with Face ID: {face_id}. Searching for full name...")
                print(f"Matched Face ID: {face_id} with Full Name: {fullname}")
                print("Deleting data related to the detected face...")
    
                deleteface(face_id)
    
                print("Successfully deleted all data related to the face!")
                resultfound = True
                break
            
    if not resultfound:
        print("\nNo result found after going through the entire database!")

elif menu == "6":
    faceid = input("Input Face ID to delete ==> ")
    deleteface(faceid)
    print("Successfully deleted all data related to the face!")

elif menu == "7":
    print("REALLY DANGEROUS OPERATION, THIS CANNOT BE UNDONE.")
    if input("Please type '9840nfd9' to continue ==> ") != "9840nfd9":
        print("Database Clear operation cancelled...")
        sys.exit()
    if input("Type 'COMPLETELYDELETE' to completely delete the entire database ==> ") == "COMPLETELYDELETE":
        clearalldb()
        print("Database cleared.")
    else:
        print("Database Clear operation cancelled...")
