from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry
from lib.utils.db import menambahkanData, fetch_data, cur, conn
from lib.utils.algoritma import merge_sort, dynamic_binary_search
from lib.components.header import header


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
            
    def tambah_data_peminjam():
        
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

            # Insert the data into the database
            cur.execute(f"INSERT INTO pustakawan (nip, nama, tanggal_lahir, alamat, no_telepon, email) VALUES ({idanggota}, '{nama}', '{tanggal_lahir}', '{alamat}', '{no_telepon}', '{email}')")
            conn.commit()
            update_treeview()
            
            messagebox.showinfo("Success", "Data pustakawan berhasil ditambahkan!")
        
        tambahDataAnggotaLabel = ctk.CTkLabel(app, text="Tambah Data Anggota\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
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
        
        submitData = ctk.CTkButton(frame_action, text="Submit", text_color='Black', command=upload_data)
        submitData.grid(row=0, column=0, padx=10, pady=10)

        tombolKembali=ctk.CTkButton(frame_action, text="Kembali", text_color='Black', command=back)
        tombolKembali.grid(row=0, column=1, padx=10, pady=10)

        app.mainloop()

    def edit_data_Pustakawan():
        def back() :
            app.destroy()
            return
        def save_edit():
            nip = selected_data[1]
            new_data = (entries[0].get(), entries[1].get(), entries[2].get(), entries[3].get(), entries[4].get())
            # cur.execute("UPDATE anggota SET nama = %s, tanggal_lahir = %s, alamat = %s, no_telepon = %s, email = %s WHERE id_anggota = %s", (*new_data, id_anggota))
            cur.execute("UPDATE pustakawan SET nama = %s, alamat = %s, no_telepon = %s, email = %s, tanggal_lahir = %s WHERE nip = %s", (*new_data, nip))
            conn.commit()
            app.destroy()

        if selected_data:
            app = header()
            editDataPustakawanLabel = ctk.CTkLabel(app, text="Edit Pustakawan\nLibrary Go", font=("Gill Sans Ultra Bold Condensed", 25), text_color="Black")
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

    labelSearching = ctk.CTkLabel(frameSearching, text="Cari ID Pustakawan :", text_color='Black')
    labelSearching.grid(row=0, column=0, padx=5)

    inputIDAnggota = ctk.CTkEntry(frameSearching, fg_color='#FAFAFA', text_color='Black')
    inputIDAnggota.grid(row=0, column=1, padx=5)
    
    tombolSearching = ctk.CTkButton(frameSearching, text="Cari")
    tombolSearching.grid(row=0, column=2, padx=5)
    inputIDAnggota.bind("<Return>", lambda event: search_anggota())
    
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
    
    data = fetch_data("anggota_perpustakaan")
    update_treeview()
    tabelPustakawan.pack(pady=15)
    tabelPustakawan.bind('<ButtonRelease-1>', on_item_selected)
    
    frame_actions = ctk.CTkFrame(app, fg_color='#FAFAFA')
    frame_actions.pack()

    button_edit = ctk.CTkButton(frame_actions, text="Edit",command=edit_data_Pustakawan)
    button_edit.grid(row=0, column=0, padx=10, pady=10)

    button_add = ctk.CTkButton(frame_actions, text="Tambah", command=tambah_data_peminjam)
    button_add.grid(row=0, column=1, padx=10, pady=10)
    
    button_delete = ctk.CTkButton(frame_actions, text="Hapus", command=delete_selected_data)
    button_delete.grid(row=0, column=2, padx=10, pady=10)
    
    button_kembali=ctk.CTkButton(frame_actions, text="Kembali",command=back)
    button_kembali.grid(row=1,columns=3, padx=10, pady=15)
    
    app.mainloop()
    
    return status
