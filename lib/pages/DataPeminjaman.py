from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from lib.utils.db import menambahkanData, fetch_data, cur, conn, readAnggota, membacaPeminjaman, membacaDetailPeminjaman, membacaIDAnggota, menarikDataDenda
from lib.utils.algoritma import merge_sort, dynamic_binary_search, linear_search
from lib.components.header import header
import string, random
from datetime import datetime, timedelta


def DataPeminjaman(akun):
    
    status = 0
    global selected_data
    id_anggota_pengguna = akun[0][0][1]  # Assuming that this is the correct index for id_anggota in akun
    
    #Fungsi Pendukung dalam jendela
    def back() :
        nonlocal status
        status = 1

        app.destroy()

    def dataTerpilih(event): #Memasukkan data yang dipilih oleh user kedalam variable
        global selected_data
        selected_item = tabelPeminjaman.selection()[0]
        selected_data = tabelPeminjaman.item(selected_item, 'values')
    
    def updateTabelData(): #Melakukan Update pada setiap data yang ada didalam data buku
        for item in tabelPeminjaman.get_children():
            tabelPeminjaman.delete(item)
        for i, row in enumerate(membacaPeminjaman()):
            if row[4] == '1':  # Compare id_anggota in row with the user's id_anggota
                tabelPeminjaman.insert('', ctk.END, values=(i+1, *row[:]))
                
    def updateTabelDataMilikAnggota():
        for item in tabelPeminjaman.get_children():
            tabelPeminjaman.delete(item)
            
        for i, row in enumerate(membacaPeminjaman()):
            if row[3] == id_anggota_pengguna and row[4] == '1':  # Compare id_anggota in row with the user's id_anggota
                tabelPeminjaman.insert('', ctk.END, values=(i+1, *row[:]))
    
    def hapusDataTerpilih(): #Menghapus data yang dipilih
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                id_peminjaman = selected_data[1]
                try:
                    cur.execute(f"DELETE FROM peminjaman WHERE id_peminjaman = {id_peminjaman}")
                    conn.commit()
                    updateTabelData()
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete peminjaman: {e}")
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
        
    def hapusDataTerpilih(): #Menghapus data yang dipilih
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                id_peminjaman = selected_data[1]
                cur.execute(f"DELETE FROM peminjaman WHERE id_peminjaman = {id_peminjaman}")
                conn.commit()
                updateTabelData()
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
    def sortingData(key, secondary_key=None): #Sorting dengan menggunakan Merge Sort
        data = membacaPeminjaman()
        data = merge_sort(data, key, secondary_key)
        for item in tabelPeminjaman.get_children():
            tabelPeminjaman.delete(item)
        for i, row in enumerate(data):
            if row[4] == '1':  # Compare id_anggota in row with the user's id_anggota
                tabelPeminjaman.insert('', ctk.END, values=(i+1, *row[:]))
            
    def searchingDataPeminjaman():
        search_term = inputNamaPeminjam.get().strip()
        if search_term:
            data = membacaPeminjaman()
            merge_sort(data, 3)  # Mengurutkan data berdasarkan kolom nama (index ke-2)
            results = linear_search(data, search_term, 3)  # Mencari berdasarkan kolom nama (index ke-2)

            if results:
                tabelPeminjaman.delete(*tabelPeminjaman.get_children())
                for i, row in enumerate(results):
                    if row[4] == '1':
                        tabelPeminjaman.insert('', 'end', values=(i, *row[:]))
            else:
                messagebox.showinfo("Hasil Pencarian", f"Anggota dengan nama '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan nama Anggota untuk mencari.")


    #Fungsi Pendukung dalam jendela        
    
                        
    selected_data = None #Variabel untuk menampung nilai/data buku yang dipilih oleh user
    selected_data_buku = None
    
    #UI Interface
    app = header()
    
    columns = ('#1', '#2', '#3', '#4', '#5')
    tabelPeminjaman = ttk.Treeview(app, columns=columns, show='headings')
    if akun[0][1] == 2 or akun[0][1] == 1:

        sortFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        sortFrame.pack(padx=10, pady=10)
        
        sortByTanggalPeminjaman = ctk.CTkButton(sortFrame, text="Sorting Tanggal Peminjaman", command=lambda: sortingData(1))
        sortByTanggalPeminjaman.grid(row=0, column=1, padx=10, pady=5, sticky='ew')

        sortByTenggatPengembalian = ctk.CTkButton(sortFrame, text="Sorting Tenggat Pengembalian", command=lambda: sortingData(3))
        sortByTenggatPengembalian.grid(row=0, column=2, padx=10, pady=5, sticky='ew')
            
        sortByIDPeminjam = ctk.CTkButton(sortFrame, text="Sorting ID Anggota", command=lambda: sortingData(5))
        sortByIDPeminjam.grid(row=0, column=0, padx=10, pady=5, sticky='ew')
    
    if akun[0][1] == 2 or akun[0][1] == 1:
        frameSearching = ctk.CTkFrame(app, fg_color='#FAFAFA')
        frameSearching.pack(pady=10)

        labelSearching = ctk.CTkLabel(frameSearching, text="Cari Nama Anggota :", text_color='Black')
        labelSearching.grid(row=0, column=0, padx=5)
        
        inputNamaPeminjam = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
        inputNamaPeminjam.grid(row=0, column=1, padx=5)
        inputNamaPeminjam.bind("<Return>", lambda event: searchingDataPeminjaman())
    
        tombolSearching = ctk.CTkButton(frameSearching, text="Cari", command=searchingDataPeminjaman)
        tombolSearching.grid(row=0, column=2, padx=5)
    
    tabelPeminjaman.heading('#1', text='No')
    tabelPeminjaman.heading('#2', text='ID Peminjaman')
    tabelPeminjaman.heading('#3', text='Tanggal Peminjaman')
    tabelPeminjaman.heading('#4', text='Tenggat Peminjaman')
    tabelPeminjaman.heading('#5', text='Nama Anggota')
    
    tabelPeminjaman.column('#1', width=60)
    tabelPeminjaman.column('#2', width=60)
    tabelPeminjaman.column('#3', width=200)
    tabelPeminjaman.column('#4', width=100)
    tabelPeminjaman.column('#5', width=100)
    
    data = membacaPeminjaman()
    
    if akun[0][1] == 3:
        updateTabelDataMilikAnggota()
    else:
        updateTabelData()
    
    tabelPeminjaman.pack(pady=15)
    tabelPeminjaman.bind('<ButtonRelease-1>', dataTerpilih)
    
    frame_actions = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_actions.pack()
    
    frame_actions2 = ctk.CTkFrame(frame_actions, fg_color='#FAFAFA')
    frame_actions2.grid(row=1, column = 2)
    
    
    button_detail = ctk.CTkButton(frame_actions2, text="Detail", command=lambda: show_detail(tabelPeminjaman))
    button_detail.grid(row=0, column=1, padx=10, pady=10)
    
    if akun[0][1] == 2 or akun[0][1] == 1:

        button_add = ctk.CTkButton(frame_actions, text="Tambah", command=MenambahDataPeminjaman)
        button_add.grid(row=0, column=1, padx=10, pady=10)
        
        button_delete = ctk.CTkButton(frame_actions, text="Hapus", command=hapusDataTerpilih)
        button_delete.grid(row=0, column=2, padx=10, pady=10)
        
        button_history = ctk.CTkButton(frame_actions, text="History", command=History)
        button_history.grid(row=0, column=3, padx=10, pady=10)
        
        button_pengembalian = ctk.CTkButton(frame_actions2, text="Pengembalian", command=lambda: pengembalianBuku(tabelPeminjaman, updateTabelData))
        button_pengembalian.grid(row=0, column=2, padx=10, pady=10)
            
    frame_kembali = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_kembali.pack()

    button_kembali=ctk.CTkButton(frame_kembali, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)
    
    app.mainloop()
    
    return status

def MenambahDataPeminjaman():
    
    global dataBukuTerpilihonselect
    
    app = header()
    
    def back() :
        app.destroy()
        return
    
    def onSelect(selected_data):
        nama_entry.delete(0, ctk.END)
        nama_entry.insert(0, selected_data_anggota[2])
        
    def onSelectBuku(selected_data):
        exists = 0
        iddatabaru = int(selected_data_buku[1])
        
        for row in table.get_children():
            iddatalama = int(table.item(row)['values'][0])
            if iddatalama == iddatabaru:
                exists += 1
        print(exists)
        if exists == 0:
            table.insert('', 'end', values=(selected_data_buku[1], selected_data_buku[2]))
        else:
            messagebox.showwarning("Warning", "This book has already been added.")
    
    def dataBukuTerpilihonselect(event):
        global dataBukuTerpilihonselect
        selected_item = table.selection()[0]
        dataBukuTerpilihonselect = table.item(selected_item, 'values')

    def delete_selected_row():
        dataBukuTerpilihonselect = table.selection()
        if dataBukuTerpilihonselect:
            table.delete(dataBukuTerpilihonselect[0])
        else:
            messagebox.showwarning("Warning", "Pilih data buku")  
                  
    def submit_peminjaman():
        # Get today's date and calculate the due date
        today = datetime.now()
        due_date = today + timedelta(days=7)
        
        # Format dates in the format yyyy-mm-dd
        tanggal_peminjaman = today.strftime('%Y-%m-%d')
        tenggat_pengembalian = due_date.strftime('%Y-%m-%d')
        try:
            id_anggota = selected_data_anggota[1]
        except:
            messagebox.showwarning("Warning", "Masukkan Identitas Anggota")
        
        book_ids = [int(table.item(row)['values'][0]) for row in table.get_children()]
        if not book_ids:
            messagebox.showwarning("Warning", "Please select at least one book.")
            return
        status_peminjaman = '1'  # Assuming '1' signifies an active loan
        
        insert_peminjaman_query = """INSERT INTO peminjaman (tanggal_peminjaman, tenggat_pengembalian, id_anggota, status_peminjaman)
                                    VALUES (%s, %s, %s, %s) RETURNING id_peminjaman;"""
        cur.execute(insert_peminjaman_query, (tanggal_peminjaman, tenggat_pengembalian, id_anggota, status_peminjaman))
        peminjaman_id = cur.fetchone()[0]
        conn.commit()
        
        # Insert selected books into detail_peminjaman table
        # Assuming you have a list or similar structure to keep track of selected books
        for book_id in book_ids:
            insert_detail_query = """INSERT INTO detail_peminjaman (id_peminjaman, id_buku, status_peminjaman)
                                    VALUES (%s, %s, %s);"""
            cur.execute(insert_detail_query, (peminjaman_id, book_id, status_peminjaman))
        conn.commit()
        
        # Show a success message
        messagebox.showinfo("Success", "Data peminjaman berhasil diupload.")
        
        app.destroy()

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
    pilih_button = ctk.CTkButton(form_frame, text="Pilih", text_color="Black", command=lambda: DataAnggota(onSelect))
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
    table.bind('<ButtonRelease-1>', dataBukuTerpilihonselect)

    on_selected_buku_menambah = None 
    
    frame_button = ctk.CTkFrame(form_frame, fg_color='white')
    frame_button.grid(row=1, column=2, padx=10, pady=10)
    
    tambah_button = ctk.CTkButton(frame_button, text="Tambah", text_color="Black", command=lambda: tampilanDataBuku(onSelectBuku))
    tambah_button.grid(row=0, column=0, padx=10, pady=10)
    
    hapus_button = ctk.CTkButton(frame_button, text="Hapus", text_color="Black", command=delete_selected_row)
    hapus_button.grid(row=1, column=0, padx=10, pady=10)
    
    frame_tombol = ctk.CTkFrame(app, fg_color='white')
    frame_tombol.pack(pady=10)
    
    submitData = ctk.CTkButton(frame_tombol, text="Submit", command=submit_peminjaman)
    submitData.grid(row=0, column=0, padx=10, pady=10)
    
    Keluar = ctk.CTkButton(frame_tombol, text="Kembali", command=back)
    Keluar.grid(row=0, column=1, padx=10, pady=10)
    
    app.mainloop()
    
def DataAnggota(callback):
    
    status = 0
    global selected_data_anggota
    
    
    #Fungsi Pendukung dalam jendela
    def back() :
        app.destroy()
        return

    def dataTerpilih(event): #Memasukkan data yang dipilih oleh user kedalam variable
        global selected_data_anggota
        selected_item = tabelAnggota.selection()[0]
        selected_data_anggota = tabelAnggota.item(selected_item, 'values')
        print(selected_data_anggota[2])
        
    def pilihData():
        app.destroy()
        callback(selected_data_anggota)
    
    def updateTabelData(): #Melakukan Update pada setiap data yang ada didalam data buku
        for item in tabelAnggota.get_children():
            tabelAnggota.delete(item)
        for i, row in enumerate(fetch_data("anggota_perpustakaan")):
            tabelAnggota.insert('', ctk.END, values=(i+1, *row[:]))
    
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
            data = fetch_data("anggota_perpustakaan")
            merge_sort(data, 0)
            index = dynamic_binary_search(data, int(search_term))
            if index != -1:
                tabelAnggota.delete(*tabelAnggota.get_children())
                tabelAnggota.insert('', 'end', values=data[index])
            else:
                messagebox.showinfo("Hasil Pencarian", f"Anggota dengan ID '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan ID Anggota untuk mencari.")

    #Fungsi Pendukung dalam jendela        
    
                        
    selected_data_anggota = None #Variabel untuk menampung nilai/data buku yang dipilih oleh user
    
    
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
                
    frame_kembali = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_kembali.pack(pady=10)

    button_kembali=ctk.CTkButton(frame_kembali, text="Kembali",command=back)
    button_kembali.grid(row=0,columns=1, padx=10, pady=10)
    
    button_pilih = ctk.CTkButton(frame_kembali, text="Pilih", command=pilihData)
    button_pilih.grid(row=0, column=2, padx=10, pady=10)
    
    app.mainloop()
    
    return status

def show_detail(tabelPeminjaman):
    
    def back() :
        detail_window.destroy()
        return
    
    def updateTabelDataPeminjaman(): #Melakukan Update pada setiap data yang ada didalam data buku
        data = membacaDetailPeminjaman()
        for item in tablePeminjaman.get_children():
            tablePeminjaman.delete(item)
        for i, row in enumerate(data):
            print(data[i][0], selected_data[1])
            if (data[i][3]) == int(selected_data[1]) and data[i][2] == '1' :
                tablePeminjaman.insert('', ctk.END, values=(data[i][0], data[i][1]))
    
    try:
        selected_item = tabelPeminjaman.selection()[0]
    except:
        messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
        return
    
    selected_data = tabelPeminjaman.item(selected_item, 'values')
    
    detail_window = header()
    detail_window.title("Detail Peminjaman")
    
        
    
    detailPeminjamanlabel = ctk.CTkLabel(detail_window, text="Detail Peminjaman", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
    detailPeminjamanlabel.pack(padx=25, pady=15)
    
    frame = ctk.CTkFrame(detail_window, fg_color='#FAFAFA')
    frame.pack(pady=10)
    
    # Create labels for the detail information
    id_label = ctk.CTkLabel(frame, text="ID Peminjaman:", text_color="Black")
    id_label.grid(row=0, column=0, padx=10, pady=10)
    
    nilai_label_id = ctk.CTkLabel(frame, text=f"{selected_data[1]}", text_color="Black")
    nilai_label_id.grid(row=0, column=1, padx=10, pady=10)
    
    nama_label = ctk.CTkLabel(frame, text="Nama Peminjaman:", text_color="Black")
    nama_label.grid(row=1, column=0, padx=10, pady=10)
    
    nilai_label_nama = ctk.CTkLabel(frame, text=f"{selected_data[4]}", text_color="Black")
    nilai_label_nama.grid(row=1, column=1, padx=10, pady=10)
    
    tanggal_label = ctk.CTkLabel(frame, text="Tanggal Peminjaman:", text_color="Black")
    tanggal_label.grid(row=2, column=0, padx=10, pady=10)

    nilai_label_tanggal = ctk.CTkLabel(frame, text=f"{selected_data[2]}", text_color="Black")
    nilai_label_tanggal.grid(row=2, column=1, padx=10, pady=10)
    
    tenggat_label = ctk.CTkLabel(frame, text="Tenggat Pengembalian:", text_color="Black")
    tenggat_label.grid(row=3, column=0, padx=10, pady=10)
    
    nilai_label_tenggat = ctk.CTkLabel(frame, text=f"{selected_data[3]}", text_color="Black")
    nilai_label_tenggat.grid(row=3, column=1, padx=10, pady=10)
    
    status_label = ctk.CTkLabel(frame, text="Status Peminjaman:", text_color="Black")
    status_label.grid(row=4, column=0, padx=10, pady=10)
    
    judulbukudipinjam = selected_data[5]
    
    match judulbukudipinjam:
        case "1":
            judulbukudipinjam = 'Belum di Kembalikan'
        case "2":
            judulbukudipinjam = 'Sudah di Kembalikan'
            
    nilai_label_status = ctk.CTkLabel(frame, text=f"{judulbukudipinjam}", text_color="Black")
    nilai_label_status.grid(row=4, column=1, padx=10, pady=10)
    
    buku_label = ctk.CTkLabel(frame, text="Judul Buku:", text_color="Black")
    buku_label.grid(row=5, column=0, padx=10, pady=10, sticky=E)
    
        # Creating the table using Treeview widget
    tablePeminjaman = ttk.Treeview(frame, columns=('Column1', 'Column2'), show='headings', height=5)
    tablePeminjaman.heading('Column1', text='ID Buku')
    tablePeminjaman.heading('Column2', text='Judul Buku')
    tablePeminjaman.column('Column1', width=60)
    tablePeminjaman.column('Column2', width=125)
    tablePeminjaman.grid(row=5, column=1, padx=10, pady=10, sticky='nsew')
    updateTabelDataPeminjaman()
    
    # # Create a table to display the list of books
    # table_frame = Frame(detail_window)
    # table_frame.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    
    # table = ttk.Treeview(table_frame, columns=('ID Buku', 'Judul Buku'))
    # table.heading('ID Buku', text='ID Buku')
    # table.heading('Judul Buku', text='Judul Buku')
    # table.column('ID Buku', width=100)
    # table.column('Judul Buku', width=200)
    # table.grid(row=0, column=0, padx=10, pady=10, sticky='nsew')
    
    # # Fill the labels and table with the selected data
    
    # id_label.config(text="ID Peminjaman: " + selected_data[0])
    # nama_label.config(text="Nama Peminjaman: " + selected_data[1])
    # tanggal_label.config(text="Tanggal Peminjaman: " + selected_data[2])
    # tenggat_label.config(text="Tenggat Pengembalian: " + selected_data[3])
    # status_label.config(text="Status Peminjaman: " + selected_data[4])
    
    # # Fill the table with the list of books
    # for row in selected_data[5:]:
    #     table.insert('', 'end', values=row)

    frame2 = ctk.CTkFrame(detail_window, fg_color='#FAFAFA')
    frame2.pack(pady=10)
    
    button_kembali=ctk.CTkButton(frame2, text="Kembali",command=back)
    button_kembali.grid(row=0,columns=1, padx=10, pady=15)
    
def tampilanDataBuku(callback):
    
    status = 0
    global selected_data


    #Fungsi Pendukung dalam Jendela
    def back() :
        app.destroy()
        return
        
    def itemTerpilih(event): #Fungsi untuk memasukkan data yang dipilih user kedalam variabel
        global selected_data_buku
        selected_item = tabelBuku.selection()[0]
        selected_data_buku = tabelBuku.item(selected_item, 'values')
        
    def pilihData():
        app.destroy()
        callback(selected_data_buku)
        
    def updateTabelData(): #Melakukan Update pada setiap data yang ada didalam data buku
        data = fetch_data("buku")
        for item in tabelBuku.get_children():
            tabelBuku.delete(item)
        for i, row in enumerate(data, start=1):
            tabelBuku.insert('', ctk.END, values=(i, *row[:]))
    
    def sortingData(key, secondary_key=None): #Sorting dengan menggunakan Merge Sort
        data = fetch_data("buku")
        data = merge_sort(data, key, secondary_key)
        for item in tabelBuku.get_children():
            tabelBuku.delete(item)
        for i, row in enumerate(data, start=1):
            tabelBuku.insert('', ctk.END, values=(i, *row[:]))

    def cariJudulBuku(): #Searching dengan menggunakan Binary Search
        search_term = inputJudulBuku.get().strip().lower()
        if search_term:
            data = fetch_data("buku")
            merge_sort(data, 1)
            index = dynamic_binary_search(data, search_term)
            if index != -1:
                tabelBuku.delete(*tabelBuku.get_children())
                tabelBuku.insert('', 'end', values=(1, *data[index][:]))
            else:
                messagebox.showinfo("Hasil Pencarian", f"Buku dengan judul '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan judul buku untuk mencari.")
    #Fungsi Pendukung dalam Jendela
    
    
    selected_data_buku = None #Variabel untuk menampung nilai/data buku yang dipilih oleh user
    
    
    #UI Interface
    app = header()
        
    columns = ('#1', '#2', '#3', '#4', '#5', '#6')
    tabelBuku = ttk.Treeview(app, columns=columns, show='headings')

    tabelBuku.heading('#1', text='Nomor')
    tabelBuku.heading('#2', text='ID Buku')
    tabelBuku.heading('#3', text='Judul Buku')
    tabelBuku.heading('#4', text='Tahun Terbit')
    tabelBuku.heading('#5', text='Penerbit')
    tabelBuku.heading('#6', text='ID Genre')

    tabelBuku.column('#1', width=50)
    tabelBuku.column('#2', width=50)
    tabelBuku.column('#3', width=200)
    tabelBuku.column('#4', width=80)
    tabelBuku.column('#5', width=200)
    tabelBuku.column('#6', width=80)

    data = fetch_data("buku")
    updateTabelData()
        
    frameTombolSorting = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameTombolSorting.pack(pady=10)

    tombolSortingJudul = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Judul", command=lambda: sortingData(1))
    tombolSortingJudul.grid(row=0, column=0, padx=5)

    tombolSortingTahun = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Tahun Terbit", command=lambda: sortingData(2, 1))
    tombolSortingTahun.grid(row=0, column=1, padx=5)

    tombolSortingPenerbit = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Penerbit", command=lambda: sortingData(3, 1))
    tombolSortingPenerbit.grid(row=0, column=2, padx=5)

    tombolSortingIdGenre = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan ID Genre", command=lambda: sortingData(4, 1))
    tombolSortingIdGenre.grid(row=0, column=3, padx=5)

    frameSearching = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameSearching.pack(pady=10)

    labelSearching = ctk.CTkLabel(frameSearching, text="Cari Judul Buku:", text_color='Black')
    labelSearching.grid(row=0, column=0, padx=5)

    inputJudulBuku = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputJudulBuku.grid(row=0, column=1, padx=5)
    inputJudulBuku.bind("<Return>", lambda event: cariJudulBuku())

    tombolSearching = ctk.CTkButton(frameSearching, text="Cari", command=cariJudulBuku)
    tombolSearching.grid(row=0, column=2, padx=5)

    tabelBuku.pack(pady=15)
    tabelBuku.bind('<<TreeviewSelect>>', itemTerpilih)
    
    tombolPerintah = ctk.CTkFrame(app, fg_color='#FAFAFA')
    tombolPerintah.pack()
    
    button_kembali=ctk.CTkButton(tombolPerintah, text="Kembali",command=back)
    button_kembali.grid(row=0,columns=1, padx=10, pady=15)
    
    button_pilih = ctk.CTkButton(tombolPerintah, text="Tambah", command=pilihData)
    button_pilih.grid(row=0, column=2, padx=10, pady=10)
    
    app.mainloop()
    #UI Interface
    
    return status

def pengembalianBuku(tabelPeminjaman, updateTabelData):
    
    global bukuDikembalikan
    
    def back() :
        app.destroy()
        return
    
    def updateTabelDataPeminjaman(): #Melakukan Update pada setiap data yang ada didalam data buku
        data = membacaDetailPeminjaman()
        for item in tablePeminjaman.get_children():
            tablePeminjaman.delete(item)
        for i, row in enumerate(data):
            print(data[i][0], selected_data[1])
            if (data[i][3]) == int(selected_data[1]) and data[i][2] == '1':
                tablePeminjaman.insert('', ctk.END, values=(data[i][0], data[i][1]))
    
    def on_item_selected(event):
        global bukuDikembalikan
        selected_item = tablePeminjaman.selection()[0]
        bukuDikembalikan = tablePeminjaman.item(selected_item, 'values')
        print(bukuDikembalikan)

    # Bind event untuk menangkap item yang dipilih
                    
    def updateStatusPeminjamanBuku():
        
        global bukuDikembalikan
        
        if bukuDikembalikan is None:
            messagebox.showwarning("Peringatan", "Mohon memilih buku yang akan dikembalikan")
            return
        
        id_Peminjaman = int(selected_data[1])
        print(id_Peminjaman)
        id_buku = int(bukuDikembalikan[0])
        print(id_buku)
        
        try:
            cur.execute(f"UPDATE detail_peminjaman SET status_peminjaman = '2' WHERE id_peminjaman = {id_Peminjaman} AND id_buku = {id_buku}")
            conn.commit()
            messagebox.showinfo("Sukses", "Status peminjaman buku berhasil diperbarui")
        except Exception as e:
            messagebox.showerror("Error", f"Terjadi kesalahan: {str(e)}")
        
        updateTabelDataPeminjaman()
        
        return
    
    def pengembalianTotal():
        
        id_Peminjaman = int(selected_data[1])
        
        id_anggota = membacaIDAnggota(id_Peminjaman)[0][0]
        print(id_anggota)
        print(id_Peminjaman)
        # id_buku = int(bukuDikembalikan[0])
        # print(id_buku)
        
        data = membacaDetailPeminjaman()
        
        counter = 0
        denda = 0
        
        for i, row in enumerate(data):
            if (data[i][3]) == int(selected_data[1]) and data[i][2] == '1':
                counter += 1
                        
        if counter == 0:
            tenggat_pengembalian = datetime.strptime(selected_data[3], '%Y-%m-%d')
            tanggal_sekarang = datetime.now()
            
            if tanggal_sekarang > tenggat_pengembalian:
                hariterlambat = (tanggal_sekarang - tenggat_pengembalian).days
                denda = 1000 * hariterlambat
                
                dataDendaLama = menarikDataDenda(id_anggota)
                
                    
                if dataDendaLama:
                    
                    dendabaru = dataDendaLama[1] + denda
                    
                    cur.execute(f"UPDATE data_denda SET jumlah_denda = {dendabaru} WHERE id_anggota = {id_anggota}")
                    conn.commit()
                    
                elif dataDendaLama == None:
                    
                    cur.execute(f"INSERT INTO data_denda (jumlah_denda, id_anggota, status_denda) VALUES ({denda}, {id_anggota}, '1')")
                    conn.commit()
                
            
            cur.execute(f"UPDATE peminjaman SET status_peminjaman = '2' WHERE id_peminjaman = {id_Peminjaman}")
            conn.commit()
        
        updateTabelData()
        app.destroy()
        
        return

        
    
    try:
        selected_item = tabelPeminjaman.selection()[0]
    except:
        messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
        return
    
    selected_data = tabelPeminjaman.item(selected_item, 'values')
    
    app = header()
    app.title("Pengembalian Buku")
    
    detailPeminjamanlabel = ctk.CTkLabel(app, text="Detail Peminjaman", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
    detailPeminjamanlabel.pack(padx=25, pady=15)
    
    frame = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame.pack(pady=10)
    
    # Create labels for the detail information
    id_label = ctk.CTkLabel(frame, text="ID Peminjaman:", text_color="Black")
    id_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    
    nilai_label_id = ctk.CTkLabel(frame, text=f"{selected_data[1]}", text_color="Black")
    nilai_label_id.grid(row=0, column=1, padx=10, pady=10, sticky=W)
    
    nama_label = ctk.CTkLabel(frame, text="Nama Peminjaman:", text_color="Black")
    nama_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    
    nilai_label_nama = ctk.CTkLabel(frame, text=f"{selected_data[4]}", text_color="Black")
    nilai_label_nama.grid(row=1, column=1, padx=10, pady=10, sticky=W)
    
    tanggal_label = ctk.CTkLabel(frame, text="Tanggal Peminjaman:", text_color="Black")
    tanggal_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)

    nilai_label_tanggal = ctk.CTkLabel(frame, text=f"{selected_data[2]}", text_color="Black")
    nilai_label_tanggal.grid(row=2, column=1, padx=10, pady=10, sticky=W)
    
    tenggat_label = ctk.CTkLabel(frame, text="Tenggat Pengembalian:", text_color="Black")
    tenggat_label.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    
    nilai_label_tenggat = ctk.CTkLabel(frame, text=f"{selected_data[3]}", text_color="Black")
    nilai_label_tenggat.grid(row=3, column=1, padx=10, pady=10, sticky=W)
    
    status_label = ctk.CTkLabel(frame, text="Status Peminjaman:", text_color="Black")
    status_label.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    
    judulbukudipinjam = selected_data[5]
    
    match judulbukudipinjam:
        case "1":
            judulbukudipinjam = 'Belum di Kembalikan'
        case "2":
            judulbukudipinjam = 'Sudah di Kembalikan'
            
    nilai_label_status = ctk.CTkLabel(frame, text=f"{judulbukudipinjam}", text_color="Black")
    nilai_label_status.grid(row=4, column=1, padx=10, pady=10, sticky=W)
    
    buku_label = ctk.CTkLabel(frame, text="Judul Buku:", text_color="Black")
    buku_label.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    
    frame_tombol_pengembalian = ctk.CTkFrame(frame, fg_color='#FAFAFA')
    frame_tombol_pengembalian.grid(row=5, column=1, padx=10, pady=10, sticky='nsew')
    
    bukuDikembalikan = None
    
        # Creating the table using Treeview widget
    tablePeminjaman = ttk.Treeview(frame_tombol_pengembalian, columns=('Column1', 'Column2'), show='headings', height=5)
    tablePeminjaman.heading('Column1', text='ID Buku')
    tablePeminjaman.heading('Column2', text='Judul Buku')
    tablePeminjaman.column('Column1', width=60)
    tablePeminjaman.column('Column2', width=125)
    tablePeminjaman.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')
    # tabelPeminjaman.bind('<<TreeviewSelect>>', itemTerpilih)
    tablePeminjaman.bind('<ButtonRelease-1>', on_item_selected)

    updateTabelDataPeminjaman()
    
    button_pengembalian= ctk.CTkButton(frame_tombol_pengembalian, text="Dikembalikan", command=updateStatusPeminjamanBuku)
    button_pengembalian.grid(row=1,columns=1, padx=10, pady=5)
    
    frame2 = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame2.pack(pady=0)
    
    button_kembali=ctk.CTkButton(frame2, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=1, padx=10, pady=5)
    
    button_submit= ctk.CTkButton(frame2, text="Submit", command=pengembalianTotal)
    button_submit.grid(row=0,columns=2, padx=10, pady=5)


def History():
    
    def back() :
        app.destroy()
        return
    
    def updateTabelData(): #Melakukan Update pada setiap data yang ada didalam data buku
        for item in tabelPeminjaman.get_children():
            tabelPeminjaman.delete(item)
        for i, row in enumerate(membacaPeminjaman()):
            if row[4] == '2':  # Compare id_anggota in row with the user's id_anggota
                tabelPeminjaman.insert('', ctk.END, values=(i+1, *row[:]))
    
    app = header()
    
    Historylabel = ctk.CTkLabel(app, text="History Peminjaman Buku", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
    Historylabel.pack(padx=25, pady=15)

    columns = ('#1', '#2', '#3', '#4', '#5')
    tabelPeminjaman = ttk.Treeview(app, columns=columns, show='headings')    
        
    tabelPeminjaman.heading('#1', text='No')
    tabelPeminjaman.heading('#2', text='ID Peminjaman')
    tabelPeminjaman.heading('#3', text='Tanggal Peminjaman')
    tabelPeminjaman.heading('#4', text='Tenggat Peminjaman')
    tabelPeminjaman.heading('#5', text='Nama Anggota')
    
    tabelPeminjaman.column('#1', width=60)
    tabelPeminjaman.column('#2', width=60)
    tabelPeminjaman.column('#3', width=200)
    tabelPeminjaman.column('#4', width=100)
    tabelPeminjaman.column('#5', width=100)
    
    data = membacaPeminjaman()
    
    updateTabelData()
    
    tabelPeminjaman.pack(pady=15)
                    
    frame_kembali = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_kembali.pack()

    button_kembali=ctk.CTkButton(frame_kembali, text="Kembali",command=back)
    button_kembali.grid(row=0,columns=1, padx=10, pady=15)
    
    app.mainloop()