from tkinter import *
import customtkinter as ctk
from lib.components.header import header


def dashboard() :
    menuTarget = []

    def navigate() :

        menuTarget.append("Data Peminjaman")

        app.destroy()
    
    app = header()

    MainMenuFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
    MainMenuFrame.pack(padx=10, pady=100)

    MainMenuFrame.grid_columnconfigure(0, weight=1)
    MainMenuFrame.grid_columnconfigure(1, weight=1)
    MainMenuFrame.grid_columnconfigure(2, weight=1)

    AturBuku = ctk.CTkButton(MainMenuFrame, text="Atur Buku", fg_color='#2DE053', text_color='Black')
    AturBuku.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    LihatPeminjaman = ctk.CTkButton(MainMenuFrame, text="Lihat Peminjaman", fg_color='#2DE053', text_color='Black')
    LihatPeminjaman.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    DataPeminjaman = ctk.CTkButton(MainMenuFrame, text="Data Peminjaman", fg_color='#2DE053', text_color='Black', command=navigate)
    DataPeminjaman.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

    app.mainloop()

    return menuTarget
