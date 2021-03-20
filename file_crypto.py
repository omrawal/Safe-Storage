from cryptography.fernet import Fernet
import os


def generateKey():  # generates a key  store in DB caution is object of bytes type NOT string
    key = Fernet.generate_key()
    return key


def encrypt(filename, key):  # encrypts a file and stores (filename) "+_enc" (.ext)
    fernet_obj = Fernet(key)
    fname = filename.replace('/', '\\')
    with open(fname, 'rb') as original_file:
        original = original_file.read()

    encrypted = fernet_obj.encrypt(original)
    newFilename = fname.split('.')
    newFileName = '_enc.'.join(newFilename)
    # print(newFileName)
    only_file_name = (newFileName.split('\\')[-1])
    if(not os.path.exists('encrypted_files')):
        os.umask(0)
        os.mkdir(os.getcwd()+'\\'+'encrypted_files', mode=0o777)
    filePath = 'encrypted_files'+'\\'+only_file_name
    with open(filePath, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)
    return filePath


def decrypt(filename, key):  # decrypts a file and stores (filename) "+_dec" (.ext)
    fernet_obj = Fernet(key)
    fname = filename.replace('/', '\\')
    with open(fname, 'rb') as encrypted_file:
        encrypted = encrypted_file.read()
    decrypted = fernet_obj.decrypt(encrypted)
    newFilename = fname.split('_enc.')
    newFileName = '_dec.'.join(newFilename)
    only_file_name = (newFileName.split('\\')[-1])
    if(not os.path.exists('decrypted_files')):
        os.umask(0)
        os.mkdir(os.getcwd()+'\\'+'decrypted_files', mode=0o777)
    filePath = 'decrypted_files'+'\\'+only_file_name
    # print(newFileName)
    with open(filePath, 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    return filePath

# Example


# print(encrypt('1.txt', b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM='))
# print(encrypt('D:\Code\Git stuff\Safe-Storage\profile_pics\Mypic_feb.jpg',
#               b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM='))

# decrypt('1_enc.txt',b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM=')
# print(decrypt('D:\Code\Git stuff\Safe-Storage\encrypted_files\Mypic_feb_enc.jpg',
#               b'NtEvVBWbzSEBu6axGA21Aw6pt3MsO1zFM_mCu9Al8oM='))
