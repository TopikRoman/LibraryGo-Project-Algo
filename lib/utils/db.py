from pickle import NONE
import psycopg2

conn = psycopg2.connect(
    dbname="LibraryGo",
    user="postgres",
    password="12345678",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

def fetch_data():
    cur.execute("SELECT * FROM buku")
    rows = cur.fetchall()
    return rows

def menambahkanData(namaTabel, namaKolom, values):
    cur.execute("INSERT INTO " + namaTabel + " " + f'({namaKolom})' + " VALUES " + f'{values}'.replace("[", "(").replace("]", ")"))
    conn.commit()
    return


def loginQuery(username, password) :
    table = ''
    primaryKey = ''
    


    if password.isnumeric() and len(password) == 8 :
        table = 'pustakawan'
        primaryKey = 'right(CAST(nip AS VARCHAR), 8)'
    elif password.isnumeric() and len(password) == 6 :
        table = 'anggota_perpustakaan'
        primaryKey = 'id_anggota'
    else : 
        return 'Password tidak sesuai'

    cur.execute(f"SELECT * FROM {table} WHERE email = '{username}' AND {primaryKey} = '{password}'")
    
    data = cur.fetchone()
    

    if data == None :
        return 'Akun tidak ditemukan'
    
    return data
