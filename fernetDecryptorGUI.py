import tkinter
import customtkinter as ct
from tkinter import filedialog as fd
import fernetDecryptor as FDE
from tkinter import messagebox
import os



def fernetMessageDecrypterWindow():

    global closeWin
    def closeWin():
        app.destroy()

    ct.set_appearance_mode("System") 
    ct.set_default_color_theme("blue")  
    app = ct.CTk() 
    app.title("Decrypter")
    app.geometry("440x470")

    MessageToDE = ""
    DecryptKey = ""
    


    def BrowseEncryptFile():
        messagebox.showinfo("Browse Message File", "Browse to the Encrypted Message file and select it to Decrypt it")
        global MessageToDE
        msgPath = fd.askopenfile(mode='r', filetypes=[('Encrypt Message File', '*.txt')])
        msg = msgPath.readlines()
        MessageToDE = str(msg)

    def GetKey():
        global DecryptKey
        keyPath = fd.askopenfile(mode='r', filetypes=[('Key File', '*.key')])
        key = keyPath.readlines()
        DecryptKey = str(key)

        
    def DecryptIt():
        global MessageToDE, DecryptKey
        NewState = FDE.MessageDecryption(DecryptKey,MessageToDE)
        DecryptMsgEntry.insert(0,NewState)

    def saveIt():
        value1 = DecryptMsgEntry.get()
        path = fd.askdirectory()
        with open(f"{path}\YourDecryptedMessage.txt", "w") as msg:
            msg.write(value1)


    EnterMessageBtn = ct.CTkButton(master=app, text="Browse Encrypted File",fg_color=("blue"), command=BrowseEncryptFile)
    EnterMessageBtn.grid(row=0,column = 1, padx=20, pady=20)


    GenerateDKeyBtn = ct.CTkButton(master=app, text="Browse Key",fg_color=("orange"),command=GetKey)
    GenerateDKeyBtn.grid(row=2,column = 1)

    DecryptButton = ct.CTkButton(master=app, text="Decrypt It",command=DecryptIt)
    DecryptButton.grid(row=3,column = 1, padx=20, pady=20)

    label = ct.CTkLabel(master=app, text="Your Decrypted Message")
    label.grid(row=4,column = 1, padx=20, pady=20)
    DecryptMsgEntry = ct.CTkEntry(master=app,
                                placeholder_text="Your Encrypted Message will be Display here",
                                width=400,
                                height=100,
                                border_width=1,
                                corner_radius=10)
    DecryptMsgEntry.grid(row=5, column=1, padx=20)

    saveButton = ct.CTkButton(master=app, text="Save It",fg_color=("green"), command=saveIt)
    saveButton.grid(row=6,column = 1, padx=20, pady=20)


    ExitButton = ct.CTkButton(master=app, text="Exit",fg_color=("red"), command=closeWin)
    ExitButton.grid(row=7,column = 1, padx=20, pady=20)


    app.mainloop()

