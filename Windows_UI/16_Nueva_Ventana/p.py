#Un fram es un contenedor rectangular para agrupar y contener widgets
from tkinter import *
old_window = Tk()

def create_window():
    new_window = Toplevel()#si cierro la original, se cierra la nueva ventana
    #Tk(): crea una nueva ventana independiente de la original
    #old_window.destroy(): cerrara la ventana vieja
Button(old_window,text="W",font=("Consolas",25),width=3,command=create_window).pack(side=TOP)

old_window.mainloop()