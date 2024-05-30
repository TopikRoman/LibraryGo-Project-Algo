from tkinter import Tk
from lib.pages import login, dashboard, DataBuku, DataAnggota




if __name__ == "__main__" :
    # app = Tk()
    # app.geometry('720x420')
    # app.title("Login")

    # akun, login = loginPage(app)
    # login.pack(padx=10, pady=100, anchor="center")


    # app.mainloop()

    # while True :
    #     akun = loginPage()
        
    #     if len(akun) == 0 :
    #         continue

    #     dashboard()

     
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
        

            
        
