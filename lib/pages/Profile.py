from tkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from lib.components.header import header

detail_data = []

def showProfile (akun):
    
    status = 0
        
    def back() :
        nonlocal status
        status = 1
        
        app.destroy()
        # app.destroy()
    
    app = header()
    
    detail_data.append(akun[0][0])
    
    print(detail_data)

    detail_label = ctk.CTkLabel(app, text="Profil Pengguna\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
    detail_label.pack(padx=25, pady=15)

    detail_frame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    detail_frame.pack(padx=10, pady=10)

    labels = ["ID:", "Nama:", "Alamat:", "No. Telepon:", "Email:", "Tanggal Lahir:", "Passcode:"]
    value_labels = []

    for i, text in enumerate(labels):
        label = ctk.CTkLabel(detail_frame, text=text, font=("Helvetica", 14), text_color="Black")
        label.grid(row=i, column=0, padx=5, pady=10, sticky='e')

        if text == "Passcode:":
            value_label = ctk.CTkLabel(detail_frame, text="*******", font=("Helvetica", 14), text_color="Black")
            value_label.grid(row=i, column=1, padx=10, pady=10, sticky='w')
            toggle_button = ctk.CTkButton(detail_frame, text="Show", command=lambda l=value_label: tampilkanPassword(l))
            toggle_button.grid(row=i, column=2, padx=10, pady=10)
        else:
            value_label = ctk.CTkLabel(detail_frame, text=detail_data[0][i], font=("Helvetica", 14), text_color="Black")
            value_label.grid(row=i, column=1, padx=10, pady=10, sticky='w')
        
        value_labels.append(value_label)

    close_button = ctk.CTkButton(app, text="Tutup", command=back)
    close_button.pack(pady=10)
    
    app.mainloop()
    
    return status
    
    

def tampilkanPassword(label):
    if label.cget("text") == "*******":
        label.configure(text=detail_data[0][6])  # Assuming detail_data[6] is the passcode
    else:
        label.configure(text="*******")
