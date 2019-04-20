from tkinter import *
from tkinter import ttk
root = Tk()

notebook = ttk.Notebook(root)
notebook.pack() # pack is geometry manager
frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)

notebook.add(frame1, text='tab1')
notebook.add(frame2, text='tab2')
# when call the tab method, it will add tab on the right

ttk.Button(frame1, text='Click Me').pack()
# when adding a button in frame1, frame2 will extend same size as frame1


frame3 = ttk.Frame(notebook)
notebook.insert(1, frame3, text='three')
# insert method(index of the tab, what to insert, what is the tabname)
# insert method is similar to add method, but index is specified

notebook.forget(1)
# forget method is not deleting the object, one can bring it up by calling add
notebook.add(frame3, text='Three')
# the add method will add widget to the right side

print(notebook.select())
# returns a object name with parent object's name
print(notebook.index(notebook.select()))
# returns the selected notebook tab index

notebook.select(1)
# defaultly select the tab

notebook.tab(1, state='disabled')
# tab method is like the config method of other widgets, disable the tab 1

notebook.tab(2, state='hidden')
# change it to hidden, but it does exists in the background

notebook.tab(2, state='normal')
# back to normal

print(notebook.tab(1, 'text'))
# get the text label of a tab

print(notebook.tab(1))
# get all the properties of a tab


