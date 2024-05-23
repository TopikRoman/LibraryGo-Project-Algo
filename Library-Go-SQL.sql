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
    id_buku        INTEGER NOT NULL,
    judul_buku     VARCHAR(50) NOT NULL,
    tahun_terbit   DATE NOT NULL,
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
    nip       			 INTEGER NOT NULL,
    status_peminjaman    CHAR(1) NOT NULL
);

ALTER TABLE peminjaman ADD CONSTRAINT peminjaman_pk PRIMARY KEY ( id_peminjaman );

CREATE TABLE pustakawan (
    nip           INTEGER NOT NULL,
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