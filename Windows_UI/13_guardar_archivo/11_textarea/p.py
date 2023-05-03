from tkinter import *
from tkinter import filedialog#submodulo

window = Tk()

def savefile():
    file = filedialog.asksaveasfile(initialdir="D:\\Downloads",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Archivo de texto",".txt"),
                                        ("Archivo HTML",".html"),
                                        ("Archivo*",".*"),
                                    ])
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()
    
button = Button(window,text='submit',command=savefile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()