from tkinter import *
from tkinter.ttk import *
import time

window = Tk()
percent = StringVar()
text = StringVar()

def start():
    GB = 200
    downloaded = 0
    speed = 1
    while downloaded<GB: 
        time.sleep(0.05)
        bar['value']+=(speed/GB)*100#alargo el porcentaje de la barra
        downloaded+=speed
        percent.set(str(int((downloaded/GB)*100))+"%")#muestro el porcentaje actual en la barra
        text.set(str(downloaded)+"/"+str(GB)+" GB descargados")#tarea actual de 10
        print(downloaded)


bar = Progressbar(window,orient=HORIZONTAL,length=300)
bar.pack(pady=10)

percentLabel = Label(window,textvariable=percent).pack()
taskLabel = Label(window,textvariable=text).pack()

button = Button(window,text="download",command=start).pack()

window.mainloop()
