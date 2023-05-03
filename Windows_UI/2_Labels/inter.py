from tkinter import *
window = Tk()
window.geometry("420x420")
window.title("Mi app")
window.config(background="#078ff7")
photo = PhotoImage(file='logo.png')
#crear
label = Label(window,
              text="Hola mundo",
              font=('Arial',40,'bold'),
              fg='green',bg='black',
              relief=RAISED,#borde del label
              bd=1,#grosor del borde
              padx=20,#padding izquierda y derecha
              pady=20,#padding arriba y abajo
              image=photo,
              compound='top'#donde estara la imagen
              )

#colocar en el centro
label.pack()
#colocar y poscicionar o solo posicionar
# label.place(x=0,y=0)


window.mainloop()