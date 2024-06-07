from pickle import NONE
import psycopg2

conn = psycopg2.connect(
    dbname="LibraryGo",
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

def membacaPeminjaman():
    cur.execute(f"""select p.id_peminjaman, p.tanggal_peminjaman, p.tenggat_pengembalian, a.nama, p.status_peminjaman, p.id_anggota
                from peminjaman p join anggota_perpustakaan a on (p.id_anggota = a.id_anggota)""")
    rows = cur.fetchall()
    return rows

def membacaDetailPeminjaman():
    cur.execute(f"""select b.judul_buku
                    from detail_peminjaman dp join buku b on (dp.id_buku = b.id_buku)""")
    rows = cur.fetchall()
    return rows

def loginQuery(username, password) :
    table = ''
    primaryKey = ''
    
    cur.execute(f"SELECT * FROM pustakawan WHERE email = '{username}' AND passcode = '{password}'")
    data = cur.fetchone()
    
    
    if data == None:
        cur.execute(f"SELECT * FROM anggota_perpustakaan WHERE email = '{username}' AND passcode = '{password}'")
        data = cur.fetchone()
        if data:
            return data, 3
        return "Password tidak sesuai"
    elif data:
        if data[1] == "Andi Wijaya":
            return data, 1
        return data, 2
    
        
    # if password.isnumeric() and len(password) == 8 :
    #     table = 'pustakawan'
    #     primaryKey = 'right(CAST(nip AS VARCHAR), 8)'
    # elif password.isnumeric() and len(password) == 6 :
    #     table = 'anggota_perpustakaan'
    #     primaryKey = 'id_anggota'
    # else : 
    #     return 'Password tidak sesuai'

def readAnggota(idAnggota: str = ''):
    key = idAnggota
    
    if key != '':
        search = f"WHERE id_anggota = {key}"
    
    cur.execute(f"SELECT * FROM anggota_perpustakaan {search}")
    data = cur.fetchall()
    
    return data
    