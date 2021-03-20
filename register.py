from cam_capture import *
from helper_fun import *
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os


empty_temp_folder()
root = tk.Tk()
root.title("Safe-Storage:Register")
root.geometry("500x700")  # 300x200

uname_label = tk.Label(root, text="Username:", font=10)
uname_label.place(x=10, y=100)

uname_entry = tk.Entry(root, font=10)
uname_entry.place(x=150, y=100)

passwd_label = tk.Label(root, text="Password (4 char):", font=10)
passwd_label.place(x=10, y=150)

passwd_entry = tk.Entry(root, show="*", font=10)
passwd_entry.place(x=200, y=150)


profilepic_message = tk.Label(root, text="Profile Pic:", font=10)
profilepic_message.place(x=10, y=200)

profilepic_entry = tk.Entry(root, font=10)
profilepic_entry.place(x=150, y=200)

profilepic_browse_button = tk.Button(
    root, text="Browse", font=10, command=lambda: browsefunc(profilepic_entry))
profilepic_browse_button.place(x=400, y=190)


def browsefunc(ent):
    filename = askopenfilename(filetypes=([
        ("image", ".jpeg"),
        ("image", ".png"),
        ("image", ".jpg"),
    ]))
    ent.insert(tk.END, filename)  # add this


def captureFace(ent):
    filename = os.getcwd()+'\\temp\\test_img.png'
    # messagebox.showinfo(
    #     'SUCCESS!!!', 'Press Space Bar to click picture and ESC to exit')
    res = None
    res = messagebox.askquestion(
        'Click Picture', 'Press Space Bar to click picture and ESC to exit')
    if res == 'yes':
        capture_image_from_cam_into_temp()
        ent.insert(tk.END, filename)
    return True


facepic_message = tk.Label(root, text="Face Pic:", font=10)
facepic_message.place(x=10, y=250)

facepic_entry = tk.Entry(root, font=10)
facepic_entry.place(x=150, y=250)

facepic_browse_button = tk.Button(
    root, text="Capture", font=10, command=lambda: captureFace(facepic_entry))
facepic_browse_button.place(x=400, y=240)

register_button = tk.Button(
    root, text="register", font=10, command=lambda: register_user(window=root,
                                                                  username=uname_entry.get(),
                                                                  facepic_path=facepic_entry.get(),
                                                                  password=passwd_entry.get(),
                                                                  propic_path=profilepic_entry.get()))

register_button.place(x=200, y=320)

root.mainloop()
