from tkinter import *
from tkinter import ttk

def click() :
    print("Topik Kontol")

window = Tk()
window.geometry()
window.title('Page 1')

info = ttk.Style()
info.configure('Info.TFrame', background='blue', borderWidth=5)

frame = ttk.Frame(window, width=500, height=500, padding="10").grid(column=0, row=0, sticky=(N,W,E,S))


button = Button(frame, text="CLICK", command=click).grid(column=0, row=0, sticky=(N, E))
# button.pack()

window.mainloop()