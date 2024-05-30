from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from lib.utils.db import menambahkanData, fetch_data, cur, conn
from lib.components.header import header

def tampilanDataBuku(Password):
    
    global selected_data
    selected_data = None
    app = header()
    
    def back() :
        nonlocal status
        status = 1

        app.destroy()

    status = 0



    def update_treeview():
        for item in tabelBuku.get_children():
            tabelBuku.delete(item)
        for row in fetch_data():
            tabelBuku.insert('', ctk.END, values=row)
    
    def delete_selected_data():
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                id_buku = selected_data[0]
                cur.execute("DELETE FROM buku WHERE id_buku = %s", (id_buku,))
                conn.commit()
                update_treeview()
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
    
    def sort_and_display(key, secondary_key=None):
        data = fetch_data()
        data = merge_sort(data, key, secondary_key)
        for item in tabelBuku.get_children():
            tabelBuku.delete(item)
        for row in data:
            tabelBuku.insert('', ctk.END, values=row)
    
    def merge_sort(data, key, secondary_key=None):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            merge_sort(left_half, key, secondary_key)
            merge_sort(right_half, key, secondary_key)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i][key] < right_half[j][key]:
                    data[k] = left_half[i]
                    i += 1
                elif left_half[i][key] > right_half[j][key]:
                    data[k] = right_half[j]
                    j += 1
                else:  # if primary keys are equal
                    if secondary_key is not None:
                        if left_half[i][secondary_key] < right_half[j][secondary_key]:
                            data[k] = left_half[i]
                            i += 1
                        else:
                            data[k] = right_half[j]
                            j += 1
                    else:
                        data[k] = left_half[i]
                        i += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1
                
        return data

    def search_book():
        search_term = inputJudulBuku.get().strip().lower()
        if search_term:
            data = fetch_data()
            merge_sort(data, 1)  # Ensure data is sorted by title before binary search
            index = binary_search(data, search_term, 1)
            if index != -1:
                tabelBuku.delete(*tabelBuku.get_children())  # Remove all existing data
                tabelBuku.insert('', 'end', values=data[index])  # Insert the searched data
            else:
                messagebox.showinfo("Hasil Pencarian", f"Buku dengan judul '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan judul buku untuk mencari.")
    
    def binary_search(data, target, key):
        low = 0
        high = len(data) - 1

        while low <= high:
            mid = (low + high) // 2
            if data[mid][key].lower() == target.lower():
                return mid
            elif data[mid][key].lower() < target.lower():
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
    def on_item_selected(event):
        global selected_data
        selected_item = tabelBuku.selection()[0]
        selected_data = tabelBuku.item(selected_item, 'values')
        print(selected_data)
    

    password = str(Password) 
    print(password)
    
    # Tampilkan tombol tambah, edit, dan hapus jika panjang password adalah 8
    global selected_data
    selected_data = None
    Window = header()
    
    columns = ('#1', '#2', '#3', '#4', '#5')
    tabelBuku = ttk.Treeview(Window, columns=columns, show='headings')

    # Tentukan heading
    tabelBuku.heading('#1', text='ID Buku')
    tabelBuku.heading('#2', text='Judul Buku')
    tabelBuku.heading('#3', text='Tahun Terbit')
    tabelBuku.heading('#4', text='Penerbit')
    tabelBuku.heading('#5', text='ID Genre')

    # Tentukan ukuran kolom
    tabelBuku.column('#1', width=50)
    tabelBuku.column('#2', width=200)
    tabelBuku.column('#3', width=100)
    tabelBuku.column('#4', width=200)
    tabelBuku.column('#5', width=100)

    data = fetch_data()
    update_treeview()

    frameTombolSorting = ctk.CTkFrame(Window, fg_color='#FAFAFA')
    frameTombolSorting.pack(pady=10)

    tombolSortingJudul = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Judul", command=lambda: sort_and_display(1))
    tombolSortingJudul.grid(row=0, column=0, padx=5)

    tombolSortingTahun = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Tahun Terbit", command=lambda: sort_and_display(2, 1))
    tombolSortingTahun.grid(row=0, column=1, padx=5)

    tombolSortingPenerbit = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan Penerbit", command=lambda: sort_and_display(3, 1))
    tombolSortingPenerbit.grid(row=0, column=2, padx=5)

    tombolSortingIdGenre = ctk.CTkButton(frameTombolSorting, text="Sortir berdasarkan ID Genre", command=lambda: sort_and_display(4, 1))
    tombolSortingIdGenre.grid(row=0, column=3, padx=5)

    frameSearching = ctk.CTkFrame(Window, fg_color='#FAFAFA')
    frameSearching.pack(pady=10)

    labelSearching = ctk.CTkLabel(frameSearching, text="Cari Judul Buku:", text_color='Black')
    labelSearching.grid(row=0, column=0, padx=5)

    inputJudulBuku = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputJudulBuku.grid(row=0, column=1, padx=5)

    # Tambahkan tombol untuk melakukan pencarian
    tombolSearching = ctk.CTkButton(frame_search, text="Cari", command=search_book)
    tombolSearching.grid(row=0, column=2, padx=5)

    # Tempatkan Treeview di jendela utama
    tree.pack(pady=15)

    # Tambahkan event binding untuk menangani pemilihan item
    tabelBuku.bind('<<TreeviewSelect>>', on_item_selected)
    
    if len(password) > 6:
        frame_actions = ctk.CTkFrame(app, fg_color='#FAFAFA')
        frame_actions.pack()

        # Tambahkan tombol untuk mengedit data
        button_edit = ctk.CTkButton(frame_actions, text="Edit", command=open_edit_window)
        button_edit.grid(row=0, column=0, padx=5,pady=5)

        # Tambahkan tombol untuk menambah data
        button_add = ctk.CTkButton(frame_actions, text="Tambah", command=tambahBuku)
        button_add.grid(row=0, column=1, padx=5)

        # Tambahkan tombol untuk menghapus data
        button_delete = ctk.CTkButton(frame_actions, text="Hapus", command=delete_selected_data)
        button_delete.grid(row=0, column=2, padx=5)

        button_kembali=ctk.CTkButton(frame_actions, text="Kembali",command=back)
        button_kembali.grid(row=1,columns=3, padx=5)

    app.mainloop()
    
    return status



def tambahBuku():
    def back() :
        app.destroy()
        return

    def uploadDataBuku():
        namaTabel = "buku"
        namaKolom = "judul_buku, tahun_terbit, penerbit, id_genre"
        QueryInput = []
        
        QueryInput.append(judulBuku.get())
        QueryInput.append(tahunPenerbit.get())
        QueryInput.append(Penerbit.get())
        Genre = genreBuku.get()
        
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

    app = header()
    
    tambahDatabukuLabel = ctk.CTkLabel(app, text="LiGO", font=("Helvetica", 45), text_color="Black")
    tambahDatabukuLabel.pack(padx=50, pady=25)

    # Creating the frame
    tambahDatabukuFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    tambahDatabukuFrame.pack(padx=10, pady=10)

    # Creating the label
    judulBuku = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Judulnya")
    judulBuku.pack(padx=10, pady=10)

    # Creating inputJudulBuku
    tahunPenerbit = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan tahun penerbit")
    tahunPenerbit.pack(padx=10, pady=1)

    Penerbit = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Penerbitnya")
    Penerbit.pack(padx=10, pady=10)

    genreBuku = ctk.CTkComboBox(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', values=["Fiksi", "Non-Fiksi", "Sains", "Biografi", "Sejarah"], corner_radius=50)
    genreBuku.pack(padx=10, pady=10)

    submitData = ctk.CTkButton(app, text="Submit", fg_color='#FF3399', text_color='Black', corner_radius=50, command=uploadDataBuku)
    submitData.pack(padx=10, pady=10)
    
    Keluar = ctk.CTkButton(app, text="Kembali", fg_color='#FF3399', text_color='Black', corner_radius=50, command=back)
    Keluar.pack(padx=10, pady=10)
    
    app.mainloop()
    
def open_edit_window():
    def back() :
        app.destroy()
        return
    def save_edit():
        id_buku = selected_data[0]
        new_data = (entry_judul.get(), entry_tahun.get(), entry_penerbit.get(), pilih_genre(entry_genre.get(), '2'))
        cur.execute("UPDATE buku SET judul_buku = %s, tahun_terbit = %s, penerbit = %s, id_genre = %s WHERE id_buku = %s", (*new_data, id_buku))
        conn.commit()
        app.destroy()
        
    if selected_data:
        
        app = header()
        
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
        submit_button.pack(padx=5,pady=2)

        button_kembali=ctk.CTkButton(app, text="Kembali",command=back)
        button_kembali.pack(padx=5,pady=2)

    else:
        messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
        
    app.mainloop()
    

def pilih_genre(genre, status):
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



