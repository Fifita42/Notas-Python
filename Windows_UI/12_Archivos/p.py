from tkinter import *
from tkinter import filedialog#submodulo

def openFile():
    filepath=filedialog.askopenfilename(initialdir="D:\\Codigos\\Python",
                                        title='Abrir un archivo python',
                                        filetypes=(('Archivos de texto','*.txt'),('Archivos python','*.py')),
                                        )
    print(filepath)
    file = open(filepath,'r')
    print(file.read())
    file.close()
window = Tk()

button = Button(window,text='Abrir',command=openFile)
button.pack()
window.mainloop()