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
        selected_item = tabelBuku.selection()[0]
        selected_data = tabelBuku.item(selected_item, 'values')
        
    def updateTabelData(): #Melakukan Update pada setiap data yang ada didalam data buku
        data = bacaDataDenda()
        for item in tabelBuku.get_children():
            tabelBuku.delete(item)
        for i, row in enumerate(data, start=1):
            if row[3] == '1':
                tabelBuku.insert('', ctk.END, values=(i, *row[:]))
    
    def hapusDataTerpilih(): #Menghapus data yang telah dipilih oleh user
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                id_buku = selected_data[1]
                cur.execute(f"UPDATE data_denda SET status_denda = '2' where id_denda = {id_buku}")
                conn.commit()
                updateTabelData()
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
    def sortingData(key, secondary_key=None): #Sorting dengan menggunakan Merge Sort
        data = bacaDataDenda()
        data = merge_sort(data, key, secondary_key)
        for item in tabelBuku.get_children():
            tabelBuku.delete(item)
        for i, row in enumerate(data, start=1):
            if row[3] == '1':
                tabelBuku.insert('', ctk.END, values=(i, *row[:]))

    def cariNamaOrang(): #Searching dengan menggunakan Binary Search
        search_term = inputJudulBuku.get().strip().lower()
        if search_term:
            data = bacaDataDenda()
            merge_sort(data, 1)
            index = binary_search_denda(data, search_term)
            if index != -1:
                tabelBuku.delete(*tabelBuku.get_children())
                tabelBuku.insert('', 'end', values=(1, *data[index][:]))
            else:
                messagebox.showinfo("Hasil Pencarian", f"Buku dengan judul '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan judul buku untuk mencari.")
    #Fungsi Pendukung dalam Jendela
    
    
    selected_data = None #Variabel untuk menampung nilai/data buku yang dipilih oleh user
    
    
    #UI Interface
    app = header()
        
    columns = ('#1', '#2', '#3', '#4', '#5')
    tabelBuku = ttk.Treeview(app, columns=columns, show='headings')

    tabelBuku.heading('#1', text='Nomor')
    tabelBuku.heading('#2', text='ID Denda')
    tabelBuku.heading('#3', text='Jumlah Denda')
    tabelBuku.heading('#4', text='Nama Anggota')
    tabelBuku.heading('#5', text='Status Denda')

    tabelBuku.column('#1', width=50)
    tabelBuku.column('#2', width=50)
    tabelBuku.column('#3', width=200)
    tabelBuku.column('#4', width=80)
    tabelBuku.column('#5', width=200)

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

    inputJudulBuku = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputJudulBuku.grid(row=0, column=1, padx=5)
    inputJudulBuku.bind("<Return>", lambda event: cariNamaOrang())

    tombolSearching = ctk.CTkButton(frameSearching, text="Cari", command=cariNamaOrang)
    tombolSearching.grid(row=0, column=2, padx=5)

    tabelBuku.pack(pady=15)
    tabelBuku.bind('<<TreeviewSelect>>', itemTerpilih)
    
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

def windowEditBuku(): #Jendela Edit Buku
    
    #Fungsi Pendukung dalam Jendela
    def back() :
        app.destroy()
        return   
    #Fungsi Pendukung dalam Jendela
    
    
    #Penghubung / Input kedalam Database
    def simpanDataEdit():
        id_buku = selected_data[1]
        new_data = (entries[0].get(), entries[1].get(), entries[2].get(), pilihGenre(entries[3].get(),'2'))
        cur.execute("UPDATE buku SET judul_buku = %s, tahun_terbit = %s, penerbit = %s, id_genre = %s WHERE id_buku = %s", (*new_data, id_buku))
        conn.commit()
        updateTabelData()
        
        app.destroy()
    #Penghubung / Input kedalam Database
    
    
    #UI Interface
    if selected_data:
                    
        app = header()
        editDataBukuLabel = ctk.CTkLabel(app, text="Edit Buku\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
        editDataBukuLabel.pack(padx=25, pady=15)
        mainFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        mainFrame.pack(padx=10, pady=10)

        labels = ["Judul Buku :", "Tahun Terbit :", "Penerbit :", "Genre:"]
        entries = []

        for i, text in enumerate(labels):
            label = ctk.CTkLabel(mainFrame, text=text, font=("Helvetica", 14), text_color="Black")
            label.grid(row=i, column=0, padx=5, pady=10, sticky='e')
            
            if text == "Genre:":
                entry = ctk.CTkComboBox(mainFrame,font=("Helvetica", 14),width=250, text_color='Black', fg_color='#FAFAFA', values=["Fiksi", "Non-Fiksi", "Sains", "Biografi", "Sejarah"], corner_radius=50)
            else:
                entry = ctk.CTkEntry(mainFrame,font=("Helvetica", 14),width=250, text_color='Black', fg_color='#FAFAFA')
            
            entry.grid(row=i, column=1, padx=10, pady=10, sticky='w')
            entries.append(entry)

        
        entries[0].insert(0, selected_data[2])
        entries[1].insert(0, selected_data[3])
        entries[2].insert(0, selected_data[4])
        genre = pilihGenre(selected_data[5], '1')
        entries[3].set(genre)

        frame_action = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        frame_action.pack(padx=10, pady=10)
        
        submit_button = ctk.CTkButton(frame_action, text="Submit", command=simpanDataEdit)
        submit_button.grid(row=0, column=0, padx=10, pady=5)

        button_kembali=ctk.CTkButton(frame_action, text="Kembali",command=back)
        button_kembali.grid(row=0, column=1, padx=10, pady=5)

    else:
        messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
    app.mainloop()
    #UI Interface
