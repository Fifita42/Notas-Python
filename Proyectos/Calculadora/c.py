from tkinter import *
from tecla import *
def button_press(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)
    
def equals():
    global equation_text
    try:
        total = str(eval(equation_text))
        equation_label.set(total)
        equation_text = total
    except SyntaxError:
        equation_label.set("Error de sintaxis.")
    except ZeroDivisionError:
        equation_label.set("Error aritmetico.")

def clear():
    global equation_text
    equation_label.set("")
    equation_text = ""

window = Tk()
window.title("Calculadora")
window.geometry("500x500")

equation_text = ""

equation_label = StringVar()

label = Label(window,textvariable=equation_label,font=('Consolas',20),bg="white",width=24,height=2)
label.pack()

frame = Frame(window)
frame.pack()

button1 = Tecla(frame,1,0,0,button_press)
button2 = Tecla(frame,2,0,1,button_press)
button3 = Tecla(frame,3,0,2,button_press)
button4 = Tecla(frame,4,1,0,button_press)
button5 = Tecla(frame,5,1,1,button_press)
button6 = Tecla(frame,6,1,2,button_press)
button7 = Tecla(frame,7,2,0,button_press)
button8 = Tecla(frame,8,2,1,button_press)
button9 = Tecla(frame,9,2,2,button_press)
button0 = Tecla(frame,0,3,0,button_press)


plus = Button(frame,text='+',height=4,width=9,command=lambda:button_press('+'))
plus.grid(row=0,column=3)

minus = Button(frame,text='-',height=4,width=9,command=lambda:button_press('-'))
minus.grid(row=1,column=3)

por = Button(frame,text='*',height=4,width=9,command=lambda:button_press('*'))
por.grid(row=2,column=3)

divide = Button(frame,text='/',height=4,width=9,command=lambda:button_press('/'))
divide.grid(row=3,column=3)

equal = Button(frame,text='=',height=4,width=9,command=equals)
equal.grid(row=3,column=2)

decimal = Button(frame,text='.',height=4,width=9,command=lambda:button_press('.'))
decimal.grid(row=3,column=1)

clearr = Button(window,text='Clear',height=4,width=12,command=clear)
clearr.pack()

window.mainloop()