import tkinter as tk
from tkinter import messagebox

# Function to handle registration
def register():
    username = entry_register_username.get()
    password = entry_register_password.get()

    if username and password:
        with open('users.txt', 'a') as file:
            file.write(f"{username},{password}\n")
        messagebox.showinfo("Success", "Registration berhasil!")
    else:
        messagebox.showerror("Error", "isi terlebih dahulu.")

# Function to handle login
def login():
    username = entry_login_username.get()
    password = entry_login_password.get()

    if username and password:
        with open('users.txt', 'r') as file:
            users = file.readlines()
            for user in users:
                saved_username, saved_password = user.strip().split(',')
                if saved_username == username and saved_password == password:
                    messagebox.showinfo("Success", "Login berhasil!")
                    return
            messagebox.showerror("Error", "Invalid username or password.")
    else:
        messagebox.showerror("Error", "Please fill out all fields.")

# Function to open register window
def open_register_window():
    login_window.withdraw()
    register_window.deiconify()

# Function to open login window
def open_login_window():
    register_window.withdraw()
    login_window.deiconify()

# Create the main windows
login_window = tk.Tk()
login_window.title("Login")

register_window = tk.Toplevel(login_window)
register_window.title("Register")
register_window.withdraw()

# Create the login frame
frame_login = tk.Frame(login_window)
frame_login.pack(padx=10, pady=10)

label_login_title = tk.Label(frame_login, text="Login")
label_login_title.grid(row=0, column=0, columnspan=2)

label_login_username = tk.Label(frame_login, text="Username:")
label_login_username.grid(row=1, column=0)
entry_login_username = tk.Entry(frame_login)
entry_login_username.grid(row=1, column=1)

label_login_password = tk.Label(frame_login, text="Password:")
label_login_password.grid(row=2, column=0)
entry_login_password = tk.Entry(frame_login, show='*')
entry_login_password.grid(row=2, column=1)

button_login = tk.Button(frame_login, text="Login", command=login)
button_login.grid(row=3, column=0, columnspan=2)

button_open_register = tk.Button(frame_login, text="Register", command=open_register_window)
button_open_register.grid(row=4, column=0, columnspan=2)

# Create the registration frame
frame_register = tk.Frame(register_window)
frame_register.pack(padx=10, pady=10)

label_register_title = tk.Label(frame_register, text="Register")
label_register_title.grid(row=0, column=0, columnspan=2)

label_register_username = tk.Label(frame_register, text="Username:")
label_register_username.grid(row=1, column=0)
entry_register_username = tk.Entry(frame_register)
entry_register_username.grid(row=1, column=1)

label_register_password = tk.Label(frame_register, text="Password:")
label_register_password.grid(row=2, column=0)
entry_register_password = tk.Entry(frame_register, show='*')
entry_register_password.grid(row=2, column=1)

button_register = tk.Button(frame_register, text="Register", command=register)
button_register.grid(row=3, column=0, columnspan=2)

button_open_login = tk.Button(frame_register, text="Login", command=open_login_window)
button_open_login.grid(row=4, column=0, columnspan=2)

# Run the main event loop
login_window.mainloop()
