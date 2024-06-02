from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from lib.components.header import header
from lib.components.input import input
from lib.utils.db import loginQuery



def loginPage() :
    status = 0
    akun = []

    app = header()


    def login() :
        nonlocal status
        status = 1

        Usn = username.get()
        Pwd = password.get()
        
        if Usn == 'Admin' and Pwd == 'Admin' :
            print("Login Berhasil")
            app.destroy()
            akun.append(Usn)
            akun.append(Pwd)
            return

        result = loginQuery(Usn, Pwd)

        if type(result) == tuple :
            akun.append(result)
            app.destroy()

            return
        
        messagebox.showinfo(title='Login gagal', message=f"{result}")


    LoginFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
    LoginFrame.pack(padx=10, pady=100, anchor="center")

    loginLabel = ctk.CTkLabel(LoginFrame, text="Login", font=("Gill Sans Ultra Bold Condensed", 40), text_color="#22437B")
    loginLabel.pack(padx=10, pady=10)

    usernameFrame = ctk.CTkFrame(LoginFrame, fg_color='transparent', )
    usernameFrame.pack(padx=0, pady=10, anchor="center")
    
    username_label = ctk.CTkLabel(usernameFrame, text="Username:", text_color='Black')
    username_label.pack(padx=0, pady=0)

    username = ctk.CTkEntry(usernameFrame, fg_color='#FAFAFA', text_color='Black', width=200)
    username.pack(padx=5, pady=0)
    username.bind("<Return>", lambda event: login())
    
    passwordFrame = ctk.CTkFrame(LoginFrame, fg_color='transparent', )
    passwordFrame.pack(padx=0, pady=10, anchor="center")

    password_label = ctk.CTkLabel(passwordFrame, text="Password:", text_color='Black')
    password_label.pack(padx=0, pady=0)

    password = ctk.CTkEntry(passwordFrame, fg_color='#FAFAFA', text_color='Black', width=200)
    password.pack(padx=10, pady=0)
    password.bind("<Return>", lambda event: login())
    loginButton = ctk.CTkButton(LoginFrame, text="Login", fg_color='#22437B', text_color='Black', command=login)
    loginButton.pack(padx=10, pady=20)
    LoginFrame.bind("<Return>", lambda event: login())

    app.mainloop()

    return status, akun
