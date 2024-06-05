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
    
    cur.execute(f"SELECT * FROM pustakawan WHERE email = '{username}' AND passcode = '{password}'")
    data = cur.fetchone()
    
    if data == None:
        cur.execute(f"SELECT * FROM anggota_perpustakaan WHERE email = '{username}' AND passcode = '{password}'")
        data = cur.fetchone()
        return data, 3
        
    # if password.isnumeric() and len(password) == 8 :
    #     table = 'pustakawan'
    #     primaryKey = 'right(CAST(nip AS VARCHAR), 8)'
    # elif password.isnumeric() and len(password) == 6 :
    #     table = 'anggota_perpustakaan'
    #     primaryKey = 'id_anggota'
    # else : 
    #     return 'Password tidak sesuai'
    
    if data == None :
        return 'Akun tidak ditemukan'
    
    return data, 2

def readAnggota(idAnggota: str = ''):
    key = idAnggota
    
    if key != '':
        search = f"WHERE id_anggota = {key}"
    
    cur.execute(f"SELECT * FROM anggota_perpustakaan {search}")
    data = cur.fetchall()
    
    return data
    