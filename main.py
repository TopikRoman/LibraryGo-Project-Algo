
from tkinter import Tk
from lib.pages import login, dashboard, DataBuku, DataAnggota



if __name__ == "__main__" :
     
    akun = login.loginPage()
    
    if len(akun) != 0 :
        loop = 1
        while loop :
            targetMenu = dashboard.dashboard(akun[0][0])
            
            print(targetMenu)

            if len(targetMenu) <= 0 :
                break
        
            match targetMenu[0] :
                case 'Data Buku' :
                    print("1")
                    loop = DataBuku.tampilanDataBuku(akun[0][0])
                case 'Data Anggota' :
                    loop = DataAnggota.DataAnggota()
                case _ :
                    print("Keluar...")
            print(f"Target {targetMenu}")
        

            
        
