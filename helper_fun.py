from cam_capture import *
from db_queries import *
from face_rec import *
from tkinter import messagebox
import tkinter as tk
from tkinter.filedialog import askopenfilename
# from pages import user_frame
# from login import login_frame
# from register import register_frame


def user_frame(username, destroy_this_win=None, ):
    if destroy_this_win is not None:
        destroy_this_win.destroy()

    empty_temp_folder()
    root = tk.Tk()
    root.title("Safe-Storage:User Page")
    root.geometry("500x700")  # 300x200
    welcome_text = 'Welcome '+username+' !!!'
    welcome_label = tk.Label(root, text=welcome_text, font=20)
    welcome_label.place(x=180, y=5)

    root.mainloop()


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
        messagebox.showinfo('Success',
                            'Registration Successful')
        print('Registration Successful !!!!')

        pass


def login_user(window, username, password, facepic_path):
    if(authenticateUser(username=username, password=password)):
        if(authenticateUserImage(imgPath=facepic_path, username=username)):
            messagebox.showinfo('Success',
                                'Login Successful')
            print('authentication success from DB and FaceRec')
            user_frame(destroy_this_win=window, username=username)
        else:
            messagebox.showerror(
                "Error", "Try again check whether captured image contains correct face")
            print('auth failed from FaceRec')
    else:
        messagebox.showerror(
            "Error", "Try again check username,password")
        print('auth failed from DB')
