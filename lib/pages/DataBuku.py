from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from lib.utils.db import menambahkanData, fetch_data, cur, conn
from lib.utils.algoritma import merge_sort, dynamic_binary_search
from lib.components.header import header

    
def tampilanDataBuku(akun):
    
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
        data = fetch_data("buku")
        for item in tabelBuku.get_children():
            tabelBuku.delete(item)
        for i, row in enumerate(data, start=1):
            tabelBuku.insert('', ctk.END, values=(i, *row[:]))
    
    def hapusDataTerpilih(): #Menghapus data yang telah dipilih oleh user
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                id_buku = selected_data[1]
                cur.execute("DELETE FROM buku WHERE id_buku = %s", (id_buku,))
                conn.commit()
                updateTabelData()
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
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
    
    
    selected_data = None #Variabel untuk menampung nilai/data buku yang dipilih oleh user
    
    
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
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)
    
    if akun[0][1] == 2 or akun[0][1] == 1:

        button_edit = ctk.CTkButton(tombolPerintah, text="Edit", command=lambda: windowEditBuku(updateTabelData))
        button_edit.grid(row=0, column=0, padx=10, pady=10)
        
        button_add = ctk.CTkButton(tombolPerintah, text="Tambah", command=lambda: windowTambahBuku(updateTabelData))
        button_add.grid(row=0, column=1, padx=10, pady=10)

        button_delete = ctk.CTkButton(tombolPerintah, text="Hapus", command=hapusDataTerpilih)
        button_delete.grid(row=0, column=2, padx=10, pady=10)

    app.mainloop()
    #UI Interface
    
    return status

def windowEditBuku(updateTabelData): #Jendela Edit Buku
    
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


def windowTambahBuku(updateTabelData): # Jendela Tambah Buku
    
    #Fungsi Pendukung dalam Jendela
    def back() :
        app.destroy()
        return

    def focus_next_widget(event):
        event.widget.tk_focusNext().focus()
        return("break")
    #Fungsi Pendukung dalam Jendela
    
    
    #Penghubung / Input kedalam Database
    def menambahDatabaseBuku():
        namaTabel = "buku"
        namaKolom = "judul_buku, tahun_terbit, penerbit, id_genre"
        QueryInput = []
        
        for i, entry in enumerate(entries):
            if isinstance(entry, ctk.CTkComboBox):
                value = entry.get()
            else:
                value = entry.get().strip()
            
            if not value:
                messagebox.showerror("Error", "Data tidak lengkap")
                app.destroy()
                return
            
            if i == 1:
                if not value.isdigit() or len(value) != 4:
                    messagebox.showerror("Error", "Masukkan tahun terbit dengan benar")
                    app.destroy()
                    return
                
        QueryInput.append(entries[0].get().capitalize())
        QueryInput.append(entries[1].get())
        QueryInput.append(entries[2].get())
        Genre = entries[3].get()
        
        match Genre:
            case "Fiksi":
                QueryInput.append(1)
            case "Non-Fiksi":
                QueryInput.append(2)
            case "Sains":
                QueryInput.append(3)
            case "Biografi":
                QueryInput.append(4)
            case "Sejarah":
                QueryInput.append(5)
                
        menambahkanData(namaTabel, namaKolom, QueryInput)
        messagebox.showinfo("Success", "Data Berhasil")
        
        updateTabelData()
        app.destroy()
        
        return
    #Penghubung / Input kedalam Database


    #UI Interface
    app = header()
    
    tambahDatabukuLabel = ctk.CTkLabel(app, text="Tambah Data Buku\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 45), text_color="Black")
    tambahDatabukuLabel.pack(padx=50, pady=25)

    tambahDatabukuFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    tambahDatabukuFrame.pack(padx=10, pady=10)

    labels = ["Judul Buku", "Tahun Terbit", "Penerbit", "Genre"]
    entries = []

    for i, text in enumerate(labels):
        label = ctk.CTkLabel(tambahDatabukuFrame, text=text, text_color='Black')
        label.grid(row=i, column=0, padx=5, pady=5, sticky='e')

        if text == "Genre":
            entry = ctk.CTkComboBox(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', values=["Fiksi", "Non-Fiksi", "Sains", "Biografi", "Sejarah"], corner_radius=50)
        else :
            entry = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text=text)
            entry.bind("<Return>", focus_next_widget)

        entry.grid(row=i, column=1, padx=10, pady=10, sticky='w')
        entries.append(entry)

    frame_action = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    frame_action.pack(padx=10, pady=10)
    
    submitData = ctk.CTkButton(frame_action, text="Submit", command=menambahDatabaseBuku)
    submitData.grid(row=0, column=0, padx=10, pady=10)
    
    Keluar = ctk.CTkButton(frame_action, text="Kembali", command=back)
    Keluar.grid(row=0, column=1, padx=10, pady=10)
    
    app.mainloop()
    #UI Interface
    
    return


def pilihGenre(genre, status):
    match status:
        case '1':
            match genre:
                case '1':
                    genre = "Fiksi"
                case '2':
                    genre = "Non-Fiksi"
                case '3':
                    genre = "Sains"
                case '4':
                    genre = "Biografi"
                case '5':
                    genre = "Sejarah"
        case '2':
            match genre:
                case 'Fiksi':
                    genre = 1
                case 'Non-Fiksi':
                    genre = 2
                case 'Sains':
                    genre = 3
                case 'Biografi':
                    genre = 4
                case 'Sejarah':
                    genre = 5
    return genre




