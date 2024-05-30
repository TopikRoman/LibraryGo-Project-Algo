from tkinter import *
from tkinter import messagebox
import customtkinter as ctk

from lib.components.header import header
from lib.components.input import input
from lib.utils.db import loginQuery
# from lib.pages.tambahBuku import tambahDataBuku



def loginPage() :
    akun = []

    # app = Tk()
    # app.geometry('720x420')
    # app.title("Login")

    app = header()


    def login() :

        Usn = username.get()
        Pwd = password.get()

        # print(type(Pwd))
        
        if Usn == 'Admin' and Pwd == 'Admin' :
            print("Login Berhasil")
            # print(akun)
            app.destroy()
            akun.append(Usn)
            akun.append(Pwd)
            return

        result = loginQuery(Usn, Pwd)

        # print(type(result))

        if type(result) == tuple :
            akun.append(result)
            # akun.append('')
            app.destroy()

            return
        
        # Message Box disini
        messagebox.showinfo(title='Login gagal', message=f"{result}")

    
            
    # def mainmenu():
    #     MainMenuFrame.pack(fill="both", expand=True)
    #     LoginFrame.pack_forget()
        


    LoginFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
    LoginFrame.pack(padx=10, pady=100, anchor="center")

    loginLabel = ctk.CTkLabel(LoginFrame, text="Login", font=("Helvetica", 24), text_color="Black")
    loginLabel.pack(padx=10, pady=10)

    # username = input(LoginFrame, "Username")

    # password = input(LoginFrame, "Password")

    username_label = ctk.CTkLabel(LoginFrame, text="Masukkan Username:", text_color='Black')
    username_label.pack(padx=10, pady=1)

    username = ctk.CTkEntry(LoginFrame, fg_color='#FAFAFA', text_color='Black', width=200)
    username.pack(padx=5, pady=10)
    username.bind("<Return>", lambda event: login())

    password_label = ctk.CTkLabel(LoginFrame, text="Masukkan Password:", text_color='Black')
    password_label.pack(padx=5, pady=1)

    password = ctk.CTkEntry(LoginFrame, fg_color='#FAFAFA', text_color='Black', width=200)
    password.pack(padx=10, pady=10)
    password.bind("<Return>", lambda event: login())
    loginButton = ctk.CTkButton(LoginFrame, text="Login", fg_color='#2DE053', text_color='Black', command=login)
    loginButton.pack(padx=10, pady=10)
    LoginFrame.bind("<Return>", lambda event: login())

    
    app.mainloop()

    return akun
