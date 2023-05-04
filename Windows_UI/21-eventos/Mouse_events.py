from tkinter import *
window = Tk()

def clickIzq(event):
    label.config(text=("Presionaste: Click Izquierdo"))
    print("Presionaste: Click Izquierdo")
def ruedaBoton(event):
    label.config(text=("Presionaste: Boton central de la rueda"))
    print("Presionaste: Boton central de la rueda")
def clickDEr(event):
    label.config(text=("Presionaste: Click Derecho"))
    print("Presionaste: Click Derecho")
def soltar(event):
    label.config(text=("Soltaste un boton."))
    print("Coordenadas del mouse: "+str(event.x)+", "+str(event.y))
def entrasteEnLaVentana(event):
    label.config(text=("Vienvenido al mouseProgram."))
def salisteDeLaVentana(event):
    label.config(text=("Adios."))
def mover(event):
    print("Te moviste")


window.bind("<Button-1>",clickIzq)
window.bind("<Button-2>",ruedaBoton)
window.bind("<Button-3>",clickDEr)
window.bind("<ButtonRelease>",soltar)
window.bind("<Enter>",entrasteEnLaVentana)
window.bind("<Leave>",salisteDeLaVentana)
window.bind("<Motion>",mover)

label = Label(window,font=("Helvetica",100))
label.pack()
window.mainloop()