import psycopg2
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import customtkinter as ctk
from tkcalendar import DateEntry

# Declare id_detail_mapping dictionary
id_detail_mapping = {}

# Function to connect to the PostgreSQL database
def connect_to_database():
    return psycopg2.connect(
        dbname="LibraryGo",
        user="postgres",
        password="Easyjust123",  # Replace with your actual password
        host="localhost",
        port="5432"
    )

# Function to delete selected data
def delete_data():
    selected_item = table.selection()
    if selected_item:
        # Retrieve the index of the selected item
        index = int(selected_item[0][1:]) - 1
        # Retrieve the ID detail using the index
        item_id = id_detail_mapping.pop(index, None)
        if item_id is not None:
            # Connect to the PostgreSQL database
            conn_delete = connect_to_database()
            # Create a cursor to execute SQL queries
            cursor_delete = conn_delete.cursor()
            # Delete the data from the database
            delete_query = f"DELETE FROM detail_peminjaman WHERE id_detail = {item_id}"
            cursor_delete.execute(delete_query)
            conn_delete.commit()
            # Close the cursor and connection
            cursor_delete.close()
            conn_delete.close()

            # Remove the item from the Treeview
            table.delete(selected_item)

            # Update IDs in the Treeview
            update_ids_in_treeview()

    else:
        # No item selected, display a message
        messagebox.showinfo("Delete", "Please select an item to delete.")

# Function to update IDs in the Treeview
def update_ids_in_treeview():
    for i, item in enumerate(table.get_children(), start=1):
        table.item(item, values=(i,) + table.item(item, 'values')[1:])

    # Refresh the Treeview to update the display
    app.update()

    # Update IDs in the database
    conn_update = connect_to_database()
    cursor_update = conn_update.cursor()
    for i, item in enumerate(table.get_children(), start=1):
        old_id = id_detail_mapping.get(i)
        if old_id:
            new_id = i
            update_query = f"UPDATE detail_peminjaman SET id_detail = {new_id} WHERE id_detail = {old_id}"
            cursor_update.execute(update_query)
    conn_update.commit()
    cursor_update.close()
    conn_update.close()

# Function to refresh data
def refresh_data():
    # Clear existing data from the Treeview and ID mapping
    table.delete(*table.get_children())
    id_detail_mapping.clear()

    # Fetch new data from the database and insert into the Treeview
    conn_refresh = connect_to_database()
    cursor_refresh = conn_refresh.cursor()
    cursor_refresh.execute(query)
    for i, row in enumerate(cursor_refresh.fetchall(), start=1):
        table.insert('', END, values=(i,) + row[1:])  # Start ID from 1
        # Map ID detail to row index
        id_detail_mapping[i] = row[0]  # Assuming the first column is the ID
    # Close the cursor and connection
    cursor_refresh.close()
    conn_refresh.close()

# Tkinter application setup
app = Tk()
app.geometry('720x420')
app.configure(bg='#333333')
app.title("LiGO")

tambahDatabukuLabel = ctk.CTkLabel(app, text="Data manajemen buku", font=("Helvetica", 25), text_color="white")
tambahDatabukuLabel.pack(padx=50, pady=15)

tableFrame = ctk.CTkFrame(app, fg_color='#FAFAFA', corner_radius=10)
tableFrame.pack(padx=10, pady=10)

# Create the Treeview widget
table = ttk.Treeview(tableFrame, columns=("id_detail", "nama_anggota", "judul_buku", "tanggal_peminjaman"), show="headings")
table.heading('id_detail', text='ID Detail')
table.heading('nama_anggota', text='Nama Anggota')
table.heading('judul_buku', text='Judul Buku')
table.heading('tanggal_peminjaman', text='Tanggal Peminjaman')
table.pack(fill='both', expand=True)

# Fetch data from the database and insert into the Treeview
query = """
SELECT detail_peminjaman.id_detail, 
       anggota_perpustakaan.nama AS nama_anggota, 
       buku.judul_buku AS judul_buku, 
       peminjaman.tanggal_peminjaman AS tanggal_peminjaman
FROM peminjaman
INNER JOIN detail_peminjaman ON peminjaman.id_peminjaman = detail_peminjaman.id_peminjaman
INNER JOIN anggota_perpustakaan ON detail_peminjaman.id_anggota = anggota_perpustakaan.id_anggota
INNER JOIN buku ON detail_peminjaman.id_buku = buku.id_buku;
"""

# Connect to the PostgreSQL database
conn = connect_to_database()

# Create a cursor to execute SQL queries
cursor = conn.cursor()
cursor.execute(query)
for i, row in enumerate(cursor.fetchall(), start=1):
    table.insert('', END, values=(i,) + row[1:])  # Start ID from 1
    # Map ID detail to row index
    id_detail_mapping[i] = row[0]  # Assuming the first column is the ID

# Function to add a button to delete data
def add_delete_button():
    delete_button = Button(app, text="Delete Data", command=delete_data)
    delete_button.pack(pady=10)

# Call the function to add the delete button
add_delete_button()

app.mainloop()
