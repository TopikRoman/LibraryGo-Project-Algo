CREATE TABLE anggota_perpustakaan (
    id_anggota    INTEGER NOT NULL,
    nama          VARCHAR(50) NOT NULL,
    alamat        VARCHAR(50) NOT NULL,
    no_telepon    VARCHAR(15) NOT NULL,
    email         VARCHAR(50) NOT NULL,
    tanggal_lahir DATE NOT NULL
);

ALTER TABLE anggota_perpustakaan ADD CONSTRAINT anggota_perpustakaan_pk PRIMARY KEY ( id_anggota );

CREATE TABLE buku (
    id_buku        SERIAL NOT NULL,
    judul_buku     VARCHAR(50) NOT NULL,
    tahun_terbit   VARCHAR(4) NOT NULL,
    penerbit       VARCHAR(50) NOT NULL,
    id_genre 	   INTEGER NOT NULL
);

ALTER TABLE buku ADD CONSTRAINT buku_pk PRIMARY KEY ( id_buku );

CREATE TABLE data_denda (
    id_denda                        INTEGER NOT NULL,
    jumlah_denda                    INTEGER NOT NULL, 
    id_anggota                      INTEGER NOT NULL,
    status_denda                    CHAR(1) NOT NULL
);

ALTER TABLE data_denda ADD CONSTRAINT data_denda_pk PRIMARY KEY ( id_denda );

CREATE TABLE detail_peminjaman (
    id_detail                       INTEGER NOT NULL,
    id_peminjaman                   INTEGER NOT NULL, 
    id_anggota                      INTEGER NOT NULL,
    id_buku                    		INTEGER NOT NULL
);

ALTER TABLE detail_peminjaman ADD CONSTRAINT detail_peminjaman_pk PRIMARY KEY ( id_detail );

CREATE TABLE genre (
    id_genre   INTEGER NOT NULL,
    nama_genre VARCHAR NOT NULL
);

ALTER TABLE genre ADD CONSTRAINT genre_pk PRIMARY KEY ( id_genre );

CREATE TABLE peminjaman (
    id_peminjaman        INTEGER NOT NULL,
    tanggal_peminjaman   DATE NOT NULL,
    tenggat_pengembalian DATE NOT NULL,
    nip       			 BIGINT NOT NULL,
    status_peminjaman    CHAR(1) NOT NULL
);

ALTER TABLE peminjaman ADD CONSTRAINT peminjaman_pk PRIMARY KEY ( id_peminjaman );

CREATE TABLE pustakawan (
    nip           BIGINT NOT NULL,
    nama          VARCHAR(50) NOT NULL,
    alamat        VARCHAR(50) NOT NULL,
    no_telepon    VARCHAR(15) NOT NULL,
    email         VARCHAR(50) NOT NULL,
    tanggal_lahir DATE NOT NULL
);

ALTER TABLE pustakawan ADD CONSTRAINT pustakawan_pk PRIMARY KEY ( nip );

ALTER TABLE buku
    ADD CONSTRAINT buku_genre_fk FOREIGN KEY ( id_genre )
        REFERENCES genre ( id_genre );

ALTER TABLE data_denda
    ADD CONSTRAINT data_denda_anggota_perpustakaan_fk FOREIGN KEY ( id_anggota )
        REFERENCES anggota_perpustakaan ( id_anggota );

ALTER TABLE detail_peminjaman
    ADD CONSTRAINT detail_peminjaman_anggota_perpustakaan_fk FOREIGN KEY ( id_anggota )
        REFERENCES anggota_perpustakaan ( id_anggota );

ALTER TABLE detail_peminjaman
    ADD CONSTRAINT detail_peminjaman_buku_fk FOREIGN KEY ( id_buku )
        REFERENCES buku ( id_buku );

ALTER TABLE detail_peminjaman
    ADD CONSTRAINT detail_peminjaman_peminjaman_fk FOREIGN KEY ( id_peminjaman )
        REFERENCES peminjaman ( id_peminjaman );

ALTER TABLE peminjaman
    ADD CONSTRAINT peminjaman_pustakawan_fk FOREIGN KEY ( nip )
        REFERENCES pustakawan ( nip );

#InsertData buku buat testing

INSERT INTO buku (judul_buku, tahun_terbit, penerbit, id_genre) VALUES
('To Kill a Mockingbird', '1960', 'HarperCollins Publishers', 1),
('1984', '1949', 'Penguin Books', 2),
('Pride and Prejudice', '1813', 'Penguin Classics', 3),
('The Great Gatsby', '1925', 'Scribner', 1),
('The Catcher in the Rye', '1951', 'Little, Brown and Company', 1),
('The Hobbit', '1937', 'Houghton Mifflin Harcourt', 1),
('Fahrenheit 451', '1953', 'Simon & Schuster', 1),
('Brave New World', '1932', 'Harper & Brothers', 1),
('The Lord of the Rings', '1954', 'Allen & Unwin', 1),
('Animal Farm', '1945', 'Secker & Warburg', 1),
('The Chronicles of Narnia', '1950', 'Geoffrey Bles', 1),
('Jane Eyre', '1847', 'Smith, Elder & Co.', 1),
('Wuthering Heights', '1847', 'Thomas Cautley Newby', 1),
('Frankenstein', '1818', 'Lackington, Hughes, Harding, Mavor & Jones', 1),
('Moby-Dick', '1851', 'Richard Bentley', 1),
('The Picture of Dorian Gray', '1890', 'Ward, Lock and Company', 1),
('Dracula', '1897', 'Archibald Constable and Company', 1),
('Romeo and Juliet', '1597', 'Penguin Classics', 1)

INSERT INTO pustakawan (nip, nama, alamat, no_telepon, email, tanggal_lahir) VALUES
(123456789012345678, 'Andi Wijaya', 'Jl. Merpati No. 10, Jakarta', '081234567890', 'andi.wijaya@example.com', '1985-03-12'),
(234567890123456789, 'Budi Santoso', 'Jl. Kenari No. 20, Bandung', '082345678901', 'budi.santoso@example.com', '1978-07-24'),
(345678901234567890, 'Citra Lestari', 'Jl. Melati No. 30, Surabaya', '083456789012', 'citra.lestari@example.com', '1990-11-05');

INSERT INTO anggota_perpustakaan (id_anggota, nama, alamat, no_telepon, email, tanggal_lahir) VALUES
(123456, 'Eka Putra', 'Jl. Anggrek No. 5, Yogyakarta', '081234567890', 'eka.putra@example.com', '1992-01-15'),
(234567, 'Fajar Setiawan', 'Jl. Cempaka No. 15, Semarang', '082345678901', 'fajar.setiawan@example.com', '1988-06-21'),
(345678, 'Gina Rahma', 'Jl. Flamboyan No. 25, Bali', '083456789012', 'gina.rahma@example.com', '1995-10-30');