from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from lib.utils.db import menambahkanData, fetch_data, cur, conn, readAnggota
from lib.utils.algoritma import merge_sort, binary_search, binary_search_for_id
from lib.components.header import header
import random


def DataAnggota():
    status = 0

    global selected_data
    
    def back() :
        nonlocal status
        status = 1

        app.destroy()

    def on_item_selected(event):
        global selected_data
        selected_item = tabelAnggota.selection()[0]
        selected_data = tabelAnggota.item(selected_item, 'values')
        
    def delete_selected_data():
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                id_anggota = selected_data[0]
                cur.execute(f"DELETE FROM anggota_perpustakaan WHERE id_anggota = {id_anggota}")
                conn.commit()
                update_treeview()
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
    def sort_and_display(key, secondary_key=None):
        data = fetch_data("anggota_perpustakaan")
        data = merge_sort(data, key, secondary_key)
        for item in tabelAnggota.get_children():
            tabelAnggota.delete(item)
        for row in data:
            tabelAnggota.insert('', ctk.END, values=row)
            
    def search_anggota():
        search_term = inputIDAnggota.get().strip()
        if search_term:
            data = fetch_data("anggota_perpustakaan")
            merge_sort(data, 0)  # Ensure data is sorted by title before binary search
            index = binary_search_for_id(data, int(search_term), 0)
            if index != -1:
                tabelAnggota.delete(*tabelAnggota.get_children())  # Remove all existing data
                tabelAnggota.insert('', 'end', values=data[index])  # Insert the searched data
            else:
                messagebox.showinfo("Hasil Pencarian", f"Buku dengan judul '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan judul buku untuk mencari.")

    def update_treeview():
        for item in tabelAnggota.get_children():
            tabelAnggota.delete(item)
        for row in fetch_data("anggota_perpustakaan"):
            tabelAnggota.insert('', ctk.END, values=row)
            
    def tambah_data_peminjam():
        
        app = header()
        
        def back() :
            app.destroy()
            update_treeview()
            return
        
        def upload_data(): 

            # Retrieve the values entered in the form
            idanggota = Makeidanggota()
            nama = entries[0].get()
            tanggal_lahir = entries[1].get()
            alamat = entries[2].get()
            no_telepon = entries[3].get()
            email = entries[4].get()

            # Insert the data into the database
            cur.execute(f"INSERT INTO anggota_perpustakaan (id_anggota, nama, tanggal_lahir, alamat, no_telepon, email) VALUES ({idanggota}, '{nama}', '{tanggal_lahir}', '{alamat}', '{no_telepon}', '{email}')")
            conn.commit()
            update_treeview()
            
            messagebox.showinfo("Success", "Data anggota berhasil ditambahkan!")
        
        tambahDataAnggotaLabel = ctk.CTkLabel(app, text="Tambah Anggota\nLiGO", font=("Helvetica", 25), text_color="Black")
        tambahDataAnggotaLabel.pack(padx=25, pady=15)

        mainFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        mainFrame.pack(padx=10, pady=10)

        labels = ["Nama:", "Tanggal Lahir:", "Alamat:", "No telepon:", "Email:"]
        entries = []

        for i, text in enumerate(labels):
            label = ctk.CTkLabel(mainFrame, text=text, font=("Helvetica", 14), text_color="Black")
            label.grid(row=i, column=0, padx=5, pady=10, sticky='e')
            
            if text == "Tanggal Lahir:":
                entry = DateEntry(mainFrame, widht=50, background='darkblue', foreground='white', borderwidth=2, year=2023, date_pattern='yyyy-mm-dd')
            else:
                entry = ctk.CTkEntry(mainFrame, width=300, fg_color='#FAFAFA', text_color='Black', placeholder_text=text.replace(":", ""))
            
            entry.grid(row=i, column=1, padx=10, pady=10, sticky='w')
            entries.append(entry)

        submitData = ctk.CTkButton(app, text="Submit", fg_color='#FF3399', text_color='Black', corner_radius=50, command=upload_data)
        submitData.pack(padx=25, pady=5)

        tombolKembali=ctk.CTkButton(app, text="Kembali", fg_color='#FF3399', text_color='Black', command=back, corner_radius=50)
        tombolKembali.pack(pady=5)

        app.mainloop()
    
        
    selected_data = None
    app = header()
    
    columns = ('#1', '#2', '#3', '#4', '#5', '6')
    tabelAnggota = ttk.Treeview(app, columns=columns, show='headings')
    
    # Creating the sorting buttons
    sortFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    sortFrame.pack(padx=10, pady=10)
    
    sortByNameButton = ctk.CTkButton(sortFrame, text="Sort by Name", command=lambda: sort_and_display(1))
    sortByNameButton.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

    sortByIDButton = ctk.CTkButton(sortFrame, text="Sort by ID", command=lambda: sort_and_display(0))
    sortByIDButton.grid(row=0, column=2, padx=10, pady=5, sticky='ew')
    
    frameSearching = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameSearching.pack(pady=10)

    labelSearching = ctk.CTkLabel(frameSearching, text="Cari ID Anggota :", text_color='Black')
    labelSearching.grid(row=0, column=0, padx=5)

    inputIDAnggota = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputIDAnggota.grid(row=0, column=1, padx=5)
    
    tombolSearching = ctk.CTkButton(frameSearching, text="Cari", command=search_anggota)
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
    
    data = fetch_data("anggota_perpustakaan")
    update_treeview()
    tabelAnggota.pack(pady=15)
    tabelAnggota.bind('<ButtonRelease-1>', on_item_selected)
    
    frame_actions = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_actions.pack()

    # Tambahkan tombol untuk mengedit data
    button_edit = ctk.CTkButton(frame_actions, text="Edit")
    button_edit.grid(row=0, column=0, padx=5,pady=5)

    # Tambahkan tombol untuk menambah data
    button_add = ctk.CTkButton(frame_actions, text="Tambah", command=tambah_data_peminjam)
    button_add.grid(row=0, column=1, padx=5)

    # Tambahkan tombol untuk menghapus data
    button_delete = ctk.CTkButton(frame_actions, text="Hapus", command=delete_selected_data)
    button_delete.grid(row=0, column=2, padx=5)
    
    button_kembali=ctk.CTkButton(frame_actions, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=3, padx=5)
    
    app.mainloop()
    
    return status

def Makeidanggota() :
    
    while True:
        idanggota = random.randint(100000, 999999)
        cek = readAnggota(idanggota)
        if len(cek) == 0:
            return idanggota


