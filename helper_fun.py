from cam_capture import *
from db_queries import *
from face_rec import *
from tkinter import messagebox
# from login import login_frame
# from register import register_frame


def register_user(window, username, password, propic_path, facepic_path):
    print('username=', username)
    print('password=', password)
    print('propic_path=', propic_path)
    print('facepic_path=', facepic_path)
    print('-----------------')
    propic_loc = save_profile_pic(propic_path)
    k = addUser(username=username, password=password,
                profile_pic_name=propic_loc)
    k1 = save_user(imgPath=facepic_path, username=username)
    if(k == False or k1 == False):
        messagebox.showerror("Error", "try again Unique username required")
    # print_all_users()
    else:
        print('Registration Successful !!!!')
        pass


def login_user(window, username, password, facepic_path):
    if(authenticateUser(username=username, password=password)):
        if(authenticateUserImage(imgPath=facepic_path, username=username)):
            print('authentication success from DB and FaceRec')
        else:
            print('auth failed from FaceRec')
    else:
        print('auth failed from DB')
