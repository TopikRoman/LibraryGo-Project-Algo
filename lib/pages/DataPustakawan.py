from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from lib.utils.db import menambahkanData, fetch_data, cur, conn
from lib.utils.algoritma import merge_sort, dynamic_binary_search
from lib.components.header import header


def DataPustakawan():
    status = 0

    global selected_data
    
    def back() :
        nonlocal status
        status = 1
        
        app.destroy()
        # app.destroy()

    def on_item_selected(event):
        global selected_data
        selected_item = tabelPustakawan.selection()[0]
        selected_data = tabelPustakawan.item(selected_item, 'values')
            
    def update_treeview():
        for item in tabelPustakawan.get_children():
            tabelPustakawan.delete(item)
        for row in fetch_data("pustakawan"):
            tabelPustakawan.insert('', ctk.END, values=row)
            
    selected_data = None
    app = header()

    columns = ('#1', '#2', '#3', '#4', '#5', '#6')
    tabelPustakawan = ttk.Treeview(app, columns=columns, show='headings')

    # Tentukan heading
    tabelPustakawan.heading('#1', text='NIP')
    tabelPustakawan.heading('#2', text='Nama')
    tabelPustakawan.heading('#3', text='Alamat')
    tabelPustakawan.heading('#4', text='No Telepon')
    tabelPustakawan.heading('#5', text='Email')
    tabelPustakawan.heading('#6', text='Tanggal Lahir')

    # Tentukan ukuran kolom
    tabelPustakawan.column('#1', width=100)
    tabelPustakawan.column('#2', width=200)
    tabelPustakawan.column('#3', width=200)
    tabelPustakawan.column('#4', width=100)
    tabelPustakawan.column('#5', width=200)
    tabelPustakawan.column('#6', width=100)

    data = fetch_data("pustakawan")
    update_treeview()

    frameTombolSorting = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameTombolSorting.pack(pady=10)

    tombolPerintah = ctk.CTkFrame(app, fg_color='#FAFAFA')
    tombolPerintah.pack()

    button_kembali=ctk.CTkButton(tombolPerintah, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)

    app = header()

    app.mainloop()
