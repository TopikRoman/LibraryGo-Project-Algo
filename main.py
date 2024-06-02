
from tkinter import Tk
from lib.pages import login, dashboard, DataBuku, DataAnggota



if __name__ == "__main__" :
    loop = 1
    while loop :
        loop, akun = login.loginPage()
        
        while loop and len(akun) != 0 :
            loop, targetMenu, akun = dashboard.dashboard(akun)
            
            # print(targetMenu)

            # if len(targetMenu) <= 0 :
            #     break
            if len(targetMenu) > 0 :
                match targetMenu[0] :
                    case 'Data Buku' :
                        print("1")
                        loop = DataBuku.tampilanDataBuku(akun[0][0])
                    case 'Data Anggota' :
                        loop = DataAnggota.DataAnggota()
                    case _ :
                        print("Keluar...")
                print(f"Target {targetMenu}")
        

            
        
