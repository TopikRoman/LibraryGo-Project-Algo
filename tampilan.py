import tkinter as tk
from tkinter import font

# Function to display notifications
def display_notification(message, color="red"):
    notification_label.config(text=message, fg=color)
    notification_label.pack(pady=10)

# Function to handle registration
def register_user():
    username = entry_username.get().strip()
    password = entry_password.get().strip()
    
    if not username or not password:
        display_notification("Please fill out all fields.")
    elif len(password) < 6:
        display_notification("Password must be at least 6 characters long.")
    elif username in users:
        display_notification("Username already exists.")
    else:
        users[username] = password
        display_notification("Registration successful!", "green")
        show_login_screen()

# Function to handle login
def login_user():
    username = login_entry_username.get().strip()
    password = login_entry_password.get().strip()
    
    if not username or not password:
        display_notification("Please fill out all fields.")
    elif username in users and users[username] == password:
        display_notification("Login successful!", "green")
        show_main_menu()
    else:
        display_notification("Invalid username or password.")

# Function to show the registration screen
def show_registration_screen():
    registration_frame.pack(fill="both", expand=True)
    login_frame.pack_forget()
    main_menu_frame.pack_forget()
    notification_label.pack_forget()

# Function to show the login screen
def show_login_screen():
    login_frame.pack(fill="both", expand=True)
    registration_frame.pack_forget()
    main_menu_frame.pack_forget()
    notification_label.pack_forget()

# Function to show the main menu
def show_main_menu():
    main_menu_frame.pack(fill="both", expand=True)
    registration_frame.pack_forget()
    login_frame.pack_forget()
    notification_label.pack_forget()

# Function to show the personal data screen
def show_data_diri():
    display_notification("Tampilkan Data Diri pengguna di sini.", "Red")

# Function to show the book search screen
def show_pencarian_buku():
    display_notification("Tampilkan pencarian buku di sini.", "blue")

# Function to show the book borrowing screen
def show_peminjaman_buku():
    display_notification("Tampilkan peminjaman buku di sini.", "blue")

# Dictionary to store user credentials (for example purposes only)
users = {}

# Create the main window
root = tk.Tk()
root.title("User Registration and Login")

# Center the window on the screen
window_width = 600
window_height = 400
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
position_top = int(screen_height / 2 - window_height / 2)
position_right = int(screen_width / 2 - window_width / 2)
root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Allow window resizing
root.resizable(True, True)

# Set custom fonts
title_font = font.Font(family="Helvetica", size=20, weight="bold")
custom_font = font.Font(family="Helvetica", size=14)

# Create a style dictionary for consistent styling
style = {
    'font': custom_font,
    'bg': "#f0f0f0",
    'fg': "#333",
    'padx': 10,
    'pady': 5
}

# Notification Label
notification_label = tk.Label(root, font=custom_font, bg=style['bg'])

# Registration Frame
registration_frame = tk.Frame(root, bg=style['bg'], bd=5)

registration_label = tk.Label(registration_frame, text="Register", font=title_font, bg=style['bg'], fg="#007acc")
registration_label.pack(pady=20)

entry_username = tk.Entry(registration_frame, font=custom_font, width=30, bd=2, relief="groove")
entry_username.pack(pady=10)
entry_username.insert(0, "Username")

entry_password = tk.Entry(registration_frame, font=custom_font, width=30, show="*", bd=2, relief="groove")
entry_password.pack(pady=10)
entry_password.insert(0, "Password")

register_button = tk.Button(registration_frame, text="Register", font=custom_font, bg="#28a745", fg="white", command=register_user)
register_button.pack(pady=20)

switch_to_login_button = tk.Button(registration_frame, text="Go to Login", font=custom_font, bg="#007acc", fg="white", command=show_login_screen)
switch_to_login_button.pack(pady=10)

# Login Frame
login_frame = tk.Frame(root, bg=style['bg'], bd=5)

login_label = tk.Label(login_frame, text="Login", font=title_font, bg=style['bg'], fg="#007acc")
login_label.pack(pady=20)

login_entry_username = tk.Entry(login_frame, font=custom_font, width=30, bd=2, relief="groove")
login_entry_username.pack(pady=10)
login_entry_username.insert(0, "Username")

login_entry_password = tk.Entry(login_frame, font=custom_font, width=30, show="*", bd=2, relief="groove")
login_entry_password.pack(pady=10)
login_entry_password.insert(0, "Password")

login_button = tk.Button(login_frame, text="Login", font=custom_font, bg="#007acc", fg="white", command=login_user)
login_button.pack(pady=20)

switch_to_register_button = tk.Button(login_frame, text="Go to Register", font=custom_font, bg="#28a745", fg="white", command=show_registration_screen)
switch_to_register_button.pack(pady=10)

# Main Menu Frame
main_menu_frame = tk.Frame(root, bg=style['bg'], bd=5)

main_menu_label = tk.Label(main_menu_frame, text="Main Menu", font=title_font, bg=style['bg'], fg="#007acc")
main_menu_label.pack(pady=20)

data_diri_button = tk.Button(main_menu_frame, text="Data Diri", font=custom_font, bg="#007acc", fg="white", command=show_data_diri)
data_diri_button.pack(pady=10)

pencarian_buku_button = tk.Button(main_menu_frame, text="Pencarian Buku", font=custom_font, bg="#007acc", fg="white", command=show_pencarian_buku)
pencarian_buku_button.pack(pady=10)

peminjaman_buku_button = tk.Button(main_menu_frame, text="Peminjaman Buku", font=custom_font, bg="#007acc", fg="white", command=show_peminjaman_buku)
peminjaman_buku_button.pack(pady=10)

logout_button = tk.Button(main_menu_frame, text="Logout", font=custom_font, bg="#28a745", fg="white", command=show_login_screen)
logout_button.pack(pady=10)

exit_button = tk.Button(main_menu_frame, text="Exit", font=custom_font, bg="#dc3545", fg="white", command=root.quit)
exit_button.pack(pady=10)

# Start with the registration screen
show_registration_screen()

# Run the application
root.mainloop()

