from tkinter import *

class Tecla:
    def __init__(self,frame,tecl,ROW,COL,button_press):
        self.frame = frame
        self.tecl = Button(self.frame,text=tecl,height=4,width=9,command=lambda:button_press(tecl))
        self.tecl.grid(row=ROW,column=COL)
