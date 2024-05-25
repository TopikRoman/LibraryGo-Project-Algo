import psycopg2

def fetch_books():
    conn = psycopg2.connect(
        dbname="Library_Go",
        user="postgres",
        password="19Januari",
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM buku")
    #id_buku[0], judul_buku[1], id_genre[2]
    buku = cur.fetchall()
    cur.close()
    conn.close()
    return buku

def merge_sort(buku, pembeda = 4):
    if len(buku) > 1:
        mid = len(buku) // 2
        left_half = buku[:mid]
        right_half = buku[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            #left_half[i][2] dan right_half[j][2] merujuk ke id_genre dari buku.
            #left_half[i][1] dan right_half[j][1] merujuk ke judul_buku dari buku.
            if left_half[i][pembeda] < right_half[j][pembeda] or (left_half[i][pembeda] == right_half[j][pembeda] and left_half[i][1] < right_half[j][1]):

                buku[k] = left_half[i]
                i += 1

            else:
                buku[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            buku[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            buku[k] = right_half[j]
            j += 1
            k += 1

def cari_indeks(arr, target, batas_bawah, batas_atas):
    # menerima argumen arr (array),
    # target (nilai yang dicari),
    # batas_bawah (indeks bawah),
    # dan batas_atas (indeks atas)
    # mengimplementasikan algoritma binary search untuk mencari indeks dari target dalam array arr
    while batas_bawah <= batas_atas:
        # pencarian akan terus berlanjut selama batas_bawah tidak melebihi batas_atas
        tengah = (batas_bawah + batas_atas) // 2
        # menghitung indeks tengah sebagai pembulatan ke bawah hasil penjumlahan batas_bawah dan batas_atas dibagi dua
        if arr[tengah] == target:
            # memeriksa apakah nilai pada arr[tengah] sama dengan target
            # jika iya, berarti kita telah menemukan indeks yang mengandung target,
            # sehingga langsung mengembalikan tengah
            return tengah
        elif arr[tengah] < target:
            # maka perlu dilakukan pencarian di setengah bagian kanan dari array
            # oleh karena itu, batas_bawah diperbarui menjadi tengah + 1 untuk menggeser
            # rentang pencarian ke bagian kanan array
            batas_bawah = tengah + 1
        else:
            batas_atas = tengah - 1
            # batas_atas diperbarui menjadi tengah - 1 untuk
            # menggeser rentang pencarian ke bagian kiri array
    # jika tidak ada indeks yang ditemukan yang mengandung target dalam rentang pencarian,
    # maka loop akan terus berlanjut hingga batas_bawah melampaui batas_atas
    # pada saat itu, akan dikembalikan nilai -1 untuk menunjukkan bahwa target tidak ditemukan dalam array
    return -1

def print_books(buku):
    for book in buku:
        print(book)

if __name__ == "__main__":
    buku = fetch_books()
    print("Buku sebelum sorting:")
    print_books(buku)
    
    merge_sort(buku)
    
    print("\Buku setelah sorting:")
    print_books(buku)


# INSERT TO DATABASE TABLE BUKU
# INSERT INTO genre (id_genre, nama_genre) VALUES
# (1, 'Fiction'), (2, 'Non-Fiction'), (3, 'Science'), (4, 'History'), (5, 'Biography');

# -- insert 100 buku into the buku table
# DO $$
# BEGIN
#     FOR i IN 1..80 LOOP
#         INSERT INTO buku (id_buku, judul_buku, tahun_terbit, penerbit, id_genre)
#         VALUES (i, 'Book ' || i, '2000-01-01', 'Publisher ' || i, i % 5 + 1);
#     END LOOP;
#     FOR i IN 81..100 LOOP
#         INSERT INTO buku (id_buku, judul_buku, tahun_terbit, penerbit, id_genre)
#         VALUES (i, 'Book ' || i, '2000-01-01', 'Publisher ' || i, 1); -- Genre 1 for 20 books
#     END LOOP;
# END $$;
