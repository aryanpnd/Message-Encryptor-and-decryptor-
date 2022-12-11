from cryptography.fernet import Fernet

def MessageDecryption(key,message):
    b = Fernet(key)
    decoded_slogan = b.decrypt(str(message))
    return decoded_slogan.decode()