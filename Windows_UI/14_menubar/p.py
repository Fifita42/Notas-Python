from tkinter import *
from tkinter import filedialog#submodulo

window = Tk()
imagen = PhotoImage(file='item.png')
def openfile():
    print("El archivo fue abierto")
def savefile():
    print("El archivo fue guardado")
def cut():
    print("Cortaste texto")
def copy():
    print("Copiaste texto")
def paste():
    print("pegaste texto")

menubar = Menu(window)
window.config(menu=menubar)

#---
fileMenu = Menu(menubar,tearoff=0,font=("MV Boli",15))
menubar.add_cascade(label='Archivo',menu=fileMenu)

fileMenu.add_command(label='Abrir',command=openfile,image=imagen,compound='left')
fileMenu.add_command(label='Guardar',command=savefile,image=imagen,compound='left')
fileMenu.add_separator()
fileMenu.add_command(label='Exit',command=quit,image=imagen,compound='left')

#---
editMenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Editar',menu=editMenu)

editMenu.add_command(label='Cortar',command=cut,image=imagen,compound='left')
editMenu.add_command(label='Copiar',command=copy,image=imagen,compound='left')
editMenu.add_command(label='Pegar',command=paste,image=imagen,compound='left')

window.mainloop()