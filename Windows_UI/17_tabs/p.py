from tkinter import *
from tkinter import ttk

window = Tk()
notebook = ttk.Notebook(window)#item que maneja una coleccion de ventanas/displays

tab1 = Frame(notebook)
tab2 = Frame(notebook)

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")
notebook.pack(expand=True,fill="both")#expand=True: expande toda la nota por los espacios bacios
                            #fill = both: llena el espacio en x y axis
Label(tab1,text="Hello, este texto es del tab #1",width=50,height=25).pack()
Label(tab2,text="Hello, este texto es del tab #2",width=50,height=25).pack()
window.mainloop()