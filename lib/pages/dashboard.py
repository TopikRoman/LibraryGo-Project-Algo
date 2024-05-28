from tkinter import *
import customtkinter as ctk
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

    if len(password) > 6:
        MainMenuFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
        MainMenuFrame.pack(padx=10, pady=100)

        MainMenuFrame.grid_columnconfigure(0, weight=1)
        MainMenuFrame.grid_columnconfigure(1, weight=1)
        MainMenuFrame.grid_columnconfigure(2, weight=1)

        DataBuku = ctk.CTkButton(MainMenuFrame, text="Data Buku", fg_color='#2DE053', text_color='Black', command=lambda: navigate(1))
        DataBuku.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        DataPeminjaman = ctk.CTkButton(MainMenuFrame, text="Lihat Peminjaman", fg_color='#2DE053', text_color='Black')
        DataPeminjaman.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

        DataAnggota = ctk.CTkButton(MainMenuFrame, text="Data Peminjaman", fg_color='#2DE053', text_color='Black')
        DataAnggota.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        
        DataPustakawan = ctk.CTkButton(MainMenuFrame, text="Data Anggota", fg_color='#2DE053', text_color='Black', command=lambda: navigate(2))
        DataPustakawan.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        DataDenda = ctk.CTkButton(MainMenuFrame, text="Data Denda", fg_color='#2DE053', text_color='Black')
        DataDenda.grid(row=1, column=2, padx=10, pady=10, sticky="ew")
        
        LogOut = ctk.CTkButton(MainMenuFrame, text="Log Out", fg_color='#2DE053', text_color='Black')
        LogOut.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        Exit = ctk.CTkButton(MainMenuFrame, text="Exit", fg_color='#2DE053', text_color='Black')
        Exit.grid(row=2, column=1, padx=10, pady=10, sticky="ew")
    else: 
        MainMenuFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
        MainMenuFrame.pack(padx=10, pady=100)

        MainMenuFrame.grid_columnconfigure(0, weight=1)
        MainMenuFrame.grid_columnconfigure(1, weight=1)
        MainMenuFrame.grid_columnconfigure(2, weight=1)

        DataBuku = ctk.CTkButton(MainMenuFrame, text="Data Buku", fg_color='#2DE053', text_color='Black', command=lambda: navigate(1))
        DataBuku.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

        DataPeminjaman = ctk.CTkButton(MainMenuFrame, text="Lihat Peminjaman", fg_color='#2DE053', text_color='Black')
        DataPeminjaman.grid(row=0, column=1, padx=10, pady=10, sticky="ew")
                
        DataDenda = ctk.CTkButton(MainMenuFrame, text="Data Denda", fg_color='#2DE053', text_color='Black')
        DataDenda.grid(row=0, column=2, padx=10, pady=10, sticky="ew")
        
        LogOut = ctk.CTkButton(MainMenuFrame, text="Log Out", fg_color='#2DE053', text_color='Black')
        LogOut.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
        
        Exit = ctk.CTkButton(MainMenuFrame, text="Exit", fg_color='#2DE053', text_color='Black')
        Exit.grid(row=1, column=2, padx=10, pady=10, sticky="ew")

    app.mainloop()

    return menuTarget
