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
    cur.execute(f"""select dp.id_buku, b.judul_buku, dp.status_peminjaman, dp.id_peminjaman
                    from detail_peminjaman dp join buku b on (dp.id_buku = b.id_buku)""")
    rows = cur.fetchall()
    return rows

def membacaIDAnggota(id):
    cur.execute(f"""select id_anggota from peminjaman where id_peminjaman = {id}""")
    
    data = cur.fetchall()
    
    return data

def bacaDataDenda():
    cur.execute(f"select dd.id_denda, dd.jumlah_denda, ap.nama from data_denda dd join anggota_perpustakaan ap on (dd.id_anggota=ap.id_anggota)")
    
    data = cur.fetchall()
    
    return data

def menarikDataDenda(id_anggota):
    cur.execute(f"select* from data_denda where id_anggota = {id_anggota}")
                    
    data = cur.fetchone()
    
    if data:
        return data
    
    return None

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
    