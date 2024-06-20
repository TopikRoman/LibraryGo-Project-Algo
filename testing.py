from lib.utils.db import menambahkanData, fetch_data, cur, conn, readAnggota, membacaPeminjaman, membacaDetailPeminjaman, membacaIDAnggota, menarikDataDenda


dataDendaLama = menarikDataDenda(345678)

databaru = dataDendaLama[1] + 5000

print(databaru)