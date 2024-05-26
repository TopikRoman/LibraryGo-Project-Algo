from tkinter import *
import customtkinter as ctk

def input(parent, placeholder) :
    input = ctk.CTkEntry(parent, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text=f"Masukkan {placeholder}")
    input.pack(padx=10, pady=10)

    return input


def loginPage() :
    app = Tk()
    app.geometry('720x420')
    app.title("Login")


    def login() :
        Usn = username.get()
        Pwd = password.get()
        if Usn == 'Admin' and Pwd == 'Admin' :
            print("Login Berhasil")
            mainmenu()
        else :
            print("Login Gagal")
    
            
    def mainmenu():
        MainMenuFrame.pack(fill="both", expand=True)
        LoginFrame.pack_forget()
        


    LoginFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
    LoginFrame.pack(padx=10, pady=100, anchor="center")

    loginLabel = ctk.CTkLabel(LoginFrame, text="Login", font=("Helvetica", 24), text_color="Black")
    loginLabel.pack(padx=10, pady=10)

    # username = ctk.CTkEntry(LoginFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Username")
    # username.pack(padx=10, pady=10)

    username = input(LoginFrame, "Username")

    password = input(LoginFrame, "Password")

    loginButton = ctk.CTkButton(LoginFrame, text="Login", fg_color='#2DE053', text_color='Black', command=login)
    loginButton.pack(padx=10, pady=10)

    MainMenuFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
    MainMenuFrame.pack(padx=10, pady=100)

    MainMenuFrame.grid_columnconfigure(0, weight=1)
    MainMenuFrame.grid_columnconfigure(1, weight=1)
    MainMenuFrame.grid_columnconfigure(2, weight=1)

    AturBuku = ctk.CTkButton(MainMenuFrame, text="Atur Buku", fg_color='#2DE053', text_color='Black')
    AturBuku.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    LihatPeminjaman = ctk.CTkButton(MainMenuFrame, text="Lihat Peminjaman", fg_color='#2DE053', text_color='Black')
    LihatPeminjaman.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    DataPeminjaman = ctk.CTkButton(MainMenuFrame, text="Data Peminjaman", fg_color='#2DE053', text_color='Black')
    DataPeminjaman.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    app.mainloop()