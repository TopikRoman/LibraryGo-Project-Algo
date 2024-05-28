from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from lib.components.header import header

def MenambahData():
    AllFrame.destroy()
    
    ctk.CTkLabel(app, text="Edit Data Buku", text_color="Black").pack(padx=25, pady=15)

    frameEdit = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    frameEdit.pack(padx=10, pady=10)
    
    ctk.CTkLabel(frameEdit, text="Judul Buku", text_color='Black').pack(padx=0, pady=0)
    entry_judul = ctk.CTkEntry(frameEdit, width=250, fg_color='#FAFAFA', text_color='Black')
    entry_judul.pack(padx=5, pady=5)
    entry_judul.insert(0, selected_data[1])

    ctk.CTkLabel(frameEdit, text="Tahun Terbit", text_color='Black').pack(padx=0, pady=0)
    entry_tahun = ctk.CTkEntry(frameEdit, width=250, fg_color='#FAFAFA', text_color='Black')
    entry_tahun.pack(padx=5, pady=5)
    entry_tahun.insert(0, selected_data[2])

    ctk.CTkLabel(frameEdit, text="Penerbit", text_color='Black').pack(padx=0, pady=0)
    entry_penerbit = ctk.CTkEntry(frameEdit, width=250, fg_color='#FAFAFA', text_color='Black')
    entry_penerbit.pack(padx=5, pady=5)
    entry_penerbit.insert(0, selected_data[3])
    
    genre = pilih_genre(selected_data[4], '1')
    
    ctk.CTkLabel(frameEdit, text="Genre", text_color='Black').pack(padx=5, pady=0)
    entry_genre = ctk.CTkComboBox(frameEdit, width=250, fg_color='#FAFAFA', text_color='Black', values=["Fiksi", "Non-Fiksi", "Sains", "Biografi", "Sejarah"], corner_radius=50)
    entry_genre.pack(padx=10, pady=10)
    entry_genre.set(genre)

    submit_button = ctk.CTkButton(app, text="Submit", command=save_edit)
    submit_button.pack(padx=5, pady=5)

def DataBuku():
    
    app = header()
    
    def MenambahData():
        AllFrame.destroy()
        
        tambahDatabukuLabel = ctk.CTkLabel(app, text="LiGO", font=("Helvetica", 45), text_color="Black")
        tambahDatabukuLabel.pack(padx=50, pady=25)

        # Creating the frame
        tambahDatabukuFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        tambahDatabukuFrame.pack(padx=10, pady=10)

        # Creating the label
        judulBuku = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Judulnya")
        judulBuku.pack(padx=10, pady=10)

        # Creating entry
        tahunPenerbit = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan tahun penerbit")
        tahunPenerbit.pack(padx=10, pady=1)

        Penerbit = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Penerbitnya")
        Penerbit.pack(padx=10, pady=10)

        genreBuku = ctk.CTkComboBox(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', values=["Fiksi", "Non-Fiksi", "Sains", "Biografi", "Sejarah"], corner_radius=50)
        genreBuku.pack(padx=10, pady=10)

        submitData = ctk.CTkButton(tambahDatabukuFrame, text="Submit", fg_color='#FF3399', text_color='Black', corner_radius=50)
        submitData.pack(padx=10, pady=10)
        
        Keluar = ctk.CTkButton(tambahDatabukuFrame, text="Kembali", fg_color='#FF3399', text_color='Black', corner_radius=50)
        Keluar.pack(padx=10, pady=10)
        
    AllFrame = ctk.CTkFrame(app, fg_color='#FAFAFA')
    AllFrame.pack(pady=10)

    columns = ('#1', '#2', '#3', '#4', '#5')
    tree = ttk.Treeview(AllFrame, columns=columns, show='headings')

    # Tentukan heading
    tree.heading('#1', text='ID Buku')
    tree.heading('#2', text='Judul Buku')
    tree.heading('#3', text='Tahun Terbit')
    tree.heading('#4', text='Penerbit')
    tree.heading('#5', text='ID Genre')

    # Tentukan ukuran kolom
    tree.column('#1', width=50)
    tree.column('#2', width=200)
    tree.column('#3', width=100)
    tree.column('#4', width=200)
    tree.column('#5', width=100)

    # Tempatkan frame untuk tombol-tombol sorting dan pencarian

    frame_buttons = ctk.CTkFrame(AllFrame, fg_color='#FAFAFA')
    frame_buttons.pack(pady=10)

    # Tambahkan tombol untuk mengurutkan data
    button_sort_judul = ctk.CTkButton(frame_buttons, text="Sortir berdasarkan Judul", command=lambda: sort_and_display(1))
    button_sort_judul.grid(row=0, column=0, padx=5)

    button_sort_tahun = ctk.CTkButton(frame_buttons, text="Sortir berdasarkan Tahun Terbit", command=lambda: sort_and_display(2, 1))
    button_sort_tahun.grid(row=0, column=1, padx=5)

    button_sort_penerbit = ctk.CTkButton(frame_buttons, text="Sortir berdasarkan Penerbit", command=lambda: sort_and_display(3, 1))
    button_sort_penerbit.grid(row=0, column=2, padx=5)

    button_sort_id_genre = ctk.CTkButton(frame_buttons, text="Sortir berdasarkan ID Genre", command=lambda: sort_and_display(4, 1))
    button_sort_id_genre.grid(row=0, column=3, padx=5)

    # Tempatkan frame untuk entry dan tombol pencarian
    frame_search = ctk.CTkFrame(AllFrame, fg_color='#FAFAFA')
    frame_search.pack(pady=10)

    # Tambahkan entry box untuk pencarian
    entry_label = ctk.CTkLabel(frame_search, text="Cari Judul Buku:", text_color='Black')
    entry_label.grid(row=0, column=0, padx=5)

    entry = ctk.CTkEntry(frame_search, fg_color='#FAFAFA', text_color='Black')
    entry.grid(row=0, column=1, padx=5)

    # Tambahkan tombol untuk melakukan pencarian
    button_search = ctk.CTkButton(frame_search, text="Cari")
    button_search.grid(row=0, column=2, padx=5)

    # Tempatkan Treeview di jendela utama
    tree.pack(pady=15)

    # Tambahkan event binding untuk menangani pemilihan item
    tree.bind('<<TreeviewSelect>>')

    frame_actions = ctk.CTkFrame(AllFrame, fg_color='#FAFAFA')
    frame_actions.pack(pady=10)

    # Tambahkan tombol untuk mengedit data
    button_edit = ctk.CTkButton(frame_actions, text="Edit")
    button_edit.grid(row=0, column=0, padx=5)

    # Tambahkan tombol untuk menambah data
    button_add = ctk.CTkButton(frame_actions, text="Tambah", command=MenambahData)
    button_add.grid(row=0, column=1, padx=5)

    # Tambahkan tombol untuk menghapus data
    button_delete = ctk.CTkButton(frame_actions, text="Hapus")
    button_delete.grid(row=0, column=2, padx=5)

    app.mainloop()
    

    

DataBuku()