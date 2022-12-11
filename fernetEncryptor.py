from cryptography.fernet import Fernet


def genwrite_key(path):
    key = Fernet.generate_key()
    with open(f"{path}\pass.key", "wb") as key_file:
        key_file.write(key)


def encryptMessage(key,message):
    
    slogan = f"{message}".encode()
    a = Fernet(key)
    coded_slogan = a.encrypt(slogan)
    return coded_slogan


