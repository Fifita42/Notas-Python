from tkinter import *

window = Tk()
window.title("Mi app")
photo = PhotoImage(file='like.png')

food = ['pizza','pizza2','pizza3']

x = IntVar()
def order():
    print("Ordenaste: ",food[x.get()])
   
        
for index in range(len(food)):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index,
                              padx=25,
                              font=('Impact',50),
                              image=photo,
                              compound='left',
                              indicatoron=0,#elimina el radio
                              width=375,
                              command=order
                              )
    radiobutton.pack(anchor=W)


window.mainloop()