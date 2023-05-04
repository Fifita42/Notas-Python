from tkinter import *
from Ball import *
import time
window = Tk()


WIDTH = 500
HEIGHT = 500

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,10,15,"white")
tenis_ball = Ball(canvas,0,0,50,15,10,"yellow")
basquet_ball = Ball(canvas,0,0,125,8,7,"orange")

while True:
    volley_ball.move()
    tenis_ball.move()
    basquet_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()