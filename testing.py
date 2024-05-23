from tkinter import *
from tkinter import ttk

def click() :
    output_text.insert(INSERT, "Success\n")

window = Tk()
window.geometry()
window.title('Page 1')

info = ttk.Style()
info.configure('Info.TFrame', background='blue', borderWidth=5)

frame = ttk.Frame(window, width=500, height=500, padding="10").grid(column=0, row=0, sticky=(N,W,E,S))


button = ttk.Button(frame, text="CLICK", command=click).grid(column=0, row=0, sticky=(N, E))
# button.pack()

#Output Window test
output_text = Text(frame, width=10, height=10)
output_text.grid(column=1, row=0, sticky=(N, E, W, S))

window.mainloop()