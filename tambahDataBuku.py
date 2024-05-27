from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry

app = Tk()
app.geometry('720x420')
app.configure(bg='#333333')
app.title("LiGO")

def tambah_data_peminjam(): 
    # If all checks pass, show success message
    messagebox.showinfo("Success", "Data anggota berhasil ditambahkan!")

# Creating the main label
tambahDataAnggotaLabel = ctk.CTkLabel(app, text="Tambah Anggota\nLiGO", font=("Helvetica", 25), text_color="white")
tambahDataAnggotaLabel.pack(padx=25, pady=15)

# Creating the main frame for the form
mainFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
mainFrame.pack(padx=10, pady=10)

# Creating the labels and entries for the form
labels = ["Nama:", "Tanggal Lahir:", "Alamat:", "No telepon:", "Email:"]
entries = []

for i, text in enumerate(labels):
    label = ctk.CTkLabel(mainFrame, text=text, font=("Helvetica", 14), text_color="Black")
    label.grid(row=i, column=0, padx=5, pady=10, sticky='e')
    
    if text == "Tanggal Lahir:":
        entry = DateEntry(mainFrame, width=50, background='darkblue', foreground='white', borderwidth=2, year=2023, date_pattern='yyyy-mm-dd')
    else:
        entry = ctk.CTkEntry(mainFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text=text.replace(":", ""))
    
    entry.grid(row=i, column=1, padx=10, pady=10, sticky='w')
    entries.append(entry)

# Creating the submit button
submitData = ctk.CTkButton(app, text="Submit", fg_color='#FF3399', text_color='Black', command=tambah_data_peminjam, corner_radius=50)
submitData.pack(padx=25, pady=15)

app.mainloop()