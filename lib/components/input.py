from customtkinter import CTkEntry

def input(parent, placeholder) :
    input = CTkEntry(parent, width=250, fg_color='#FAFAFA', text_color='Black', placeholder_text=f"Masukkan {placeholder}")
    input.pack(padx=10, pady=10)

    return input