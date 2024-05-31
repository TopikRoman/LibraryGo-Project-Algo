from pickle import NONE
import psycopg2

conn = psycopg2.connect(
    dbname="LibraryGo.Baru",
    user="postgres",
    password="19Januari",
    host="localhost",
    port="5432"
)

cur = conn.cursor()

def fetch_data(Parameter: str=''):
    
    cur.execute(f"SELECT * FROM {Parameter}")
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

def readAnggota(idAnggota: str = ''):
    key = idAnggota
    
    if key != '':
        search = f"WHERE id_anggota = {key}"
    
    cur.execute(f"SELECT * FROM anggota_perpustakaan {search}")
    data = cur.fetchall()
    
    return data
    