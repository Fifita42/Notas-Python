from tkinter import *

window = Tk()
window.geometry("1000x1000")
auto = PhotoImage(file='auto.png')

def move_up(event):
    canvas.move(car,0,-10)
    
def move_down(event):
    canvas.move(car,0,10)
    
def move_left(event):
    canvas.move(car,-10,0)
    
def move_right(event):
    canvas.move(car,10,0)


canvas = Canvas(window,width=1000,height=1000)
canvas.pack()
car = canvas.create_image(0,0,image=auto,anchor=NW)


window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)

window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)

window.mainloop()