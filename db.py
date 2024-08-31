from tinydb import TinyDB, Query
import os
import pickle
import uuid
import shutil
import sys

db = TinyDB('fullnames.json')

que = Query()

def check_filestrcture():
    isvalid1 = os.path.exists(os.path.join(os.getcwd(), 'facedb'))
    isvalid2 = os.path.exists(os.path.join(os.getcwd(), 'imgfacedb'))

    if isvalid1:
        pass
    else:
        os.mkdir('facedb')
    if isvalid2:
        return True
    else:
        os.mkdir('imgfacedb')
        return False

def new_face(faceid, fullname):
    db.insert({'faceid': str(faceid), 'fullname': fullname})

def save_copy(imgpath, uuid):
    shutil.copy(imgpath, f"imgfacedb/{uuid}.png")

def gen_id():
    while True:
        new_uid = uuid.uuid4()
        if db.search(que.faceid == new_uid):
            return
        else:
            return new_uid
    
def deleteface(uid):
    try:
        os.remove(f"imgfacedb/{uid}.png")
    except:
        pass

    try:
        os.remove(f"imgfacedb/{uid}.jpg")
    except:
        pass
    
    try:
        os.remove(f"imgfacedb/{uid}.jpeg")
    except:
        pass
    
    try:
        os.remove(f"facedb/{uid}.face")
    except:
        pass
    
    try:
        db.remove(que.faceid == uid)
    except:
        pass

def clearalldb():
    try:
        shutil.rmtree("imgfacedb")
    except:
        pass
    try:
        shutil.rmtree("facedb")
    except:
        pass
    try:
        db.close()
        os.remove("fullnames.json")
    except:
        pass

def search_fullname(uid):
    res = db.search(que.faceid == uid)
    return res

def save_face(face_embed, faceid):
    with open("facedb/"+str(faceid)+".face", 'wb+') as f:
        pickle.dump(face_embed, f)
        f.close()

    