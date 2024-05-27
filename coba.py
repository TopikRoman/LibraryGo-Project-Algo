import customtkinter as ctk
from tkinter import Tk

def header():
    app = Tk()
    app.geometry('720x420')
    app.title("Library Go")
    return app

def save_data():
    title = entry_title.get()
    year = entry_year.get()
    publisher = entry_publisher.get()
    genre = genre_var.get()
    print(f"Judul Buku: {title}")
    print(f"Tahun Terbit: {year}")
    print(f"Penerbit: {publisher}")
    print(f"Genre: {genre}")

# Initialize the main window using the header function
root = header()

# Configure customtkinter to use the Tk root window
ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# Frame for the form
form_frame = ctk.CTkFrame(root)
form_frame.pack(padx=20, pady=20, sticky="ew")

# Title entry
ctk.CTkLabel(form_frame, text="Masukkan Judulnya").grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
entry_title = ctk.CTkEntry(form_frame)
entry_title.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

# Year entry
ctk.CTkLabel(form_frame, text="Masukkan tahun penerbit").grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
entry_year = ctk.CTkEntry(form_frame)
entry_year.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

# Publisher entry
ctk.CTkLabel(form_frame, text="Masukkan Penerbitnya").grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
entry_publisher = ctk.CTkEntry(form_frame)
entry_publisher.grid(row=5, column=0, padx=10, pady=5, sticky="ew")

# Genre dropdown
ctk.CTkLabel(form_frame, text="Genre").grid(row=6, column=0, padx=10, pady=(10, 0), sticky="w")
genre_var = ctk.StringVar(value="Fiksi")
genre_dropdown = ctk.CTkComboBox(form_frame, values=["Fiksi", "Non-Fiksi", "Sci-Fi", "Biografi"], variable=genre_var)
genre_dropdown.grid(row=7, column=0, padx=10, pady=5, sticky="ew")

# Buttons
submit_button = ctk.CTkButton(form_frame, text="Submit", command=save_data)
submit_button.grid(row=8, column=0, padx=10, pady=(20, 10), sticky="ew")

back_button = ctk.CTkButton(form_frame, text="Kembali", command=root.quit)
back_button.grid(row=9, column=0, padx=10, pady=5, sticky="ew")

# Run the GUI
root.mainloop()
