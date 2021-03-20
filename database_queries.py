import sqlite3
import datetime

conn = sqlite3.connect('safe_storage.db')
print("Opened database successfully")
conn.execute('''CREATE TABLE IF NOT EXISTS users(
    username text PRIMARY KEY,
    password TEXT,
    profilepicfilename TEXT,
    privatekey TEXT 
    );''')
conn.commit()
conn.execute("INSERT INTO USERS (USERNAME,PASSWORD,PRIVATEKEY,PROFILEPICFILENAME) \
      VALUES ('om_rawal', '123456', '13854165', 'Texas')")

conn.execute("INSERT INTO USERS (USERNAME,PASSWORD,PRIVATEKEY,PROFILEPICFILENAME) \
      VALUES (?,?,?,?)", ('om_rawal', '123456', '13854165', 'Texas'))

conn.commit()

cursor = conn.execute(
    "SELECT USERNAME,PASSWORD,PRIVATEKEY,PROFILEPICFILENAME from USERS")

for row in cursor:
    print("USERNAME = ", row[0])
    print("PASSSWORD = ", row[1])
    print("PRIVATE_KEY = ", row[2])
    print("PROFILE_PIC_FILENAME = ", row[3], "\n")

conn.execute('''CREATE TABLE IF NOT EXISTS files(
    id integer PRIMARY KEY autoincrement,
    owner text,
    filename text,
    dateuploaded timestamp,
    FOREIGN KEY(owner) REFERENCES users(username)
    );''')
conn.commit()
conn.execute("INSERT INTO FILES (owner,filename,dateuploaded) \
      VALUES (?,?,?)", ('om_rawal', 'hello.txt', datetime.datetime.now()))
conn.commit()
cursor = conn.execute(
    "SELECT id,owner,filename,dateuploaded from files")

for row in cursor:
    print("id = ", row[0])
    print("owner = ", row[1])
    print("filename = ", row[2])
    print("dateuploaded = ", row[3], "\n")


# print(cursor)
conn.close()
