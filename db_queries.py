import sqlite3
import datetime
import hashlib
from file_crypto import *


def generateHash(rawString):
    md51 = hashlib.md5()
    md51.update(rawString.encode('utf-8'))
    hash_1 = md51.hexdigest()
    return hash_1


def getUsers():
    conn = sqlite3.connect('safe_storage.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users(
    username text PRIMARY KEY,
    password TEXT,
    profilepicfilename TEXT,
    privatekey TEXT 
    );''')
    conn.commit()
    cursor = conn.execute(
        "SELECT USERNAME,PASSWORD,PRIVATEKEY,PROFILEPICFILENAME from USERS")
    user_list = []
    for row in cursor:
        user_list.append(row[0])
    conn.close()
    return user_list


def authenticateUser(username, password):

    if(username not in getUsers()):
        return False
    else:
        pass_hash = generateHash(password)
        user_data = getUserData(username)
        true_pass = user_data[1]
        if(true_pass == pass_hash):
            return True
        else:
            return False


def getUserData(username):
    if(username not in getUsers()):
        return False
    else:
        conn = sqlite3.connect('safe_storage.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS users(
            username text PRIMARY KEY,
            password TEXT,
            profilepicfilename TEXT,
            privatekey TEXT 
            );''')
        conn.commit()
        cursor = conn.execute(
            "SELECT USERNAME,PASSWORD,PRIVATEKEY,PROFILEPICFILENAME from USERS")
        userdata = ()
        for row in cursor:
            if(row[0] == username):
                # username,password,privatekey,picname
                userdata = (row[0], row[1], row[2], row[3])
                break
        conn.close()
        return userdata
    #     print("USERNAME = ", row[0])
    #     print("PASSSWORD = ", row[1])
    #     print("PRIVATE_KEY = ", row[2])
    #     print("PROFILE_PIC_FILENAME = ", row[3], "\n")

    # conn.close()


def getPrivateKey(username):
    if(username not in getUsers()):
        return False
    else:
        user_data = getUserData(username)
        return user_data[2]


def getProfilePicName(username):
    if(username not in getUsers()):
        return False
    else:
        user_data = getUserData(username)
        return user_data[3]


def encrypt_this_file(filename, username):
    private_key = getPrivateKey(username=username)
    if(private_key == False):
        return False
    else:
        res = encrypt(filename=filename, key=private_key)
        if(res == False):
            return False
        else:
            return res


def decrypt_this_file(filename, username):
    private_key = getPrivateKey(username=username)
    if(private_key == False):
        return False
    else:
        res = decrypt(filename=filename, key=private_key)
        if(res == False):
            return False
        else:
            return res


def addFiles(owner, file_name):
    if(owner not in getUsers()):
        return False
    else:
        encrypted_filename = encrypt_this_file(
            filename=file_name, username=owner)
        conn = sqlite3.connect('safe_storage.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS files(
            id integer PRIMARY KEY autoincrement,
            owner text,
            filename text,
            dateuploaded timestamp,
            FOREIGN KEY(owner) REFERENCES users(username)
            );''')

        conn.commit()
        conn.execute("INSERT INTO FILES (owner,filename,dateuploaded) \
            VALUES (?,?,?)", (owner, encrypted_filename, datetime.datetime.now()))
        conn.commit()
        conn.close()
        return encrypted_filename


def addUser(username, password, profile_pic_name):
    if(username in getUsers()):
        return False
    else:
        conn = sqlite3.connect('safe_storage.db')
        conn.execute('''CREATE TABLE IF NOT EXISTS users(
        username text PRIMARY KEY,
        password TEXT,
        profilepicfilename TEXT,
        privatekey TEXT 
        );''')
        conn.commit()
        conn.execute("INSERT INTO USERS (USERNAME,PASSWORD,PRIVATEKEY,PROFILEPICFILENAME) \
        VALUES (?,?,?,?)", (username, generateHash(password), generateKey(), profile_pic_name))
        conn.commit()
        conn.close()
        return True


def print_all_users():
    conn = sqlite3.connect('safe_storage.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS users(
        username text PRIMARY KEY,
        password TEXT,
        profilepicfilename TEXT,
        privatekey TEXT 
        );''')
    conn.commit()
    cursor = conn.execute(
        "SELECT USERNAME,PASSWORD,PRIVATEKEY,PROFILEPICFILENAME from USERS")
    for row in cursor:
        print("USERNAME = ", row[0])
        print("PASSSWORD = ", row[1])
        print("PRIVATE_KEY = ", row[2])
        print("PROFILE_PIC_FILENAME = ", row[3], "\n")

    conn.close()


def getFilesOfUser(owner):
    if(owner not in getUsers()):
        # print('false owner not found in all users')
        return False
    else:
        all_files = getAllFiles()
        user_files = []
        for i in all_files:
            if(i[1] == owner):
                user_files.append(i[2])
        if(len(user_files) > 0):
            return user_files
        else:
            return False


def getSpecificFile(owner, filename):
    for i in getFilesOfUser(owner):
        # print(i)
        if i[2] == filename:
            return filename
    # print('false filename not in getFilesOfUser')


def getAllFiles():
    conn = sqlite3.connect('safe_storage.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS files(
    id integer PRIMARY KEY autoincrement,
    owner text,
    filename text,
    dateuploaded timestamp,
    FOREIGN KEY(owner) REFERENCES users(username)
    );''')
    conn.commit()
    files = []
    cursor = conn.execute(
        "SELECT id,owner,filename,dateuploaded from files")
    for row in cursor:
        # print("id = ", row[0])
        # print("owner = ", row[1])
        # print("filename = ", row[2])
        # print("dateuploaded = ", row[3], "\n")
        files.append(row)
    conn.close()
    return files


def print_all_files():
    conn = sqlite3.connect('safe_storage.db')
    conn.execute('''CREATE TABLE IF NOT EXISTS files(
    id integer PRIMARY KEY autoincrement,
    owner text,
    filename text,
    dateuploaded timestamp,
    FOREIGN KEY(owner) REFERENCES users(username)
    );''')

    conn.commit()
    cursor = conn.execute(
        "SELECT id,owner,filename,dateuploaded from files")
    for row in cursor:
        print("id = ", row[0])
        print("owner = ", row[1])
        print("filename = ", row[2])
        print("dateuploaded = ", row[3], "\n")
    conn.close()
