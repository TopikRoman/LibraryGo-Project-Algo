from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from lib.utils.db import menambahkanData, fetch_data, cur, conn, readAnggota
from lib.utils.algoritma import merge_sort, dynamic_binary_search, linear_search_2_parameter
from lib.components.header import header
import string, random


def DataAnggota(akun):
    
    status = 0
    global selected_data
    
    
    #Fungsi Pendukung dalam jendela
    def back() :
        nonlocal status
        status = 1

        app.destroy()

    def dataTerpilih(event): #Memasukkan data yang dipilih oleh user kedalam variable
        global selected_data
        selected_item = tabelAnggota.selection()[0]
        selected_data = tabelAnggota.item(selected_item, 'values')
    
    def updateTabelData(): #Melakukan Update pada setiap data yang ada didalam data buku
        for item in tabelAnggota.get_children():
            tabelAnggota.delete(item)
        for i, row in enumerate(fetch_data("anggota_perpustakaan")):
            tabelAnggota.insert('', ctk.END, values=(i+1, *row[:]))
        
    def hapusDataTerpilih(): #Menghapus data yang dipilih
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                id_anggota = selected_data[1]
                DataMilikAnggota = fetch_data('peminjaman')
                DataMilikAnggota = merge_sort(DataMilikAnggota, 4)
                DataBuku = linear_search_2_parameter(DataMilikAnggota, '1', 4, int(id_anggota), 3)
                if DataBuku == -1:
                    cur.execute(f"DELETE FROM anggota_perpustakaan WHERE id_anggota = {id_anggota}")
                    conn.commit()
                else:
                    messagebox.showwarning("Peringatan", "Data Anggota Masih Memiliki Buku yang Dipinjam.")
                updateTabelData()
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
    def sortingData(key, secondary_key=None): #Sorting dengan menggunakan Merge Sort
        data = fetch_data("anggota_perpustakaan")
        data = merge_sort(data, key, secondary_key)
        for item in tabelAnggota.get_children():
            tabelAnggota.delete(item)
        for i, row in enumerate(data):
            tabelAnggota.insert('', ctk.END, values=(i+1, *row[:]))
            
    def searchingDataAnggota(): #Searching dengan menggunakan Binary Search
        search_term = inputIDAnggota.get().strip()
        if search_term:
            if str(search_term).isdigit():
                data = fetch_data("anggota_perpustakaan")
                merge_sort(data, 0)
                index = dynamic_binary_search(data, int(search_term))
                if index != -1:
                    tabelAnggota.delete(*tabelAnggota.get_children())
                    tabelAnggota.insert('', 'end', values=(1, *data[index]))
                else:
                    messagebox.showinfo("Hasil Pencarian", f"Anggota dengan ID '{search_term}' tidak ditemukan.")
            else:
                messagebox.showwarning("Peringatan", "Harap masukkan ID Anggota untuk mencari.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan ID Anggota untuk mencari.")

    #Fungsi Pendukung dalam jendela        
    
                        
    selected_data = None #Variabel untuk menampung nilai/data buku yang dipilih oleh user
    
    
    #UI Interface
    app = header()
    
    columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
    tabelAnggota = ttk.Treeview(app, columns=columns, show='headings')
    
    sortFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    sortFrame.pack(padx=10, pady=10)
    
    sortByNameButton = ctk.CTkButton(sortFrame, text="Sort by Name", command=lambda: sortingData(1))
    sortByNameButton.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

    sortByIDButton = ctk.CTkButton(sortFrame, text="Sort by ID", command=lambda: sortingData(0))
    sortByIDButton.grid(row=0, column=2, padx=10, pady=5, sticky='ew')
    
    frameSearching = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameSearching.pack(pady=10)

    labelSearching = ctk.CTkLabel(frameSearching, text="Cari ID Anggota :", text_color='Black')
    labelSearching.grid(row=0, column=0, padx=5)

    inputIDAnggota = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputIDAnggota.grid(row=0, column=1, padx=5)
    inputIDAnggota.bind("<Return>", lambda event: searchingDataAnggota())
    
    tombolSearching = ctk.CTkButton(frameSearching, text="Cari", command=searchingDataAnggota)
    tombolSearching.grid(row=0, column=2, padx=5)
    
    tabelAnggota.heading('#1', text='No')
    tabelAnggota.heading('#2', text='ID')
    tabelAnggota.heading('#3', text='Nama Anggota')
    tabelAnggota.heading('#4', text='Alamat')
    tabelAnggota.heading('#5', text='No. Telepon')
    tabelAnggota.heading('#6', text='Email')
    tabelAnggota.heading('#7', text='Tanggal Lahir')
    
    tabelAnggota.column('#1', width=60)
    tabelAnggota.column('#2', width=60)
    tabelAnggota.column('#3', width=200)
    tabelAnggota.column('#4', width=100)
    tabelAnggota.column('#5', width=100)
    tabelAnggota.column('#6', width=150)
    tabelAnggota.column('#7', width=100)
    
    data = fetch_data("anggota_perpustakaan")
    updateTabelData()
    
    tabelAnggota.pack(pady=15)
    tabelAnggota.bind('<ButtonRelease-1>', dataTerpilih)
    
    if akun[0][1] == 2 or akun[0][1] == 1:
        frame_actions = ctk.CTkFrame(app, fg_color='#FAFAFA')
        frame_actions.pack()

        button_edit = ctk.CTkButton(frame_actions, text="Edit", command=lambda: windowEditDataAnggota(updateTabelData))
        button_edit.grid(row=0, column=0, padx=10, pady=10)

        button_add = ctk.CTkButton(frame_actions, text="Tambah", command=lambda: windowTambahDataAnggota(updateTabelData))
        button_add.grid(row=0, column=1, padx=10, pady=10)
        
        button_delete = ctk.CTkButton(frame_actions, text="Hapus", command=hapusDataTerpilih)
        button_delete.grid(row=0, column=2, padx=10, pady=10)
            
    frame_kembali = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_kembali.pack()

    button_kembali=ctk.CTkButton(frame_kembali, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)
    
    app.mainloop()
    
    return status
    #UI Interface

def windowEditDataAnggota(updateTabelData):
    
    
    #Fungsi Pendukung dalam jendela
    def back() :
        app.destroy()
        return
    #Fungsi Pendukung dalam jendela
    
    
    #Penghubung kedalam data base
    def save_edit():
        if not entries[2].get().isdigit() or not entries[0].get() or not entries[1].get() or not entries[3].get() or not entries[4].get() or not entries[2]:
            messagebox.showwarning("Peringatan", "Masukkan data dengan benar !")
        else :
            id_anggota = selected_data[1]
            new_data = (entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get())
            cur.execute("UPDATE anggota_perpustakaan SET nama = %s, alamat = %s, no_telepon = %s, email = %s, tanggal_lahir = %s WHERE id_anggota = %s", (*new_data, id_anggota))
            conn.commit()
            updateTabelData()
            app.destroy()
    #Penghubung kedalam data base

    
    #UI Interface
    if selected_data:
        app = header()
        editDataAnggotaLabel = ctk.CTkLabel(app, text="Edit Anggota\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 40), text_color="Black")
        editDataAnggotaLabel.pack(padx=25, pady=15)
        mainFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        mainFrame.pack(padx=10, pady=10)

        labels = ["Nama:", "Alamat", "No. Telepon:", "Email:", "Tanggal lahir:"]
        entries = []
        
        Tanggal = StringVar()
        Tanggal.set(selected_data[6])
        
        for i, text in enumerate(labels):
            label = ctk.CTkLabel(mainFrame, text=text, font=("Helvetica", 14), text_color="Black") 
            label.grid(row=i, column=0, padx=5, pady=10, sticky='e')

            if text == "Tanggal lahir:":
                entry = DateEntry(mainFrame, width=50, background='darkblue', foreground='white', borderwidth=2, year=2023, date_pattern='yyyy-mm-dd')
                entry.delete(0, ctk.END)
                entry.insert(0, selected_data[6])
            else:
                entry = ctk.CTkEntry(mainFrame,font=("Helvetica", 14),width=250, text_color='Black', fg_color='#FAFAFA')

            entry.grid(row=i, column=1, padx=10, pady=10, sticky='w')
            entries.append(entry)

        entries[0].insert(0, selected_data[2])
        entries[1].insert(0, selected_data[3])
        entries[2].insert(0, selected_data[4])
        entries[3].insert(0, selected_data[5])

        frame_action = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        frame_action.pack(padx=10, pady=10)

        submit_button = ctk.CTkButton(frame_action, text="Submit", command=save_edit)
        submit_button.grid(row=0, column=0, padx=10, pady=5)

        button_kembali=ctk.CTkButton(frame_action, text="Kembali",command=back)
        button_kembali.grid(row=0, column=1, padx=10, pady=5)

    else:
        messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")

    app.mainloop()
    #UI Interface


def windowTambahDataAnggota(updateTabelData): # Jendela Menambah data anggota Perpustakaan
    
    #Fungsi Pendukung dalam jendela
    def back() :
        app.destroy()
        return
    #Fungsi Pendukung dalam jendela
    
    
    #Penghubung kedalam data base
    def upload_data(): 

        idanggota = Makeidanggota()
        nama = entries[0].get()
        alamat = entries[1].get()
        no_telepon = entries[2].get()
        email = entries[3].get()
        tanggal_lahir = entries[4].get()
        passcode = generate_password()
        
        if not str(idanggota).isdigit() or not str(no_telepon).isdigit() or not nama or not alamat or not email or not tanggal_lahir or not idanggota or not no_telepon:
            messagebox.showwarning("Peringatan", "Masukkan data dengan benar !")
        else:
            # Lanjutkan dengan proses upload data
            cur.execute(f"INSERT INTO anggota_perpustakaan (id_anggota, nama, alamat, no_telepon, email, tanggal_lahir, passcode) VALUES ({idanggota}, '{nama}', '{alamat}', '{no_telepon}', '{email}', '{tanggal_lahir}', '{passcode}')")
            conn.commit()        
            
            updateTabelData()
            app.destroy()
            messagebox.showinfo("Success", "Data anggota berhasil ditambahkan!")
    #Penghubung kedalam data base
    
    
    #UI Interface
    app = header()
    
    tambahDataAnggotaLabel = ctk.CTkLabel(app, text="Tambah Data Anggota\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 40), text_color="Black")
    tambahDataAnggotaLabel.pack(padx=25, pady=15)

    mainFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    mainFrame.pack(padx=10, pady=10)

    labels = ["Nama:", "Alamat:", "No. Telepon:", "Email:", "Tanggal Lahir:"]
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
    
    frame_action = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    frame_action.pack(padx=10, pady=10)
    
    submitData = ctk.CTkButton(frame_action, text="Submit", text_color='Black', command=upload_data)
    submitData.grid(row=0, column=0, padx=10, pady=10)

    tombolKembali=ctk.CTkButton(frame_action, text="Kembali", text_color='Black', command=back)
    tombolKembali.grid(row=0, column=1, padx=10, pady=10)

    app.mainloop()
    #UI Interface




def Makeidanggota() :
    
    while True:
        idanggota = random.randint(100000, 999999)
        cek = readAnggota(idanggota)
        if len(cek) == 0:
            return idanggota

def generate_password():
    characters = string.digits + string.ascii_letters
    password = ""
    for _ in range(8):
        password += random.choice(characters)
    return password
