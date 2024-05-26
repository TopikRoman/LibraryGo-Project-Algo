from tkinter import *
import customtkinter as ctk

app = Tk()
app.geometry('720x420')
app.configure(bg='#333333')
app.title("LiGO")

def tambah_data_buku():
    # Add functionality for the button here
    pass


tambahDatabukuLabel = ctk.CTkLabel(app, text="LiGO", font=("Helvetica", 45), text_color="white")
tambahDatabukuLabel.pack(padx=50, pady=50)


# Creating the frame
tambahDatabukuFrame = ctk.CTkFrame(app, fg_color='white')
tambahDatabukuFrame.pack(padx=10, pady=10)

# Creating the label
judulBuku = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Judulnya")
judulBuku.pack(padx=10, pady=10)

# Creating entry
tahunPenerbit = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan tahun penerbit")
tahunPenerbit.pack(padx=10, pady=10)

Penerbit = ctk.CTkEntry(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Penerbitnya")
Penerbit.pack(padx=10, pady=10)

genreBuku = ctk.CTkComboBox(tambahDatabukuFrame, width=250, fg_color='#FAFAFA', text_color='Black', values=["Fiksi", "Non-Fiksi", "Sains", "Biografi", "Sejarah"])
genreBuku.pack(padx=10, pady=10)


app.mainloop()
