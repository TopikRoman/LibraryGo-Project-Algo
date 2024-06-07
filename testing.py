import tkinter as tk
from tkinter import ttk, messagebox

def open_anggota_form():
    global tree_anggota, anggota_window
    anggota_window = tk.Toplevel(root)
    anggota_window.title("Data Anggota Perpustakaan")

    columns = ("ID", "Nama", "Alamat")
    tree_anggota = ttk.Treeview(anggota_window, columns=columns, show="headings")
    for col in columns:
        tree_anggota.heading(col, text=col)

    # Sample data
    data_anggota = [
        (1, "John Doe", "123 Street A"),
        (2, "Jane Smith", "456 Street B"),
        (3, "Michael Johnson", "789 Street C")
    ]

    for item in data_anggota:
        tree_anggota.insert("", "end", values=item)

    tree_anggota.pack(padx=10, pady=10)

    button_pilih_anggota = tk.Button(anggota_window, text="Pilih", command=pilih_anggota)
    button_pilih_anggota.pack(pady=10)

def pilih_anggota():
    selected_item = tree_anggota.selection()
    if selected_item:
        selected_values = tree_anggota.item(selected_item, "values")
        entry_nama.delete(0, tk.END)
        entry_nama.insert(0, selected_values[1])
        anggota_window.destroy()
    else:
        messagebox.showwarning("Peringatan", "Pilih salah satu anggota!")

def open_buku_form():
    global tree_buku, buku_window
    buku_window = tk.Toplevel(root)
    buku_window.title("Data Buku Perpustakaan")

    columns = ("ID", "Judul", "Penulis")
    tree_buku = ttk.Treeview(buku_window, columns=columns, show="headings", selectmode="extended")
    for col in columns:
        tree_buku.heading(col, text=col)

    # Sample data
    data_buku = [
        (1, "The Great Gatsby", "F. Scott Fitzgerald"),
        (2, "To Kill a Mockingbird", "Harper Lee"),
        (3, "1984", "George Orwell")
    ]

    for item in data_buku:
        tree_buku.insert("", "end", values=item)

    tree_buku.pack(padx=10, pady=10)

    button_pilih_buku = tk.Button(buku_window, text="Pilih", command=pilih_buku)
    button_pilih_buku.pack(pady=10)

def pilih_buku():
    selected_items = tree_buku.selection()
    if selected_items:
        for item in selected_items:
            selected_values = tree_buku.item(item, "values")
            buku_str = f"{selected_values[1]} by {selected_values[2]}"
            if buku_str not in listbox_buku.get(0, tk.END):
                listbox_buku.insert(tk.END, buku_str)
        buku_window.destroy()
    else:
        messagebox.showwarning("Peringatan", "Pilih minimal satu buku!")

def hapus_buku():
    selected_buku_index = listbox_buku.curselection()
    if selected_buku_index:
        listbox_buku.delete(selected_buku_index)
    else:
        messagebox.showwarning("Peringatan", "Pilih buku yang ingin dihapus!")

def simpan_peminjaman():
    nama_peminjam = entry_nama.get()
    buku_dipinjam = listbox_buku.get(0, tk.END)
    if not nama_peminjam:
        messagebox.showwarning("Peringatan", "Nama peminjam tidak boleh kosong!")
    elif not buku_dipinjam:
        messagebox.showwarning("Peringatan", "Buku yang dipinjam tidak boleh kosong!")
    else:
        # Simpan data peminjaman (contoh sederhana dengan print)
        print(f"Nama Peminjam: {nama_peminjam}")
        print("Buku yang Dipinjam:")
        for buku in buku_dipinjam:
            print(f"- {buku}")
        messagebox.showinfo("Informasi", "Data peminjaman berhasil disimpan!")

root = tk.Tk()
root.title("Form Tambah Data Peminjaman")

# Form Peminjaman
label_nama = tk.Label(root, text="Nama Peminjam:")
label_nama.grid(row=0, column=0, padx=10, pady=10)
entry_nama = tk.Entry(root)
entry_nama.grid(row=0, column=1, padx=10, pady=10)
button_cari_anggota = tk.Button(root, text="Cari Anggota", command=open_anggota_form)
button_cari_anggota.grid(row=0, column=2, padx=10, pady=10)

label_buku = tk.Label(root, text="Buku yang Dipinjam:")
label_buku.grid(row=1, column=0, padx=10, pady=10)
listbox_buku = tk.Listbox(root, selectmode=tk.SINGLE)
listbox_buku.grid(row=1, column=1, padx=10, pady=10)
button_cari_buku = tk.Button(root, text="Cari Buku", command=open_buku_form)
button_cari_buku.grid(row=1, column=2, padx=10, pady=10)
button_hapus_buku = tk.Button(root, text="Hapus Buku", command=hapus_buku)
button_hapus_buku.grid(row=1, column=3, padx=10, pady=10)

button_simpan = tk.Button(root, text="Simpan", command=simpan_peminjaman)
button_simpan.grid(row=2, column=1, pady=20)

root.mainloop()
