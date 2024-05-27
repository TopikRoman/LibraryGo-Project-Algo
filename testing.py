import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def merge_sort(data, key):
    if len(data) > 1:
        mid = len(data) // 2
        left_half = data[:mid]
        right_half = data[mid:]

        merge_sort(left_half, key)
        merge_sort(right_half, key)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][key] < right_half[j][key]:
                data[k] = left_half[i]
                i += 1
            else:
                data[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            data[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            data[k] = right_half[j]
            j += 1
            k += 1

def on_item_selected(event):
    global selected_data
    selected_item = tree.selection()[0]
    selected_data = tree.item(selected_item, 'values')

def show_selected_data():
    if selected_data:
        messagebox.showinfo("Data yang Dipilih", f"Data yang dipilih: {selected_data}")
    else:
        messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")

def sort_and_display(key):
    merge_sort(data, key)
    update_treeview()

def update_treeview():
    for item in tree.get_children():
        tree.delete(item)
    for row in data:
        tree.insert('', tk.END, values=row)

# Inisialisasi variabel global untuk menyimpan data yang dipilih
selected_data = None

# Buat jendela utama
root = tk.Tk()
root.title("Tabel Pilihan dengan Tkinter")

# Buat Treeview
columns = ('#1', '#2', '#3', '#4')
tree = ttk.Treeview(root, columns=columns, show='headings')

# Tentukan heading
tree.heading('#1', text='Judul Buku')
tree.heading('#2', text='Tahun Terbit')
tree.heading('#3', text='Penerbit')
tree.heading('#4', text='ID Genre')

# Tentukan ukuran kolom
tree.column('#1', width=200)
tree.column('#2', width=100)
tree.column('#3', width=200)
tree.column('#4', width=100)

# Tambahkan data ke dalam tabel
data = [
    ('To Kill a Mockingbird', '1960', 'HarperCollins Publishers', 1),
    ('1984', '1949', 'Penguin Books', 2),
    ('Pride and Prejudice', '1813', 'Penguin Classics', 3),
    ('The Great Gatsby', '1925', 'Scribner', 1),
    ('The Catcher in the Rye', '1951', 'Little, Brown and Company', 1),
    ('The Hobbit', '1937', 'Houghton Mifflin Harcourt', 1),
    ('Fahrenheit 451', '1953', 'Simon & Schuster', 1),
    ('Brave New World', '1932', 'Harper & Brothers', 1),
    ('The Lord of the Rings', '1954', 'Allen & Unwin', 1),
    ('Animal Farm', '1945', 'Secker & Warburg', 1),
    ('The Chronicles of Narnia', '1950', 'Geoffrey Bles', 1),
    ('Jane Eyre', '1847', 'Smith, Elder & Co.', 1),
    ('Wuthering Heights', '1847', 'Thomas Cautley Newby', 1),
    ('Frankenstein', '1818', 'Lackington, Hughes, Harding, Mavor & Jones', 1),
    ('Moby-Dick', '1851', 'Richard Bentley', 1),
    ('The Picture of Dorian Gray', '1890', 'Ward, Lock and Company', 1),
    ('Dracula', '1897', 'Archibald Constable and Company', 1),
    ('The Odyssey', '8th century BC', 'Penguin Classics', 1),
    ('Romeo and Juliet', '1597', 'Penguin Classics', 1),
]

update_treeview()

# Tempatkan tombol di jendela utama
frame = tk.Frame(root)
frame.pack(pady=10)

# Tambahkan tombol untuk mengurutkan data
button_sort_judul = tk.Button(frame, text="Sortir berdasarkan Judul", command=lambda: sort_and_display(0))
button_sort_judul.grid(row=0, column=0, padx=5)

button_sort_tahun = tk.Button(frame, text="Sortir berdasarkan Tahun Terbit", command=lambda: sort_and_display(1))
button_sort_tahun.grid(row=0, column=1, padx=5)

button_sort_penerbit = tk.Button(frame, text="Sortir berdasarkan Penerbit", command=lambda: sort_and_display(2))
button_sort_penerbit.grid(row=0, column=2, padx=5)

button_sort_id_genre = tk.Button(frame, text="Sortir berdasarkan ID Genre", command=lambda: sort_and_display(3))
button_sort_id_genre.grid(row=0, column=3, padx=5)

# Tempatkan Treeview di jendela utama
tree.pack(pady=20)

# Tambahkan event binding untuk menangani pemilihan item
tree.bind('<<TreeviewSelect>>', on_item_selected)

# Buat tombol untuk menampilkan data yang dipilih
button_show = tk.Button(root, text="Tampilkan Data yang Dipilih", command=show_selected_data)
button_show.pack(pady=10)

# Jalankan aplikasi
root.mainloop()
