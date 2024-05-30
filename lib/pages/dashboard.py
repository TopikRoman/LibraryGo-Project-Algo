from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from lib.components.header import header


def dashboard(Password) :
    menuTarget = []

    def navigate(Parameter) :
        match Parameter :
            case 1:
                menuTarget.append("Data Buku")
            case 2:
                menuTarget.append("Data Anggota")

        app.destroy()
    
    app = header()
    
    password = str(Password)
    LeftFrame = ctk.CTkFrame(app, width=200, height=550, fg_color="White")
    LeftFrame.grid(row=0, column=0, padx=10, pady=20, sticky='ew')

    RightFrame = ctk.CTkFrame(app, width=650, height=550, fg_color="White")
    RightFrame.grid(row=0, column=1, padx=10, pady=20)

    image = Image.open("Logo.png")
    logo = ImageTk.PhotoImage(image)

    logo_label = ctk.CTkLabel(LeftFrame, image=logo, bg_color='#FAFAFA')
    logo_label.image = logo 
    logo_label.grid(row=0, column=0, pady=20)
    DataBuku = ctk.CTkButton(LeftFrame, text="Data Buku", width=180, text_color='Black', command=lambda: navigate(1))
    DataBuku.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    DataPeminjaman = ctk.CTkButton(LeftFrame, text="Data Peminjaman", width=180, text_color='Black')
    DataPeminjaman.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    if len(password) > 6:

        DataAnggota = ctk.CTkButton(LeftFrame, text="Data Anggota", width=180, text_color='Black', command=lambda: navigate(2))
        DataAnggota.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        DataPustakawan = ctk.CTkButton(LeftFrame, text="Data Pustakawan", width=180, text_color='Black')
        DataPustakawan.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

        DataDenda = ctk.CTkButton(LeftFrame, text="Data Denda", width=180, text_color='Black')
        DataDenda.grid(row=5, column=0, padx=10, pady=(10,180), sticky="ew")

        LogOut = ctk.CTkButton(LeftFrame, text="Log Out", width=180, text_color='Black')
        LogOut.grid(row=6, column=0, padx=10, pady=10, sticky="ew")
        
    else: 
        
        DataAnggota = ctk.CTkButton(LeftFrame, text="Data Anggota", width=180, text_color='Black', command=lambda: navigate(2))
        DataAnggota.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        DataDenda = ctk.CTkButton(LeftFrame, text="Data Denda", width=180, text_color='Black')
        DataDenda.grid(row=5, column=0, padx=10, pady=(10,225), sticky="ew")

        LogOut = ctk.CTkButton(LeftFrame, text="Log Out", width=180, text_color='Black')
        LogOut.grid(row=6, column=0, padx=10, pady=10, sticky="ew")

    app.mainloop()

    return menuTarget
