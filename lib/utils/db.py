import psycopg2

conn = psycopg2.connect(
    dbname="LibraryGo",
    user="postgres",
    password="rendydp424",
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

    if len(password) == 8 :
        table = 'pustakawan'
        primaryKey = 'nip'
    elif len(password) == 6 :
        table = 'anggota_perpustakaan'
        primaryKey = 'nip'

    cur.execute(f"SELECT * FROM {table} WHERE email = '{username}' AND {primaryKey} = '{password}'")
    
    data = cur.fetchall()

    if len(data) == 0 :
        return 'Akun tidak ditemukan'
    
    return data
