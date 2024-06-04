from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from lib.utils.db import menambahkanData, fetch_data, cur, conn
from lib.utils.algoritma import merge_sort, dynamic_binary_search
from lib.components.header import header


<<<<<<< HEAD
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
        
    # def delete_selected_data():
    #     if selected_data:
    #         confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
    #         if confirm:
    #             nip = selected_data[0]
    #             cur.execute(f"DELETE FROM pustakawan WHERE nip = {nip}")
    #             conn.commit()
    #             update_treeview()
    #     else:
    #         messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
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

    # tombolSortingNama = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Nama", command=lambda: sort_and_display(1))
    # tombolSortingNama.grid(row=0, column=0, padx=5)

    # tombolSortingAlamat = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Alamat", command=lambda: sort_and_display(2, 1))
    # tombolSortingAlamat.grid(row=0, column=1, padx=5)

    # tombolSortingTelepon = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan No Telepon", command=lambda: sort_and_display(3, 1))
    # tombolSortingTelepon.grid(row=0, column=2, padx=5)

    # tombolSortingEmail = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Email", command=lambda: sort_and_display(4, 1))
    # tombolSortingEmail.grid(row=0, column=3, padx=5)

    # tombolSortingTanggal = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Tanggal Lahir", command=lambda: sort_and_display(5, 1))
    # tombolSortingTanggal.grid(row=0, column=4, padx=5)

    # frameSearching = ctk.CTkFrame(app, fg_color='#FAFAFA')
    # frameSearching.pack(pady=10)

    # labelSearching = ctk.CTkLabel(frameSearching, text="Cari Nama Pustakawan:", text_color='Black')
    # labelSearching.grid(row=0, column=0, padx=5)

    # inputNamaPustakawan = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    # inputNamaPustakawan.grid(row=0, column=1, padx=5)

    # # Tambahkan tombol untuk melakukan pencarian
    # tombolSearching = ctk.CTkButton(frameSearching, text="Cari", command=search_pustakawan)
    # tombolSearching.grid(row=0, column=2, padx=5)
    # inputNamaPustakawan.bind("<Return>", lambda event: search_pustakawan())

    # # Tempatkan Treeview di jendela utama
    # tabelPustakawan.pack(pady=15)

    # # Tambahkan event binding untuk menangani pemilihan item
    # tabelPustakawan.bind('<<TreeviewSelect>>', on_item_selected)

    tombolPerintah = ctk.CTkFrame(app, fg_color='#FAFAFA')
    tombolPerintah.pack()

    button_kembali=ctk.CTkButton(tombolPerintah, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)

    app = header()

    app.mainloop()
=======
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
>>>>>>> 7b53c327971557ed0f654bb143326576baa117fe
