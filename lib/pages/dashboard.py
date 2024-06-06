from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from lib.components.header import header

detail_data = []

def show_detail():
    detail_window = header()

    detail_label = ctk.CTkLabel(detail_window, text="Profil Pengguna\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
    detail_label.pack(padx=25, pady=15)

    detail_frame = ctk.CTkFrame(detail_window, fg_color='white', corner_radius=10)
    detail_frame.pack(padx=10, pady=10)

    labels = ["ID:", "Nama:", "Alamat:", "No. Telepon:", "Email:", "Tanggal Lahir:", "Passcode:"]
    value_labels = []

    for i, text in enumerate(labels):
        label = ctk.CTkLabel(detail_frame, text=text, font=("Helvetica", 14), text_color="Black")
        label.grid(row=i, column=0, padx=5, pady=10, sticky='e')

        if text == "Passcode:":
            value_label = ctk.CTkLabel(detail_frame, text="*******", font=("Helvetica", 14), text_color="Black")
            value_label.grid(row=i, column=1, padx=10, pady=10, sticky='w')
            toggle_button = ctk.CTkButton(detail_frame, text="Show", command=lambda l=value_label: toggle_passcode(l))
            toggle_button.grid(row=i, column=2, padx=10, pady=10)
        else:
            value_label = ctk.CTkLabel(detail_frame, text=detail_data[0][i], font=("Helvetica", 14), text_color="Black")
            value_label.grid(row=i, column=1, padx=10, pady=10, sticky='w')
        
        value_labels.append(value_label)

    close_button = ctk.CTkButton(detail_window, text="Tutup", command=detail_window.destroy)
    close_button.pack(pady=10)

def toggle_passcode(label):
    if label.cget("text") == "*******":
        label.configure(text=detail_data[0][6])  # Assuming detail_data[6] is the passcode
    else:
        label.configure(text="*******")

def dashboard(akun):
    global detail_data
    status = 0

    # Assume akun contains the necessary details for the profile
    detail_data = [akun[0][0]]
    print(detail_data)
    menuTarget = []

    def navigate(Parameter):
        match Parameter:
            case 1:
                menuTarget.append("Data Buku")
            case 2:
                menuTarget.append("Data Anggota")
            case 3:
                menuTarget.append("Data Pustakawan")
        app.destroy()

    def logout_action():
        nonlocal akun, status
        status = 1
        akun = []
        app.destroy()

    app = header()
    
    RootFrame = ctk.CTkFrame(app, fg_color="White")
    RootFrame.pack()

    LeftFrame = ctk.CTkFrame(RootFrame, width=200, height=550, fg_color="White")
    LeftFrame.grid(row=0, column=0, padx=10, pady=20, sticky='ew')

    RightFrame = ctk.CTkFrame(RootFrame, width=650, height=550, fg_color="White")
    RightFrame.grid(row=0, column=1, padx=10, pady=20)

    image = Image.open("Logo.png")
    logo = ImageTk.PhotoImage(image)

    logo_label = ctk.CTkLabel(LeftFrame, image=logo, text='', bg_color='#FAFAFA')
    logo_label.image = logo 
    logo_label.grid(row=1, column=0, pady=20)
    
    Welcome = ctk.CTkLabel(RightFrame, text="Selamat Datang", text_color="#22437B", font=("Gill Sans Ultra Bold Condensed", 50))
    Welcome.pack(padx=150, pady=(10, 20))
    
    lblNama = ctk.CTkLabel(RightFrame, text=f"{akun[0][0][1]}", text_color="#22437B", font=("Gill Sans Ultra Bold Condensed", 30))
    lblNama.pack(padx=100, pady=10)

    ProfilButton = ctk.CTkButton(LeftFrame, text="Profil", width=180, text_color='Black', command=show_detail)
    ProfilButton.grid(row=2, column=0, padx=10, pady=10, sticky="ew")

    DataBuku = ctk.CTkButton(LeftFrame, text="Data Buku", width=180, text_color='Black', command=lambda: navigate(1))
    DataBuku.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

    DataPeminjaman = ctk.CTkButton(LeftFrame, text="Data Peminjaman", width=180, text_color='Black')
    DataPeminjaman.grid(row=4, column=0, padx=10, pady=10, sticky="ew")

    if akun[0][1] == 1:
        DataAnggota = ctk.CTkButton(LeftFrame, text="Data Anggota", width=180, text_color='Black', command=lambda: navigate(2))
        DataAnggota.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        DataPustakawan = ctk.CTkButton(LeftFrame, text="Data Pustakawan", width=180, text_color='Black', command=lambda: navigate(3))
        DataPustakawan.grid(row=6, column=0, padx=10, pady=10, sticky="ew")
        
        DataDenda = ctk.CTkButton(LeftFrame, text="Data Denda", width=180, text_color='Black')
        DataDenda.grid(row=7, column=0, padx=10, pady=(10,150), sticky="ew")
        
    elif akun[0][1] == 2:
        DataAnggota = ctk.CTkButton(LeftFrame, text="Data Anggota", width=180, text_color='Black', command=lambda: navigate(2))
        DataAnggota.grid(row=5, column=0, padx=10, pady=10, sticky="ew")

        DataDenda = ctk.CTkButton(LeftFrame, text="Data Denda", width=180, text_color='Black')
        DataDenda.grid(row=7, column=0, padx=10, pady=(10,150), sticky="ew")
        
    else: 
        DataDenda = ctk.CTkButton(LeftFrame, text="Data Denda", width=180, text_color='Black')
        DataDenda.grid(row=7, column=0, padx=10, pady=(10,195), sticky="ew")

    LogOut = ctk.CTkButton(LeftFrame, text="Log Out", width=180, text_color='Black', command=logout_action)
    LogOut.grid(row=8, column=0, padx=10, pady=10, sticky="ew")
    
    app.mainloop()

    return status, menuTarget, akun
