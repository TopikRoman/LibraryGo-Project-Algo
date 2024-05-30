import tkinter as tk

import customtkinter as ctk

app = tk.Tk()
app.maxsize(900, 600)
app.title("Library Go")

LeftFrame = tk.Frame(app, width=200, height=550, bg='White')
LeftFrame.grid(row=0, column=0, padx=10, pady=20, sticky='ew')

RightFrame = tk.Frame(app, width=650, height=550, bg='White')
RightFrame.grid(row=0, column=1, padx=10, pady=20)

# Load logo image
logo_path = "Logo.png"
image = Image.open(logo_path)
logo = ImageTk.PhotoImage(image)

# Create a label to display the logo and add it to the left frame
logo_label = tk.Label(LeftFrame, image=logo, bg='White', text='')
logo_label.image = logo  # Keep a reference to the image to prevent garbage collection
logo_label.grid(row=0, column=0, pady=20)  # Adjust padding as needed

DataBuku = ctk.CTkButton(LeftFrame, text="Data Buku", width=180, text_color='Black', command=lambda: navigate(1))
DataBuku.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

DataPeminjaman = ctk.CTkButton(LeftFrame, text="Data Pustakawan", width=180, text_color='Black')
DataPeminjaman.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

DataAnggota = ctk.CTkButton(LeftFrame, text="Data Peminjaman", width=180, text_color='Black')
DataAnggota.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

DataPustakawan = ctk.CTkButton(LeftFrame, text="Data Anggota", width=180, text_color='Black', command=lambda: navigate(2))
DataPustakawan.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

DataDenda = ctk.CTkButton(LeftFrame, text="Data Denda", width=180, text_color='Black')
DataDenda.grid(row=5, column=0, padx=10, pady=(10,178), sticky="ew")

LogOut = ctk.CTkButton(LeftFrame, text="Log Out", width=180, text_color='Black')
LogOut.grid(row=6, column=0, padx=10, pady=10, sticky="ew")


app.mainloop()
