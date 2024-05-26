from tkinter import *
import customtkinter as ctk


def dashboard() :
    app = Tk()
    app.geometry('720x420')
    app.title("Login")

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