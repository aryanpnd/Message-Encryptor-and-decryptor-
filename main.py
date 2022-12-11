import tkinter
import customtkinter as ct
from tkinter import filedialog as fd

import fernetEncryptor as FE
import fernetEncryptorGUI as FEG
import fernetDecryptor as FD
import fernetDecryptorGUI as FDG
import os


ct.set_appearance_mode("System") 
ct.set_default_color_theme("blue")  
app = ct.CTk() 
app.title("Fernet Encrypter Decrypter")
app.geometry("250x220")

def Meclose():
    FEG.closeWin()

label = ct.CTkLabel(master=app, text="Message Encrypter and Decrypted \n Using cryptography.fernet")
label.grid(row=0,column = 1, padx=20, pady=10)

MessageEncrypter = ct.CTkButton(master=app, text="Message Encrypter", command=lambda:FEG.fernetMessageEncrypterWindow())
MessageEncrypter.grid(row=1,column = 1, padx=20, pady=20)


MessageDncrypter = ct.CTkButton(master=app,fg_color=("orange"), text="Message Decrypter",command=lambda:FDG.fernetMessageDecrypterWindow())
MessageDncrypter.grid(row=2,column = 1)


Exit = ct.CTkButton(master=app, text="Exit",fg_color=("red"), command=app.destroy)
Exit.grid(row=3,column = 1, padx=20, pady=20)


app.mainloop()