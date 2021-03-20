from cam_capture import *
from db_queries import *
from face_rec import *


def register_user(window, username, password, propic_path, facepic_path):
    print('username=', username)
    print('password=', password)
    print('propic_path=', propic_path)
    print('facepic_path=', facepic_path)
    print('-----------------')
    propic_loc = save_profile_pic(propic_path)
    addUser(username=username, password=password, profile_pic_name=propic_loc)
    save_user(imgPath=facepic_path, username=username)
    print_all_users()
    pass
