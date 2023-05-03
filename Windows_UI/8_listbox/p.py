from tkinter import *
window = Tk()

def submit():
    food = []   #Como la seleccion multiple esta activada,curselection devolvera una tupla con los indices
    for index in listbox.curselection():
        food.insert(index,listbox.get(index)) 

    print("Compraste: ")
    for index in food:
        print(index)

def add():
    listbox.insert(listbox.size(),entryBox.get())
    listbox.config(height=listbox.size())
def delete():
    for index in listbox.curselection():
        listbox.delete(index)
    listbox.config(height=listbox.size())
listbox=Listbox(window,
                bg='#f7ffde',
                font=('Constantia',35),
                width=12,
                selectmode=MULTIPLE#cuantos puede seleccionar a la vez
                )
listbox.pack()
listbox.insert(1,'Pizza')
listbox.insert(2,'Pasta')
listbox.insert(3,'Garlic')
listbox.insert(4,'Soup')
listbox.insert(5,'Salad')
listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()

submitButtom = Button(window,text="Submit",command=submit)
submitButtom.pack()

addButton = Button(window,text="Add",command=add)
addButton.pack()

deleteButton = Button(window,text="Delete",command=delete)
deleteButton.pack()

window.mainloop()