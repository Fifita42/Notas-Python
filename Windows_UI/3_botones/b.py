from tkinter import *

window = Tk()
window.title("Mi app")
window.config(background="#078ff7")
photo = PhotoImage(file='like.png')

count = 0
def click():
    global count
    count += 1
    print(count)

button = Button(window,
                text="Click",
                command=click,
                font=("Comic Sans",30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="green",
                #state=ACTIVE,#DISABLED
                image=photo,
                compound="bottom"
                )
button.pack()
window.mainloop()