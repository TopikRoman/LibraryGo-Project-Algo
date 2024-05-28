from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from lib.utils.db import menambahkanData, fetch_data, cur, conn
from lib.components.header import header
app = header()

# ctk.CTkLabel(app, text="Edit Data Buku", font=("Helvetica", 25), text_color="Black").pack(padx=25, pady=15)

# frameEdit = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
# frameEdit.pack(padx=10, pady=10)


# ctk.CTkLabel(frameEdit, text="Judul Buku").pack(padx=5, pady=5)
# entry_judul = ctk.CTkEntry(frameEdit)
# entry_judul.pack(padx=5, pady=5)
# # entry_judul.insert(0, selected_data[1])

# ctk.CTkLabel(frameEdit, text="Tahun Terbit").pack(padx=5, pady=5)
# entry_tahun = ctk.CTkEntry(frameEdit)
# entry_tahun.pack(padx=5, pady=5)
# # entry_tahun.insert(0, selected_data[2])

# ctk.CTkLabel(frameEdit, text="Penerbit").pack(padx=5, pady=5)
# entry_penerbit = ctk.CTkEntry(frameEdit)
# entry_penerbit.pack(padx=5, pady=5)
# # entry_penerbit.insert(0, selected_data[3])

# ctk.CTkLabel(frameEdit, text="ID Genre").pack(padx=5, pady=5)
# entry_genre = ctk.CTkEntry(frameEdit)
# entry_genre.pack(padx=5, pady=5)
# # entry_genre.insert(0, selected_data[4])

# app.mainloop()

ctk.CTkLabel(app, text="Edit Data Buku", font=("Helvetica", 25), text_color="Black").pack(padx=25, pady=15)

frameEdit = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
frameEdit.pack(padx=10, pady=10)

ctk.CTkLabel(frameEdit, text="Judul Buku", text_color='Black').pack(padx=5, pady=0)
entry_judul = ctk.CTkEntry(frameEdit, width=250, fg_color='#FAFAFA', text_color='Black')
entry_judul.pack(padx=5, pady=5)
# entry_judul.insert(0, selected_data[1])

ctk.CTkLabel(frameEdit, text="Tahun Terbit", text_color='Black').pack(padx=5, pady=0)
entry_tahun = ctk.CTkEntry(frameEdit, width=250, fg_color='#FAFAFA', text_color='Black')
entry_tahun.pack(padx=5, pady=5)
# entry_tahun.insert(0, selected_data[2])

ctk.CTkLabel(frameEdit, text="Penerbit", text_color='Black').pack(padx=5, pady=0)
entry_penerbit = ctk.CTkEntry(frameEdit, width=250, fg_color='#FAFAFA', text_color='Black')
entry_penerbit.pack(padx=5, pady=5)
# entry_penerbit.insert(0, selected_data[3])

ctk.CTkLabel(frameEdit, text="Genre", text_color='Black').pack(padx=5, pady=0)
genreBuku = ctk.CTkComboBox(frameEdit, width=250, fg_color='#FAFAFA', text_color='Black', values=["Fiksi", "Non-Fiksi", "Sains", "Biografi", "Sejarah"], corner_radius=50)
genreBuku.pack(padx=10, pady=10)

submit_button = ctk.CTkButton(app, text="Submit")
submit_button.pack(padx=5, pady=5)

app.mainloop()