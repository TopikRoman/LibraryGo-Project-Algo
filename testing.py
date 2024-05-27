# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# def merge_sort(data, key, secondary_key=None):
#     if len(data) > 1:
#         mid = len(data) // 2
#         left_half = data[:mid]
#         right_half = data[mid:]

#         merge_sort(left_half, key, secondary_key)
#         merge_sort(right_half, key, secondary_key)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i][key] < right_half[j][key]:
#                 data[k] = left_half[i]
#                 i += 1
#             elif left_half[i][key] > right_half[j][key]:
#                 data[k] = right_half[j]
#                 j += 1
#             else:  # if primary keys are equal
#                 if secondary_key is not None:
#                     if left_half[i][secondary_key] < right_half[j][secondary_key]:
#                         data[k] = left_half[i]
#                         i += 1
#                     else:
#                         data[k] = right_half[j]
#                         j += 1
#                 else:
#                     data[k] = left_half[i]
#                     i += 1
#             k += 1

#         while i < len(left_half):
#             data[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             data[k] = right_half[j]
#             j += 1
#             k += 1

# def on_item_selected(event):
#     global selected_data
#     selected_item = tree.selection()[0]
#     selected_data = tree.item(selected_item, 'values')

# def show_selected_data():
#     if selected_data:
#         messagebox.showinfo("Data yang Dipilih", f"Data yang dipilih: {selected_data}")
#     else:
#         messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")

# def sort_and_display(key, secondary_key=None):
#     merge_sort(data, key, secondary_key)
#     update_treeview()

# def update_treeview():
#     for item in tree.get_children():
#         tree.delete(item)
#     for row in data:
#         tree.insert('', tk.END, values=row)

# # Inisialisasi variabel global untuk menyimpan data yang dipilih
# selected_data = None

# # Buat jendela utama
# root = tk.Tk()
# root.title("Tabel Pilihan dengan Tkinter")

# # Buat Treeview
# columns = ('#1', '#2', '#3', '#4')
# tree = ttk.Treeview(root, columns=columns, show='headings')

# # Tentukan heading
# tree.heading('#1', text='Judul Buku')
# tree.heading('#2', text='Tahun Terbit')
# tree.heading('#3', text='Penerbit')
# tree.heading('#4', text='ID Genre')

# # Tentukan ukuran kolom
# tree.column('#1', width=200)
# tree.column('#2', width=100)
# tree.column('#3', width=200)
# tree.column('#4', width=100)

# # Tambahkan data ke dalam tabel
# data = [
#     ('To Kill a Mockingbird', '1960', 'HarperCollins Publishers', 1),
#     ('1984', '1949', 'Penguin Books', 2),
#     ('Pride and Prejudice', '1813', 'Penguin Classics', 3),
#     ('The Great Gatsby', '1925', 'Scribner', 1),
#     ('The Catcher in the Rye', '1951', 'Little, Brown and Company', 1),
#     ('The Hobbit', '1937', 'Houghton Mifflin Harcourt', 1),
#     ('Fahrenheit 451', '1953', 'Simon & Schuster', 1),
#     ('Brave New World', '1932', 'Harper & Brothers', 1),
#     ('The Lord of the Rings', '1954', 'Allen & Unwin', 1),
#     ('Animal Farm', '1945', 'Secker & Warburg', 1),
#     ('The Chronicles of Narnia', '1950', 'Geoffrey Bles', 1),
#     ('Jane Eyre', '1847', 'Smith, Elder & Co.', 1),
#     ('Wuthering Heights', '1847', 'Thomas Cautley Newby', 1),
#     ('Frankenstein', '1818', 'Lackington, Hughes, Harding, Mavor & Jones', 1),
#     ('Moby-Dick', '1851', 'Richard Bentley', 1),
#     ('The Picture of Dorian Gray', '1890', 'Ward, Lock and Company', 1),
#     ('Dracula', '1897', 'Archibald Constable and Company', 1),
#     ('The Odyssey', '8th century BC', 'Penguin Classics', 1),
#     ('Romeo and Juliet', '1597', 'Penguin Classics', 1),
# ]

# update_treeview()

# # Tempatkan tombol di jendela utama
# frame = tk.Frame(root)
# frame.pack(pady=10)

# # Tambahkan tombol untuk mengurutkan data
# button_sort_judul = tk.Button(frame, text="Sortir berdasarkan Judul", command=lambda: sort_and_display(0))
# button_sort_judul.grid(row=0, column=0, padx=5)

# button_sort_tahun = tk.Button(frame, text="Sortir berdasarkan Tahun Terbit", command=lambda: sort_and_display(1, 0))
# button_sort_tahun.grid(row=0, column=1, padx=5)

# button_sort_penerbit = tk.Button(frame, text="Sortir berdasarkan Penerbit", command=lambda: sort_and_display(2, 0))
# button_sort_penerbit.grid(row=0, column=2, padx=5)

# button_sort_id_genre = tk.Button(frame, text="Sortir berdasarkan ID Genre", command=lambda: sort_and_display(3, 0))
# button_sort_id_genre.grid(row=0, column=3, padx=5)

# # Tempatkan Treeview di jendela utama
# tree.pack(pady=20)

# # Tambahkan event binding untuk menangani pemilihan item
# tree.bind('<<TreeviewSelect>>', on_item_selected)

# # Buat tombol untuk menampilkan data yang dipilih
# button_show = tk.Button(root, text="Tampilkan Data yang Dipilih", command=show_selected_data)
# button_show.pack(pady=10)

# # Jalankan aplikasi
# root.mainloop()


# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox

# def merge_sort(data, key, secondary_key=None):
#     if len(data) > 1:
#         mid = len(data) // 2
#         left_half = data[:mid]
#         right_half = data[mid:]

#         merge_sort(left_half, key, secondary_key)
#         merge_sort(right_half, key, secondary_key)

#         i = j = k = 0

#         while i < len(left_half) and j < len(right_half):
#             if left_half[i][key] < right_half[j][key]:
#                 data[k] = left_half[i]
#                 i += 1
#             elif left_half[i][key] > right_half[j][key]:
#                 data[k] = right_half[j]
#                 j += 1
#             else:  # if primary keys are equal
#                 if secondary_key is not None:
#                     if left_half[i][secondary_key] < right_half[j][secondary_key]:
#                         data[k] = left_half[i]
#                         i += 1
#                     else:
#                         data[k] = right_half[j]
#                         j += 1
#                 else:
#                     data[k] = left_half[i]
#                     i += 1
#             k += 1

#         while i < len(left_half):
#             data[k] = left_half[i]
#             i += 1
#             k += 1

#         while j < len(right_half):
#             data[k] = right_half[j]
#             j += 1
#             k += 1

# def binary_search(data, target, key):
#     low = 0
#     high = len(data) - 1

#     while low <= high:
#         mid = (low + high) // 2
#         if data[mid][key] == target:
#             return mid
#         elif data[mid][key] < target:
#             low = mid + 1
#         else:
#             high = mid - 1

#     return -1

# def on_item_selected(event):
#     global selected_data
#     selected_item = tree.selection()[0]
#     selected_data = tree.item(selected_item, 'values')

# def show_selected_data():
#     if selected_data:
#         messagebox.showinfo("Data yang Dipilih", f"Data yang dipilih: {selected_data}")
#     else:
#         messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")

# def sort_and_display(key, secondary_key=None):
#     merge_sort(data, key, secondary_key)
#     update_treeview()

# def update_treeview():
#     for item in tree.get_children():
#         tree.delete(item)
#     for row in data:
#         tree.insert('', tk.END, values=row)

# def search_book():
#     search_term = entry.get().strip()
#     if search_term:
#         sort_and_display(0)  # Ensure data is sorted by title before binary search
#         index = binary_search(data, search_term, 0)
#         if index != -1:
#             tree.selection_set(tree.get_children()[index])
#             tree.see(tree.get_children()[index])
#         else:
#             messagebox.showinfo("Hasil Pencarian", f"Buku dengan judul '{search_term}' tidak ditemukan.")
#     else:
#         messagebox.showwarning("Peringatan", "Harap masukkan judul buku untuk mencari.")

# # Inisialisasi variabel global untuk menyimpan data yang dipilih
# selected_data = None

# # Buat jendela utama
# root = tk.Tk()
# root.title("Tabel Pilihan dengan Tkinter")

# # Buat Treeview
# columns = ('#1', '#2', '#3', '#4')
# tree = ttk.Treeview(root, columns=columns, show='headings')

# # Tentukan heading
# tree.heading('#1', text='Judul Buku')
# tree.heading('#2', text='Tahun Terbit')
# tree.heading('#3', text='Penerbit')
# tree.heading('#4', text='ID Genre')

# # Tentukan ukuran kolom
# tree.column('#1', width=200)
# tree.column('#2', width=100)
# tree.column('#3', width=200)
# tree.column('#4', width=100)

# # Tambahkan data ke dalam tabel
# data = [
#     ('To Kill a Mockingbird', '1960', 'HarperCollins Publishers', 1),
#     ('1984', '1949', 'Penguin Books', 2),
#     ('Pride and Prejudice', '1813', 'Penguin Classics', 3),
#     ('The Great Gatsby', '1925', 'Scribner', 1),
#     ('The Catcher in the Rye', '1951', 'Little, Brown and Company', 1),
#     ('The Hobbit', '1937', 'Houghton Mifflin Harcourt', 1),
#     ('Fahrenheit 451', '1953', 'Simon & Schuster', 1),
#     ('Brave New World', '1932', 'Harper & Brothers', 1),
#     ('The Lord of the Rings', '1954', 'Allen & Unwin', 1),
#     ('Animal Farm', '1945', 'Secker & Warburg', 1),
#     ('The Chronicles of Narnia', '1950', 'Geoffrey Bles', 1),
#     ('Jane Eyre', '1847', 'Smith, Elder & Co.', 1),
#     ('Wuthering Heights', '1847', 'Thomas Cautley Newby', 1),
#     ('Frankenstein', '1818', 'Lackington, Hughes, Harding, Mavor & Jones', 1),
#     ('Moby-Dick', '1851', 'Richard Bentley', 1),
#     ('The Picture of Dorian Gray', '1890', 'Ward, Lock and Company', 1),
#     ('Dracula', '1897', 'Archibald Constable and Company', 1),
#     ('The Odyssey', '8th century BC', 'Penguin Classics', 1),
#     ('Romeo and Juliet', '1597', 'Penguin Classics', 1),
# ]

# update_treeview()

# # Tempatkan frame untuk tombol-tombol sorting dan pencarian
# frame_buttons = tk.Frame(root)
# frame_buttons.pack(pady=10)

# # Tambahkan tombol untuk mengurutkan data
# button_sort_judul = tk.Button(frame_buttons, text="Sortir berdasarkan Judul", command=lambda: sort_and_display(0))
# button_sort_judul.grid(row=0, column=0, padx=5)

# button_sort_tahun = tk.Button(frame_buttons, text="Sortir berdasarkan Tahun Terbit", command=lambda: sort_and_display(1, 0))
# button_sort_tahun.grid(row=0, column=1, padx=5)

# button_sort_penerbit = tk.Button(frame_buttons, text="Sortir berdasarkan Penerbit", command=lambda: sort_and_display(2, 0))
# button_sort_penerbit.grid(row=0, column=2, padx=5)

# button_sort_id_genre = tk.Button(frame_buttons, text="Sortir berdasarkan ID Genre", command=lambda: sort_and_display(3, 0))
# button_sort_id_genre.grid(row=0, column=3, padx=5)

# # Tempatkan frame untuk entry dan tombol pencarian
# frame_search = tk.Frame(root)
# frame_search.pack(pady=10)

# # Tambahkan entry box untuk pencarian
# entry_label = tk.Label(frame_search, text="Cari Judul Buku:")
# entry_label.grid(row=0, column=0, padx=5)

# entry = tk.Entry(frame_search)
# entry.grid(row=0, column=1, padx=5)

# # Tambahkan tombol untuk melakukan pencarian
# button_search = tk.Button(frame_search, text="Cari", command=search_book)
# button_search.grid(row=0, column=2, padx=5)

# # Tempatkan Treeview di jendela utama
# tree.pack(pady=20)

# # Tambahkan event binding untuk menangani pemilihan item
# tree.bind('<<TreeviewSelect>>', on_item_selected)

# # Buat tombol untuk menampilkan data yang dipilih
# button_show = tk.Button(root, text="Tampilkan Data yang Dipilih", command=show_selected_data)
# button_show.pack(pady=10)

# # Jalankan aplikasi
# root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2

# Koneksi ke database
conn = psycopg2.connect(
    dbname="LibraryGo",
    user="postgres",
    password="19Januari",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def fetch_data():
    cur.execute("SELECT * FROM buku")
    rows = cur.fetchall()
    return rows

def update_treeview():
    for item in tree.get_children():
        tree.delete(item)
    for row in fetch_data():
        tree.insert('', tk.END, values=row)

def open_add_window():
    def save_add():
        judul = entry_judul.get()
        tahun = entry_tahun.get()
        penerbit = entry_penerbit.get()
        genre = entry_genre.get()
        menambahkanData("buku", "judul_buku, tahun_terbit, penerbit, id_genre", f"('{judul}', '{tahun}', '{penerbit}', {genre})")
        update_treeview()
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Tambah Data Buku")

    tk.Label(add_window, text="Judul Buku").grid(row=0, column=0, padx=5, pady=5)
    tk.Label(add_window, text="Tahun Terbit").grid(row=1, column=0, padx=5, pady=5)
    tk.Label(add_window, text="Penerbit").grid(row=2, column=0, padx=5, pady=5)
    tk.Label(add_window, text="ID Genre").grid(row=3, column=0, padx=5, pady=5)

    entry_judul = tk.Entry(add_window)
    entry_judul.grid(row=0, column=1, padx=5, pady=5)

    entry_tahun = tk.Entry(add_window)
    entry_tahun.grid(row=1, column=1, padx=5, pady=5)

    entry_penerbit = tk.Entry(add_window)
    entry_penerbit.grid(row=2, column=1, padx=5, pady=5)

    entry_genre = tk.Entry(add_window)
    entry_genre.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(add_window, text="Simpan", command=save_add).grid(row=4, column=0, columnspan=2, pady=10)

def open_edit_window():
    if selected_data:
        edit_window = tk.Toplevel(root)
        edit_window.title("Edit Data Buku")

        tk.Label(edit_window, text="Judul Buku").grid(row=0, column=0, padx=5, pady=5)
        tk.Label(edit_window, text="Tahun Terbit").grid(row=1, column=0, padx=5, pady=5)
        tk.Label(edit_window, text="Penerbit").grid(row=2, column=0, padx=5, pady=5)
        tk.Label(edit_window, text="ID Genre").grid(row=3, column=0, padx=5, pady=5)

        entry_judul = tk.Entry(edit_window)
        entry_judul.grid(row=0, column=1, padx=5, pady=5)
        entry_judul.insert(0, selected_data[1])

        entry_tahun = tk.Entry(edit_window)
        entry_tahun.grid(row=1, column=1, padx=5, pady=5)
        entry_tahun.insert(0, selected_data[2])

        entry_penerbit = tk.Entry(edit_window)
        entry_penerbit.grid(row=2, column=1, padx=5, pady=5)
        entry_penerbit.insert(0, selected_data[3])

        entry_genre = tk.Entry(edit_window)
        entry_genre.grid(row=3, column=1, padx=5, pady=5)
        entry_genre.insert(0, selected_data[4])

        def save_edit():
            id_buku = selected_data[0]
            new_data = (entry_judul.get(), entry_tahun.get(), entry_penerbit.get(), int(entry_genre.get()))
            cur.execute("UPDATE buku SET judul_buku = %s, tahun_terbit = %s, penerbit = %s, id_genre = %s WHERE id_buku = %s", (*new_data, id_buku))
            conn.commit()
            update_treeview()
            edit_window.destroy()

        tk.Button(edit_window, text="Simpan", command=save_edit).grid(row=4, column=0, columnspan=2, pady=10)
    else:
        messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")

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

def menambahkanData(namaTabel, namaKolom, values):
    cur.execute("INSERT INTO " + namaTabel + " " + f'({namaKolom})' + " VALUES " + f'{values}'.replace("[", "(").replace("]", ")"))
    conn.commit()
    return

def on_item_selected(event):
    global selected_data
    selected_item = tree.selection()[0]
    selected_data = tree.item(selected_item, 'values')

def sort_and_display(key, secondary_key=None):
    data = fetch_data()
    merge_sort(data, key, secondary_key)
    for item in tree.get_children():
        tree.delete(item)
    for row in data:
        tree.insert('', tk.END, values=row)

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

# Inisialisasi variabel global untuk menyimpan data yang dipilih
selected_data = None

# Buat jendela utama
root = tk.Tk()
root.title("Tabel Pilihan dengan Tkinter")

# Buat Treeview
columns = ('#1', '#2', '#3', '#4', '#5')
tree = ttk.Treeview(root, columns=columns, show='headings')

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
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

# Tambahkan tombol untuk mengurutkan data
button_sort_judul = tk.Button(frame_buttons, text="Sortir berdasarkan Judul", command=lambda: sort_and_display(1))
button_sort_judul.grid(row=0, column=0, padx=5)

button_sort_tahun = tk.Button(frame_buttons, text="Sortir berdasarkan Tahun Terbit", command=lambda: sort_and_display(2, 1))
button_sort_tahun.grid(row=0, column=1, padx=5)

button_sort_penerbit = tk.Button(frame_buttons, text="Sortir berdasarkan Penerbit", command=lambda: sort_and_display(3, 1))
button_sort_penerbit.grid(row=0, column=2, padx=5)

button_sort_id_genre = tk.Button(frame_buttons, text="Sortir berdasarkan ID Genre", command=lambda: sort_and_display(4, 1))
button_sort_id_genre.grid(row=0, column=3, padx=5)

# Tempatkan frame untuk entry dan tombol pencarian
frame_search = tk.Frame(root)
frame_search.pack(pady=10)

# Tambahkan entry box untuk pencarian
entry_label = tk.Label(frame_search, text="Cari Judul Buku:")
entry_label.grid(row=0, column=0, padx=5)

entry = tk.Entry(frame_search)
entry.grid(row=0, column=1, padx=5)

# Tambahkan tombol untuk melakukan pencarian
button_search = tk.Button(frame_search, text="Cari", command=search_book)
button_search.grid(row=0, column=2, padx=5)

# Tempatkan Treeview di jendela utama
tree.pack(pady=20)

# Tambahkan event binding untuk menangani pemilihan item
tree.bind('<<TreeviewSelect>>', on_item_selected)

# Tempatkan frame untuk tombol aksi
frame_actions = tk.Frame(root)
frame_actions.pack(pady=10)

# Tambahkan tombol untuk mengedit data
button_edit = tk.Button(frame_actions, text="Edit", command=open_edit_window)
button_edit.grid(row=0, column=0, padx=5)

# Tambahkan tombol untuk menambah data
button_add = tk.Button(frame_actions, text="Tambah", command=open_add_window)
button_add.grid(row=0, column=1, padx=5)

# Tambahkan tombol untuk menghapus data
button_delete = tk.Button(frame_actions, text="Hapus", command=delete_selected_data)
button_delete.grid(row=0, column=2, padx=5)

# Jalankan aplikasi
root.mainloop()
