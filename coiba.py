from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from lib.utils.db import menambahkanData, fetch_data, cur, conn, readAnggota, membacaPeminjaman
from lib.utils.algoritma import merge_sort, dynamic_binary_search
from lib.components.header import header
import string, random
from tkinter import *
from customtkinter import CTk, set_default_color_theme


def header():
    app = Tk()
    app.geometry('900x600')
    app.title("Library Go")
        
    # Create and place the main label
    main_label = ctk.CTkLabel(app, text="Menambah data peminjaman", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
    main_label.pack(pady=20)
    
    # Create a frame to hold the form elements
    form_frame = ctk.CTkFrame(app, fg_color='white')
    form_frame.pack(pady=10)
    
    # Nama label and entry
    nama_label = ctk.CTkLabel(form_frame, text="Nama:", text_color="Black")
    nama_label.grid(row=0, column=0, padx=10, pady=10, sticky=E)
    
    nama_entry = ctk.CTkEntry(form_frame, width=250, fg_color='#FAFAFA', text_color='Black')
    nama_entry.grid(row=0, column=1, padx=10, pady=10)
    
    # Pilih button
    pilih_button = ctk.CTkButton(form_frame, text="Pilih", text_color="Black")
    pilih_button.grid(row=0, column=2, padx=10, pady=10)
    
    buku_label = ctk.CTkLabel(form_frame, text="Judul Buku:", text_color="Black")
    buku_label.grid(row=1, column=0, padx=10, pady=10, sticky=E)
    
        # Creating the table using Treeview widget
    table = ttk.Treeview(form_frame, columns=('Column1', 'Column2'), show='headings', height=5)
    table.heading('Column1', text='ID Buku')
    table.heading('Column2', text='Judul Buku')
    table.column('Column1', width=40)
    table.column('Column2', width=125)
    table.grid(row=1, column=1, padx=10, pady=10, sticky='nsew')
    
    frame_button = ctk.CTkFrame(form_frame, fg_color='white')
    frame_button.grid(row=1, column=2, padx=10, pady=10)
    
    tambah_button = ctk.CTkButton(frame_button, text="Tambah", text_color="Black")
    tambah_button.grid(row=0, column=0, padx=10, pady=10)
    
    hapus_button = ctk.CTkButton(frame_button, text="Hapus", text_color="Black")
    hapus_button.grid(row=1, column=0, padx=10, pady=10)
    
    frame_tombol = ctk.CTkFrame(app, fg_color='white')
    frame_tombol.pack(pady=10)
    
    submitData = ctk.CTkButton(frame_tombol, text="Submit")
    submitData.grid(row=0, column=0, padx=10, pady=10)
    
    Keluar = ctk.CTkButton(frame_tombol, text="Kembali")
    Keluar.grid(row=0, column=1, padx=10, pady=10)

    
    return app

# Run the application
app = header()
app.mainloop()

