# Safe-Storage
Drive To store Files

This Desktop application helps users save files in encrypted format at their local storage. The authentication is 2-step. First is authentication by username and password from the SQLite database. The password stored in the database is hashed using MD5 Hash. The second is Face Recognition. If both the authentication are successful then the user is taken to the operations page where encryption and decryption can be performed. The encryption-decryption is performed using the user's unique key which makes it impossible to decrypt the encrypted files by any other means as the users' unique key is not revealed to even the user. Once the user logs out or closes the application all the files decrypted during that session are deleted for added security.



## Prerequisites
1. Python >=3.6

## Other Requirements
For Windows users cmake should be installed from Visual Studio Installer for `face_recognition` module to work.

## Run
`pip install requirements.txt`



## Preview
![Preview](Assets/Safe_storage_for_gif.gif)

## Please open an issue if
* you have any suggestion to improve this project
* you noticed any problem or error
## Also view  `Web Application` of this Desktop App [Secure-Drive](https://github.com/omrawal/Secure-Drive)
