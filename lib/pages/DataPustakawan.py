from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from lib.utils.db import menambahkanData, fetch_data, cur, conn
from lib.utils.algoritma import merge_sort, dynamic_binary_search
from lib.components.header import header


def dataPustakawan(Akun):
    
    status = 0

    global selected_data

    selected_data = None
    app = header()
    
    columns = ('#1', '#2', '#3', '#4', '#5', '6')
    tabelAnggota = ttk.Treeview(app, columns=columns, show='headings')
    
    # Creating the sorting buttons
    sortFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    sortFrame.pack(padx=10, pady=10)
    
    sortByNameButton = ctk.CTkButton(sortFrame, text="Sort by Name")
    sortByNameButton.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

    sortByIDButton = ctk.CTkButton(sortFrame, text="Sort by ID")
    sortByIDButton.grid(row=0, column=2, padx=10, pady=5, sticky='ew')
    
    frameSearching = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameSearching.pack(pady=10)

    labelSearching = ctk.CTkLabel(frameSearching, text="Cari ID Anggota :", text_color='Black')
    labelSearching.grid(row=0, column=0, padx=5)

    inputIDAnggota = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputIDAnggota.grid(row=0, column=1, padx=5)
    
    tombolSearching = ctk.CTkButton(frameSearching, text="Cari")
    tombolSearching.grid(row=0, column=2, padx=5)
    
    tabelAnggota.heading('#1', text='ID Anggota')
    tabelAnggota.heading('#2', text='Nama Anggota')
    tabelAnggota.heading('#3', text='Alamat')
    tabelAnggota.heading('#4', text='No. Telepon')
    tabelAnggota.heading('#5', text='Email')
    tabelAnggota.heading('#6', text='Tanggal Lahir')
    
    tabelAnggota.column('#1', width=100)
    tabelAnggota.column('#2', width=200)
    tabelAnggota.column('#3', width=100)
    tabelAnggota.column('#4', width=200)
    tabelAnggota.column('#5', width=100)
    tabelAnggota.column('#6', width=100)
    
    # data = fetch_data("anggota_perpustakaan")
    # update_treeview()
    tabelAnggota.pack(pady=15)
    tabelAnggota.bind('<ButtonRelease-1>')
    
    frame_actions = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_actions.pack()

    button_edit = ctk.CTkButton(frame_actions, text="Edit")
    button_edit.grid(row=0, column=0, padx=10,pady=10)

    button_add = ctk.CTkButton(frame_actions, text="Tambah")
    button_add.grid(row=0, column=1, padx=10, pady=10)

    button_delete = ctk.CTkButton(frame_actions, text="Hapus")
    button_delete.grid(row=0, column=2, padx=10, pady=10)
    
    button_kembali=ctk.CTkButton(frame_actions, text="Kembali")
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)
    
    app.mainloop()
    
    return status
