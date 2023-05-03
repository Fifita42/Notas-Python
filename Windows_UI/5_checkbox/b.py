from tkinter import *

window = Tk()
window.title("Mi app")
window.config(background="#078ff7")
photo = PhotoImage(file='like.png')

x = IntVar()
def display():
    if(x.get()==1):
        print("Estas De Acuerdo.")
    else:
        print("No Estas De Acuerdo.")
        
cjeck_button = Checkbutton(window,
                           text="Estoy de acuerdo con algo",
                           variable=x,
                           onvalue=1,#puede ser cualquier cosa, true, false, etc
                           offvalue=0,##igual que el de arriba
                           command=display,
                           font=('Arial',20),
                           fg='green',
                           bg='black',
                           activeforeground='black',
                           activebackground='green',
                           padx=25,
                           pady=10,
                           image=photo,
                           compound=LEFT
                )
cjeck_button.pack()


window.mainloop()