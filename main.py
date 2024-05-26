from tkinter import Tk
from lib.pages import login, dashboard, tambahBuku, tambahAnggota




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
    print(akun)
    
    while True :
        targetMenu = dashboard.dashboard()
        print(targetMenu)

        match targetMenu[0] :
            case 'Data Peminjaman' :
                tambahBuku.tambahBuku()
            case 'Data Anggota' :
                tambahAnggota.TambahAnggota()
            case _ :
                print("Keluar...")
        print(f"Target {targetMenu}")
        

            
        
