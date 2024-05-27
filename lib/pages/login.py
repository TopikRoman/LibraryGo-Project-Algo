from tkinter import *
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

        result = loginQuery(Usn, Pwd)

        if type(result) == 'tuple' :
            return
        
        # Message Box disini

        # if Usn == 'Admin' and Pwd == 'Admin' :
        #     print("Login Berhasil")
        #     # print(akun)
        #     app.destroy()
        #     akun.append(Usn)
        #     akun.append(Pwd)
            
        #     # mainmenu()
        # else :
        #     print("Login Gagal")
    
            
    # def mainmenu():
    #     MainMenuFrame.pack(fill="both", expand=True)
    #     LoginFrame.pack_forget()
        


    LoginFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
    LoginFrame.pack(padx=10, pady=100, anchor="center")

    loginLabel = ctk.CTkLabel(LoginFrame, text="Login", font=("Helvetica", 24), text_color="Black")
    loginLabel.pack(padx=10, pady=10)

    username = input(LoginFrame, "Username")

    password = input(LoginFrame, "Password")

    loginButton = ctk.CTkButton(LoginFrame, text="Login", fg_color='#2DE053', text_color='Black', command=login)
    loginButton.pack(padx=10, pady=10)

    
    app.mainloop()

    return akun
