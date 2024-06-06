
from tkinter import Tk
from lib.pages import login, dashboard, DataBuku, DataAnggota, DataPustakawan, Profile



if __name__ == "__main__" :
    loop = 1
    while loop :
        loop, akun = login.loginPage()
        
        while loop and len(akun) != 0 :
            loop, targetMenu, akun = dashboard.dashboard(akun)

            if len(targetMenu) > 0 :
                match targetMenu[0] :
                    case "Profile":
                        loop = Profile.showProfile(akun)
                    case 'Data Buku' :
                        print("1")
                        loop = DataBuku.tampilanDataBuku(akun)
                    case 'Data Anggota' :
                        loop = DataAnggota.DataAnggota(akun)
                    case 'Data Pustakawan':
                        loop = DataPustakawan.DataPustakawan(akun)
                    case _ :
                        print("Keluar...")
                print(f"Target {targetMenu}")
        

            
        
