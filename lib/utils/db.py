import psycopg2

conn = psycopg2.connect(
    dbname="LibraryGo",
    user="postgres",
    password="19Januari",
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
