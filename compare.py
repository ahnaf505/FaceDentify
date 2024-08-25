import face_recognition
import os

# Function to encode a face from an image file and save it with a UUID
def encode_face(imagepath):
    image = face_recognition.load_image_file(imagepath)
    face_encodings = face_recognition.face_encodings(image)
    
    if face_encodings:
        return face_encodings[0]
    else:
        return False

def comparewithtuple(imagepath, facencoding):
    if not os.path.exists(imagepath):
        return False

    image = face_recognition.load_image_file(imagepath)
    imgcoded = face_recognition.face_encodings(image)
    if imgcoded:
        res = face_recognition.compare_faces(imgcoded, facencoding)
        return res[0]
    else:
        return False
