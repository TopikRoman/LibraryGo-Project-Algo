from tkinter import *
from tkinter import messagebox
import customtkinter as ctk
from lib.utils.db import menambahkanData

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

    app = Tk()
    app.geometry('720x420')
    app.configure(bg='#333333')
    app.title("LiGO")
    
    tambahDatabukuLabel = ctk.CTkLabel(app, text="LiGO", font=("Helvetica", 45), text_color="white")
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

