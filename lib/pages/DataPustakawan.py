from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from lib.utils.db import menambahkanData, fetch_data, cur, conn
from lib.utils.algoritma import merge_sort, dynamic_binary_search
from lib.components.header import header
import string, random


def DataPustakawan(akun):
    status = 0

    global selected_data
    
    def back() :
        nonlocal status
        status = 1
        
        app.destroy()
        # app.destroy()

    def on_item_selected(event):
        global selected_data
        selected_item = tabelPustakawan.selection()[0]
        selected_data = tabelPustakawan.item(selected_item, 'values')
        
    def delete_selected_data():
        if selected_data:
            confirm = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data ini?")
            if confirm:
                nip = selected_data[1]
                cur.execute(f"DELETE FROM pustakawan WHERE nip = {nip}")
                conn.commit()
                update_treeview()
        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")
            
        return
    
    def update_treeview():
        for item in tabelPustakawan.get_children():
            tabelPustakawan.delete(item)
        for i, row in enumerate(fetch_data("pustakawan")):
            tabelPustakawan.insert('', ctk.END, values=(i+1, *row[:]))
            
    def sort_and_display(key, secondary_key=None):
        data = fetch_data("pustakawan ")
        data = merge_sort(data, key, secondary_key)
        for item in tabelPustakawan.get_children():
            tabelPustakawan.delete(item)
        for i, row in enumerate(data):
            tabelPustakawan.insert('', ctk.END, values=(i+1, *row[:]))

    def search_pustakawan():
        search_term = inputNamaPustakawan.get().strip()
        if search_term:
            data = fetch_data("pustakawan")
            merge_sort(data, 0)  # Ensure data is sorted by title before binary search
            index = dynamic_binary_search(data, search_term)
            if index != -1:
                tabelPustakawan.delete(*tabelPustakawan.get_children())  # Remove all existing data
                tabelPustakawan.insert('', 'end', values=(1, *data[index][:]))  # Insert the searched data
            else:
                messagebox.showinfo("Hasil Pencarian", f"Pustakawan dengan Nama '{search_term}' tidak ditemukan.")
        else:
            messagebox.showwarning("Peringatan", "Harap masukkan Nama Pustakawan untuk mencari.")

    def tambah_data_pustakawan():
        
        app = header()
        
        def back() :
            app.destroy()
            update_treeview()
            return
        
        def upload_data(): 

            idanggota = entries[0].get()
            nama = entries[1].get()
            tanggal_lahir = entries[2].get()
            alamat = entries[3].get()
            no_telepon = entries[4].get()
            email = entries[5].get()
            passcode = generate_password()
            
            if not str(idanggota).isdigit() or not str(no_telepon).isdigit() or not nama or not alamat or not email or not tanggal_lahir or not no_telepon or not idanggota:
                messagebox.showwarning("Peringatan", "Masukkan data dengan benar !")
            else:
                cur.execute(f"INSERT INTO pustakawan (nip, nama, tanggal_lahir, alamat, no_telepon, email, passcode) VALUES ({idanggota}, '{nama}', '{tanggal_lahir}', '{alamat}', '{no_telepon}', '{email}', '{passcode}')")
                conn.commit()
                
                app.destroy()
                
                update_treeview()
                
                messagebox.showinfo("Success", "Data pustakawan berhasil ditambahkan!")
        
        tambahDataAnggotaLabel = ctk.CTkLabel(app, text="Tambah Data Pustakawan\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 45), text_color="Black")
        tambahDataAnggotaLabel.pack(padx=25, pady=15)

        mainFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        mainFrame.pack(padx=10, pady=10)

        labels = ["NIP", "Nama:", "Tanggal Lahir:", "Alamat:", "No telepon:", "Email:"]
        entries = []

        for i, text in enumerate(labels):
            label = ctk.CTkLabel(mainFrame, text=text, font=("Helvetica", 14), text_color="Black")
            label.grid(row=i, column=0, padx=5, pady=10, sticky='e')
            
            if text == "Tanggal Lahir:":
                entry = DateEntry(mainFrame, widht=50, background='darkblue', foreground='white', borderwidth=2, year=2023, date_pattern='yyyy-mm-dd')
            else:
                entry = ctk.CTkEntry(mainFrame, width=300, fg_color='#FAFAFA', text_color='Black', placeholder_text=text.replace(":", ""))
            
            entry.grid(row=i, column=1, padx=10, pady=10, sticky='w')
            entries.append(entry)
        
        frame_action = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
        frame_action.pack(padx=10, pady=10)
        
        TombolPerintah = [ctk.CTkButton(frame_action, text="Submit", text_color='Black', command=upload_data),
                          ctk.CTkButton(frame_action, text="Kembali", text_color='Black', command=back)]

        TombolPerintah[0].grid(row=0, column=0, padx=10, pady=10)
        TombolPerintah[1].grid(row=0, column=1, padx=10, pady=10)

        app.mainloop()

    def edit_data_Pustakawan():
        def back() :
            app.destroy()
            return
        
        def save_edit():
            if not entries[2].get().isdigit() or not entries[0].get() or not entries[1].get() or not entries[3].get() or not entries[4].get() or not entries[2]:
                messagebox.showwarning("Peringatan", "Masukkan data dengan benar !")
            else:
                # Lanjutkan dengan proses upload data
                nip = selected_data[1]

                new_data = (entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get())
                cur.execute("UPDATE pustakawan SET nama = %s, alamat = %s, no_telepon = %s, email = %s, tanggal_lahir = %s WHERE nip = %s", (*new_data, nip))
                conn.commit()
                app.destroy()

        if selected_data:
            app = header()
            editDataPustakawanLabel = ctk.CTkLabel(app, text="Edit Pustakawan\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 45), text_color="Black")
            editDataPustakawanLabel.pack(padx=25, pady=15)
            mainFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
            mainFrame.pack(padx=10, pady=10)

            labels = ["Nama:", "Alamat:", "No telepon:", "Email:","Tanggal lahir:"]
            entries = []
            
            Tanggal = StringVar()
            Tanggal.set(selected_data[6])
            
            for i, text in enumerate(labels):
                label = ctk.CTkLabel(mainFrame, text=text, font=("Helvetica", 14), text_color="Black")
                label.grid(row=i, column=0, padx=5, pady=10, sticky='e')

                if text == "Tanggal lahir:":
                    entry = DateEntry(mainFrame, width=50, background='darkblue', foreground='white', borderwidth=2, year=2023, date_pattern='yyyy-mm-dd')
                    entry.delete(0, ctk.END)
                    entry.insert(0, selected_data[6])
                else:
                    entry = ctk.CTkEntry(mainFrame,font=("Helvetica", 14),width=250, text_color='Black', fg_color='#FAFAFA')

                entry.grid(row=i, column=1, padx=10, pady=10, sticky='w')
                entries.append(entry)

            entries[0].insert(0, selected_data[2])
            entries[1].insert(0, selected_data[3])
            entries[2].insert(0, selected_data[4])
            entries[3].insert(0, selected_data[5])

            frame_action = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
            frame_action.pack(padx=10, pady=10)

            submit_button = ctk.CTkButton(frame_action, text="Submit", command=save_edit)
            submit_button.grid(row=0, column=0, padx=10, pady=5)

            button_kembali=ctk.CTkButton(frame_action, text="Kembali",command=back)
            button_kembali.grid(row=0, column=1, padx=10, pady=5)

        else:
            messagebox.showwarning("Peringatan", "Tidak ada data yang dipilih.")

        app.mainloop()   



    selected_data = None
    app = header()
    
    columns = ('#1', '#2', '#3', '#4', '#5', '#6', '#7')
    tabelPustakawan = ttk.Treeview(app, columns=columns, show='headings')
    
    # Creating the sorting buttons
    sortFrame = ctk.CTkFrame(app, fg_color='white', corner_radius=10)
    sortFrame.pack(padx=10, pady=10)
    
    sortByNameButton = ctk.CTkButton(sortFrame, text="Sort by Name", command=lambda: sort_and_display(1))
    sortByNameButton.grid(row=0, column=0, padx=10, pady=5, sticky='ew')

    sortByIDButton = ctk.CTkButton(sortFrame, text="Sort by ID", command=lambda: sort_and_display(0))
    sortByIDButton.grid(row=0, column=2, padx=10, pady=5, sticky='ew')
    
    frameSearching = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frameSearching.pack(pady=10)

    labelSearching = ctk.CTkLabel(frameSearching, text="Cari Nama Pustakawan :", text_color='Black')
    labelSearching.grid(row=0, column=0, padx=5)

    inputNamaPustakawan = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputNamaPustakawan.grid(row=0, column=1, padx=5)
    
    tombolSearching = ctk.CTkButton(frameSearching, text="Cari", command=search_pustakawan)
    tombolSearching.grid(row=0, column=2, padx=5)
    inputNamaPustakawan.bind("<Return>", lambda event: search_pustakawan())
    
    tabelPustakawan.heading('#1', text='No')
    tabelPustakawan.heading('#2', text='NIP')
    tabelPustakawan.heading('#3', text='Nama Pustakawan')
    tabelPustakawan.heading('#4', text='Alamat')
    tabelPustakawan.heading('#5', text='No. Telepon')
    tabelPustakawan.heading('#6', text='Email')
    tabelPustakawan.heading('#7', text='Tanggal Lahir')
    
    tabelPustakawan.column('#1', width=60)
    tabelPustakawan.column('#2', width=60)
    tabelPustakawan.column('#3', width=200)
    tabelPustakawan.column('#4', width=100)
    tabelPustakawan.column('#5', width=100)
    tabelPustakawan.column('#6', width=150)
    tabelPustakawan.column('#7', width=100)
    
    data = fetch_data("pustakawan")
    update_treeview()
    tabelPustakawan.pack(pady=15)
    tabelPustakawan.bind('<ButtonRelease-1>', on_item_selected)
    
    if akun[0][1] == 1:

        frame_actions = ctk.CTkFrame(app, fg_color='#FAFAFA')
        frame_actions.pack()

        button_edit = ctk.CTkButton(frame_actions, text="Edit",command=edit_data_Pustakawan)
        button_edit.grid(row=0, column=0, padx=10, pady=10)

        button_add = ctk.CTkButton(frame_actions, text="Tambah", command=tambah_data_pustakawan)
        button_add.grid(row=0, column=1, padx=10, pady=10)
        
        button_delete = ctk.CTkButton(frame_actions, text="Hapus", command=delete_selected_data)
        button_delete.grid(row=0, column=2, padx=10, pady=10)
    
    button_kembali=ctk.CTkButton(frame_actions, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)
    
    app.mainloop()
    
    return status

def generate_password():
    characters = string.digits + string.ascii_letters
    password = ""
    for _ in range(8):
        password += random.choice(characters)
    return password

