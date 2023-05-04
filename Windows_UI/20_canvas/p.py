from tkinter import *
window = Tk()

canvas = Canvas(window,height=500,width=500)

# canvas.create_line(0,0,500,500,fill="blue",width=5)
# canvas.create_line(0,500,500,0,fill="red",width=5)
# canvas.create_rectangle(50,50,250,250,fill="purple")

# points = [250,0,500,500,0,500]
# canvas.create_polygon(points,fill="yellow",outline="black",width=5)

                                                        #grados
canvas.create_arc(0,0,500,500,fill="green",style=CHORD,start=90,extent=180)
#styles:
#PIESLICE
#ARC


canvas.pack()


window.mainloop()