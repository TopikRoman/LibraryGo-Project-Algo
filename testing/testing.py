from tkinter import *
from tkinter import ttk
import customtkinter as ctk

# def click() :
#     output_text.insert(INSERT, "Success\n")

# window = Tk()
# window.geometry()
# window.title('Page 1')

# info = ttk.Style()
# info.configure('Info.TFrame', background='blue', borderWidth=5)

# frame = ttk.Frame(window, width=500, height=500, padding="10").grid(column=0, row=0, sticky=(N,W,E,S))


# button = ttk.Button(frame, text="CLICK", command=click).grid(column=0, row=0, sticky=(N, E))
# # button.pack()

# #Output Window test
# output_text = Text(frame, width=10, height=10)
# output_text.grid(column=1, row=0, sticky=(N, E, W, S))

app = Tk()
app.geometry('720x420')
app.title("Login")

def login() :
    Usn = username.get()
    Pwd = password.get()
    if Usn == 'Admin' and Pwd == 'Admin' :
        print("Login Berhasil")
        mainmenu()
    else :
        print("Login Gagal")
        
def mainmenu():
    MainMenuFrame.pack(fill="both", expand=True)
    LoginFrame.pack_forget()
    

# LoginFrame = ttk.Frame(app, padding=10)
# LoginFrame.pack(padx=10, pady=10)

LoginFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
LoginFrame.pack(padx=10, pady=100)

loginLabel = ctk.CTkLabel(LoginFrame, text="Login", font=("Helvetica", 24), text_color="Black")
loginLabel.pack(padx=10, pady=10)

username = ctk.CTkEntry(LoginFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Username")
username.pack(padx=10, pady=10)

password = ctk.CTkEntry(LoginFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan password")
password.pack(padx=10, pady=10)


submit = ctk.CTkButton(LoginFrame, text="Login", fg_color='#2DE053', text_color='Black', command=login)
submit.pack(padx=10, pady=10)

MainMenuFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
MainMenuFrame.pack(padx=10, pady=100)

MainMenuFrame.grid_columnconfigure(0, weight=1)
MainMenuFrame.grid_columnconfigure(1, weight=1)
MainMenuFrame.grid_columnconfigure(2, weight=1)

AturBuku = ctk.CTkButton(MainMenuFrame, text="Atur Buku", fg_color='#2DE053', text_color='Black')
AturBuku.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

LihatPeminjaman = ctk.CTkButton(MainMenuFrame, text="Lihat Peminjaman", fg_color='#2DE053', text_color='Black')
LihatPeminjaman.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

DataPeminjaman = ctk.CTkButton(MainMenuFrame, text="Data Peminjaman", fg_color='#2DE053', text_color='Black')
DataPeminjaman.grid(row=0, column=2, padx=10, pady=10, sticky="ew")

app.mainloop()
    
    