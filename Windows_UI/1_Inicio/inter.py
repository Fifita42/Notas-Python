from tkinter import *
#Widgets = GUI elements: buttons, texboxes, labels, images, etc
#Windows = serves as a container to hold or contain these widgets 

#Instanciar una ventana
window = Tk()
#dimensiones de la ventana
window.geometry("420x420")
#Titulo de la app
window.title("Mi app")
#logo del programa
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
#configuracones
window.config(background="#078ff7")
window.mainloop()#ventana en la pantalla de la pc. escucha eventos