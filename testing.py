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
    print(username.get())
    print(password.get())

# inputFrame = ttk.Frame(app, padding=10)
# inputFrame.pack(padx=10, pady=10)

inputFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', )
inputFrame.pack(padx=10, pady=100)

loginLabel = ctk.CTkLabel(inputFrame, text="Login", font=("Helvetica", 24), text_color="Black")
loginLabel.pack(padx=10, pady=10)


username = ctk.CTkEntry(inputFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan Username")
username.pack(padx=10, pady=10)

password = ctk.CTkEntry(inputFrame, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text="Masukkan password")
password.pack(padx=10, pady=10)


submit = ctk.CTkButton(inputFrame, text="Login", fg_color='#2DE053', text_color='Black', command=login)
submit.pack(padx=10, pady=10)

app.mainloop()
    
    