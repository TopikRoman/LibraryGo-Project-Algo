from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from lib.utils.db import menambahkanData, fetch_data
from lib.components.header import header

def tampilanDataBuku():
    
    app = header()
    
    def update_treeview():
        for item in tree.get_children():
            tree.delete(item)
        for row in fetch_data():
            tree.insert('', ctk.END, values=row)
    
    def on_item_selected(event):
        global selected_data
        selected_item = tree.selection()[0]
        selected_data = tree.item(selected_item, 'values')
    
    def sort_and_display(key, secondary_key=None):
        data = fetch_data()
        data = merge_sort(data, key, secondary_key)
        for item in tree.get_children():
            tree.delete(item)
        for row in data:
            tree.insert('', ctk.END, values=row)

    def search_book():
        search_term = entry.get().strip()
        if search_term:
            data = fetch_data()
            merge_sort(data, 1)  # Ensure data is sorted by title before binary search
            index = binary_search(data, search_term, 1)
            if index != -1:
                tree.selection_set(tree.get_children()[index])
                tree.see(tree.get_children()[index])
            else:
                messagebox.showinfo("Hasil Pencarian", f"Buku dengan judul '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan judul buku untuk mencari.")

    
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

    
    columns = ('#1', '#2', '#3', '#4', '#5')
    tree = ttk.Treeview(app, columns=columns, show='headings')

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

    # Tambahkan data ke dalam tabel
    data = fetch_data()
    update_treeview()

    # Tempatkan frame untuk tombol-tombol sorting dan pencarian
    frame_buttons = ctk.CTkFrame(app, fg_color='#FAFAFA')
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
    frame_search = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_search.pack(pady=10)

    # Tambahkan entry box untuk pencarian
    entry_label = ctk.CTkLabel(frame_search, text="Cari Judul Buku:", text_color='Black')
    entry_label.grid(row=0, column=0, padx=5)

    entry = ctk.CTkEntry(frame_search, fg_color='#FAFAFA', text_color='Black')
    entry.grid(row=0, column=1, padx=5)

    # Tambahkan tombol untuk melakukan pencarian
    button_search = ctk.CTkButton(frame_search, text="Cari", command=search_book)
    button_search.grid(row=0, column=2, padx=5)

    # Tempatkan Treeview di jendela utama
    tree.pack(pady=20)

    # Tambahkan event binding untuk menangani pemilihan item
    tree.bind('<<TreeviewSelect>>', on_item_selected)

    # Tempatkan frame untuk tombol aksi
    frame_actions = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_actions.pack(pady=10)

    # Tambahkan tombol untuk mengedit data
    button_edit = ctk.CTkButton(frame_actions, text="Edit", command=open_edit_window)
    button_edit.grid(row=0, column=0, padx=5)

    # Tambahkan tombol untuk menambah data
    button_add = ctk.CTkButton(frame_actions, text="Tambah", command=tambahBuku)
    button_add.grid(row=0, column=1, padx=5)

    # Tambahkan tombol untuk menghapus data
    button_delete = ctk.CTkButton(frame_actions, text="Hapus")
    button_delete.grid(row=0, column=2, padx=5)
    
    app.mainloop()



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

    # Creating entry
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
    if selected_data:
        
        app = header()
        
        ctk.CTkLabel(app, text="Edit Data Buku", font=("Helvetica", 25), text_color="Black").pack(padx=25, pady=15)

        frameEdit = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        frameEdit.pack(padx=10, pady=10)
        
        ctk.CTkLabel(frameEdit, text="Judul Buku").pack(padx=5, pady=5)
        ctk.CTkLabel(frameEdit, text="Tahun Terbit").pack(padx=5, pady=5)
        ctk.CTkLabel(frameEdit, text="Penerbit").pack(padx=5, pady=5)
        ctk.CTkLabel(frameEdit, text="ID Genre").pack(padx=5, pady=5)

        entry_judul = ctk.CTkEntry(frameEdit)
        entry_judul.pack(row=0, column=1, padx=5, pady=5)
        entry_judul.insert(0, selected_data[1])

        entry_tahun = ctk.CTkEntry(frameEdit)
        entry_tahun.pack(row=1, column=1, padx=5, pady=5)
        entry_tahun.insert(0, selected_data[2])

        entry_penerbit = ctk.CTkEntry(frameEdit)
        entry_penerbit.pack(row=2, column=1, padx=5, pady=5)
        entry_penerbit.insert(0, selected_data[3])

        entry_genre = ctk.CTkEntry(frameEdit)
        entry_genre.pack(row=3, column=1, padx=5, pady=5)
        entry_genre.insert(0, selected_data[4])

        def save_edit():
            id_buku = selected_data[0]
            new_data = (entry_judul.get(), entry_tahun.get(), entry_penerbit.get(), int(entry_genre.get()))
            cur.execute("UPDATE buku SET judul_buku = %s, tahun_terbit = %s, penerbit = %s, id_genre = %s WHERE id_buku = %s", (*new_data, id_buku))
            conn.commit()
            update_treeview()
            frameEdit.destroy()

        ctk.CTkButton(frameEdit, text="Simpan", command=save_edit).grid(row=4, column=0, columnspan=2, pady=10)
    else:
        messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")



