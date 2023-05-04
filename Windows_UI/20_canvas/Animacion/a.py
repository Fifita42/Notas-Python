from tkinter import *
import time
window = Tk()

WIDTH = 1000
HEIGHT = 1000
xVELOCITY = 10
yVELOCITY = 15
canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

photo = PhotoImage(file='nave.png')
nave = canvas.create_image(0,0,image=photo,anchor=NW) 

image_width = photo.width()
image_height = photo.height()

while True:
    coordenadas = canvas.coords(nave)
    print(coordenadas)
    
    if (coordenadas[0] >= (WIDTH-image_width) or coordenadas[0] < 0):
        xVELOCITY= -xVELOCITY
    if (coordenadas[1] >= (HEIGHT-image_height) or coordenadas[1] < 0):
        yVELOCITY= -yVELOCITY
    
    canvas.move(nave,xVELOCITY,yVELOCITY)
    window.update()
    time.sleep(0.01)
    

window.mainloop()