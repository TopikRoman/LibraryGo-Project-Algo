from tkinter import Tk
from lib.pages.login import loginPage


if __name__ == "__main__" :
    # app = Tk()
    # app.geometry('720x420')
    # app.title("Login")

    # akun, login = loginPage(app)
    # login.pack(padx=10, pady=100, anchor="center")


    # app.mainloop()

    while True :
        akun = loginPage()
        
        if len(akun) == 0 :
            continue
            
        
