from tkinter import *

window = Tk()
window.title("Mi app")
window.config(background="#078ff7")
photo = PhotoImage(file='like.png')

def submit():
    username = entry.get()
    print("Hello ",username)
    entry.config(state=DISABLED)

def delete():
    entry.delete(0,END)   
def backspace():
     entry.delete(len(entry.get())-1,END)
entry = Entry(window,
                font=("Arial",30),
                fg="#00FF00",
                bg="black",
                show="*"
                )
entry.insert(0,'Bob Esponja')
entry.pack(side=LEFT)

submit_button = Button(window,text='submit',command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,text='Delete',command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,text='backspace',command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()