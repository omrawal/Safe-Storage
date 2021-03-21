from cam_capture import *
from db_queries import *
from face_rec import *
from tkinter import Message, messagebox
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import ttk
from PIL import ImageTk, Image
# from file_crypto import *
# from pages import login_frame
# from login import login_frame
# from register import register_frame
# from user_frame_fun import user_frame


def nav_to_logout(window):
    empty_decrypted_folder()
    window.destroy()


def encrypt_button_clicked(window, username, filepath):

    # encrypted_dest = encrypt_this_file(filename=filepath, username=username)
    encrypted_dest = addFiles(owner=username, file_name=filepath)
    if(encrypted_dest != False):
        message_text = 'File encrypted and stored at:- '+encrypted_dest
        messagebox.showinfo('Success',
                            message_text)


def decrypt_button_clicked(window, username, filepath):
    # print(filepath)
    # print(filepath.replace('\\', '\\\\'))
    decrypted_dest = decrypt_this_file(
        filename=filepath, username=username)
    if(decrypted_dest != False):
        message_text = 'File decrypted and stored at:- '+decrypted_dest
        messagebox.showinfo('Success',
                            message_text)\



'D: \Code\Git stuff\Safe-Storage\encrypted_files\1811037_Rawal_Om_Utpal_ISE_SLPM_enc.pdf'


def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ('all files', '.*'),
    ]))
    ent.insert(tk.END, filename)  # add this


def user_frame(username, destroy_this_win=None, ):
    if destroy_this_win is not None:
        destroy_this_win.destroy()

    empty_temp_folder()

    root = tk.Tk()
    root.title("Safe-Storage:User Page")
    root.geometry("500x700")  # 300x200
    welcome_text = 'Welcome '+username+' !!!'
    welcome_label = tk.Label(root, text=welcome_text, font=20)
    welcome_label.place(x=20, y=5)

    logout_button = tk.Button(
        root, text="Logout and exit", font=5, command=lambda: nav_to_logout(window=root,))

    logout_button.place(x=250, y=8)

    note_text = 'Note: Files decripted will be deleted\n from location once you logout'
    note_label = tk.Label(root, text=note_text, font=5)
    note_label.place(x=20, y=55)

    profile_pic_path = getProfilePicName(username=username)
    print('profile_pic_path= ', profile_pic_path)
    load = Image.open(profile_pic_path)
    size = 200, 200
    load.thumbnail(size, Image.ANTIALIAS)
    render = ImageTk.PhotoImage(load)
    img = tk.Label(root, image=render)
    img.image = render
    img.config(height=200, width=150)
    img.place(x=150, y=130)
    encrytp_text = 'Encrypt Files:-'
    encrytp_label = tk.Label(root, text=encrytp_text, font=5)
    encrytp_label.place(x=20, y=350)

    encrypt_command_message = tk.Label(
        root, text="Select File:", font=10)
    encrypt_command_message.place(x=10, y=400)

    encrypt_command_entry = tk.Entry(root, font=10)
    encrypt_command_entry.place(x=150, y=400)

    encrypt_command_browse_button = tk.Button(
        root, text="Browse", font=10, command=lambda: browsefunc(encrypt_command_entry))
    encrypt_command_browse_button.place(x=400, y=390)

    encrypt_command_button = tk.Button(
        root, text="Encrypt", font=10, command=lambda: encrypt_button_clicked(window=root,
                                                                              username=username, filepath=encrypt_command_entry.get()
                                                                              ))

    encrypt_command_button.place(x=200, y=450)

    available_file_list = getFilesOfUser(owner=username)

    decrytp_text = 'Decrypt Files:-'
    decrytp_label = tk.Label(root, text=decrytp_text, font=5)
    decrytp_label.place(x=20, y=500)

    decrypt_command_message = tk.Label(
        root, text="Select File:", font=10)
    decrypt_command_message.place(x=10, y=550)

    decrypt_command_entry = ttk.Combobox(
        root, values=available_file_list, state="readonly", width=15)
    decrypt_command_entry.place(x=150, y=550)

    # decrypt_command_browse_button = tk.Button(
    #     root, text="Browse", font=10, command=lambda: browsefunc(decrypt_command_entry))
    # decrypt_command_browse_button.place(x=400, y=340)

    decrypt_command_button = tk.Button(
        root, text="Decrypt", font=10, command=lambda: decrypt_button_clicked(window=root,
                                                                              username=username, filepath=decrypt_command_entry.get()
                                                                              ))

    decrypt_command_button.place(x=200, y=600)

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
