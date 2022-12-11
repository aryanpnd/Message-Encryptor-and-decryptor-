import tkinter
import customtkinter as ct
from tkinter import filedialog as fd
from tkinter import messagebox
import fernetEncryptor as FE
import os



def fernetMessageEncrypterWindow():

    global closeWin
    def closeWin():
        app.destroy()

    ct.set_appearance_mode("System") 
    ct.set_default_color_theme("blue")  
    app = ct.CTk() 
    app.title("Encrypter")
    app.geometry("440x470")
    MTE = ""


    def GenerateKey():

        keyPath = fd.askdirectory()
        FE.genwrite_key(keyPath)


    def messageEntery():
        global MTE

        dialog = ct.CTkInputDialog(text="Type Your message:", title="Enter Your message")
        messageToEncrypt = dialog.get_input()

        MTE = messageToEncrypt


    def EncryptIt():
        global MTE
        messagebox.showinfo("Browse Key", "Browse to key file and select it")
        keyPath = fd.askopenfile(mode='r', filetypes=[('key File', '*.key')])
        key = keyPath.readlines()
        ecryptMsg = FE.encryptMessage(str(key),MTE)
        NewState = ecryptMsg.decode()
        ecryptMsgEntry.insert(0,NewState)

    def saveIt():
        value1 = ecryptMsgEntry.get()
        path = fd.askdirectory()
        with open(f"{path}\YourEncryptedMessage.txt", "w") as msg:
            msg.write(value1)



    EnterMessageBtn = ct.CTkButton(master=app, text="Enter Message",fg_color=("blue"), command=messageEntery)
    EnterMessageBtn.grid(row=0,column = 1, padx=20, pady=20)


    GenerateKeyBtn = ct.CTkButton(master=app, text="Generate Key",fg_color=("orange"), command=GenerateKey)
    GenerateKeyBtn.grid(row=2,column = 1)

    EncryptButton = ct.CTkButton(master=app, text="Encrypt It", command=EncryptIt)
    EncryptButton.grid(row=3,column = 1, padx=20, pady=20)

    label = ct.CTkLabel(master=app, text="Your Encrypted Message")
    label.grid(row=4,column = 1, padx=20, pady=20)
    ecryptMsgEntry = ct.CTkEntry(master=app,
                                placeholder_text="Your Encrypted Message will be Display here",
                                width=400,
                                height=100,
                                border_width=1,
                                corner_radius=10)
    ecryptMsgEntry.grid(row=5, column=1, padx=20)

    saveButton = ct.CTkButton(master=app, text="Save It",fg_color=("green"), command=saveIt)
    saveButton.grid(row=6,column = 1, padx=20, pady=20)


    ExitButton = ct.CTkButton(master=app, text="Exit",fg_color=("red"), command=closeWin)
    ExitButton.grid(row=7,column = 1, padx=20, pady=20)


    app.mainloop()