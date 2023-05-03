from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title='Este es un info message box',message='Sos una persona')
    
    messagebox.showwarning(title='Este es un warning message box',message='Virus')
    
    messagebox.showerror(title='Este es un error message box',message='Error')
    
    if messagebox.askokcancel(title='ask ok cancel',message='Quieres hacer algo?'):
        print('Pues hiciste algo.')
    else:
        print('Pues no hiciste nada.')
        
    if messagebox.askretrycancel(title='ask retry cancel',message='Quieres reintentar algo?'):
        print('Pues reintentaste algo.')
    else:
        print('Pues no reintentaste nada.')
    
    if messagebox.askyesno(title='ask yes no',message='Si o No?'):
        print('Si.')
    else:
        print('No.')

    respuesta = messagebox.askquestion(title='Ask question',message='Te gusta el pay?')
    if respuesta == 'yes':
        print('Si.')
    else:
        print('No.')

    respuesta = messagebox.askyesnocancel(title='Ask yes no cancel',message='Te gusta el pay?',icon='error')
    if respuesta == True:
        print('Si.')
    elif respuesta == False:
        print('No.')
    else:
        print('Cancelar.')

window = Tk()
button = Button(window,command=click,text='Click me')
button.pack()


window.mainloop()