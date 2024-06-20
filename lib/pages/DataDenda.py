from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from lib.utils.db import menambahkanData, fetch_data, cur, conn, readAnggota, bacaDataDenda
from lib.utils.algoritma import merge_sort, dynamic_binary_search, binary_search_denda
from lib.components.header import header
import string, random

def dataDenda(akun):
    
    status = 0
    global selected_data


    #Fungsi Pendukung dalam Jendela
    def back() : #Fungsi untuk keluar dari jendela
        nonlocal status
        status = 1
        app.destroy()
        
    def itemTerpilih(event): #Fungsi untuk memasukkan data yang dipilih user kedalam variabel
        global selected_data
        selected_item = tabelDenda.selection()[0]
        selected_data = tabelDenda.item(selected_item, 'values')
        
    def updateTabelData(): #Melakukan Update pada setiap data yang ada didalam data buku
        data = bacaDataDenda()
        for item in tabelDenda.get_children():
            tabelDenda.delete(item)
        for i, row in enumerate(data, start=1):
            tabelDenda.insert('', ctk.END, values=(i, *row[:]))
    
    def hapusDataTerpilih(): #Menghapus data yang telah dipilih oleh user
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                id_buku = selected_data[1]
                cur.execute(f"DELETE FROM data_denda WHERE id_denda = {id_buku}")
                conn.commit()
                updateTabelData()
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
    def sortingData(key, secondary_key=None): #Sorting dengan menggunakan Merge Sort
        data = bacaDataDenda()
        data = merge_sort(data, key, secondary_key)
        for item in tabelDenda.get_children():
            tabelDenda.delete(item)
        for i, row in enumerate(data, start=1):
            tabelDenda.insert('', ctk.END, values=(i, *row[:]))

    def cariNamaOrang(): #Searching dengan menggunakan Binary Search
        search_term = inputNamaPeminjam.get().strip().lower()
        if search_term:
            data = bacaDataDenda()
            merge_sort(data, 2)
            index = binary_search_denda(data, search_term)
            if index != -1:
                tabelDenda.delete(*tabelDenda.get_children())
                tabelDenda.insert('', 'end', values=(1, *data[index][:]))
            else:
                messagebox.showinfo("Hasil Pencarian", f"Buku dengan judul '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan judul buku untuk mencari.")
    #Fungsi Pendukung dalam Jendela
    
    
    selected_data = None #Variabel untuk menampung nilai/data buku yang dipilih oleh user
    
    
    #UI Interface
    app = header()
        
    columns = ('#1', '#2', '#3', '#4')
    tabelDenda = ttk.Treeview(app, columns=columns, show='headings')

    tabelDenda.heading('#1', text='Nomor')
    tabelDenda.heading('#2', text='ID Denda')
    tabelDenda.heading('#3', text='Jumlah Denda')
    tabelDenda.heading('#4', text='Nama Anggota')

    tabelDenda.column('#1', width=50)
    tabelDenda.column('#2', width=50)
    tabelDenda.column('#3', width=200)
    tabelDenda.column('#4', width=150)

    data = bacaDataDenda()
    updateTabelData()
        
    frameTombolSorting = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameTombolSorting.pack(pady=10)

    tombolSortingNama = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Nama", command=lambda: sortingData(2))
    tombolSortingNama.grid(row=0, column=0, padx=5)

    tombolSortingDenda = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Jumlah Denda", command=lambda: sortingData(1))
    tombolSortingDenda.grid(row=0, column=1, padx=5)

    frameSearching = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameSearching.pack(pady=10)

    labelSearching = ctk.CTkLabel(frameSearching, text="Cari Nama Peminjam:", text_color='Black')
    labelSearching.grid(row=0, column=0, padx=5)

    inputNamaPeminjam = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputNamaPeminjam.grid(row=0, column=1, padx=5)
    inputNamaPeminjam.bind("<Return>", lambda event: cariNamaOrang())

    tombolSearching = ctk.CTkButton(frameSearching, text="Cari", command=cariNamaOrang)
    tombolSearching.grid(row=0, column=2, padx=5)

    tabelDenda.pack(pady=15)
    tabelDenda.bind('<<TreeviewSelect>>', itemTerpilih)
    
    tombolPerintah = ctk.CTkFrame(app, fg_color='#FAFAFA')
    tombolPerintah.pack()
    
    button_kembali=ctk.CTkButton(tombolPerintah, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)
    
    if akun[0][1] == 2 or akun[0][1] == 1:

        button_pembayaran = ctk.CTkButton(tombolPerintah, text="Pembayaran", command=hapusDataTerpilih)
        button_pembayaran.grid(row=0, column=0, padx=10, pady=10)
        
    app.mainloop()
    #UI Interface
    
    return status