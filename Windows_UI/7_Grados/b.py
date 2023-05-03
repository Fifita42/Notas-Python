from tkinter import *

window = Tk()
window.title("Mi app")
photo = PhotoImage(file='like.png')

def submit():
    print("La temperatura es: ",str(scale.get()," grados C"))

scale = Scale(window,
              from_=100,
              to=0,
              length=600,#anchura o altura de la recta
              orient=HORIZONTAL,#posicion
              font=('Consolas',20),
              tickinterval=10,#Mostrar los numeros de 0 a 100 de 10 en 10
              showvalue = 0,#esconder el valor actual
              troughcolor='#69fafe',#color de la barra
              fg='#ff1c00',#color de los numeros
              bg='#111111'
              )
scale.set(50)#donde va a comenzar el valor
scale.pack()

button = Button(window,text="submit",command=submit)
window.mainloop()