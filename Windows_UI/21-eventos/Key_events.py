from tkinter import *
window = Tk()

def algo(event):
    label.config(text=("Presionaste: "+event.keysym))
    print("Presionaste: "+event.keysym)

window.bind("<Key>",algo)

label = Label(window,font=("Helvetica",100))
label.pack()
window.mainloop()