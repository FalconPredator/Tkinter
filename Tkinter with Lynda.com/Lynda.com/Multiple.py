from tkinter import *
from tkinter import ttk

root = Tk()

label1 = ttk.Label(root, text='Label 1')
label2 = ttk.Label(root, text='Label 2')
label1.pack()
label2.pack()

label1.bind('<ButtonPress>', lambda e: print('<ButtonPress> Label'))
label1.bind('<1>', lambda e: print('<1> Label'))



root.bind('<1>', lambda e: print('<1> Root'))
# binding to a top-level window

label1.unbind('<1>')
label1.unbind('<ButtonPress>')


root.bind_all('<Escape>', lambda e: print('<Escape!>'))
root.mainloop()

# When a widget is binded to several events
# Tk does its best to pick the binding that most closedly matches the action that occurs
# <1> is more specific than <ButtonPress>, so it prints out the first bind
# When the one widget is bound to an event, and the widget's master is also bound, it will triger 1, widget event. 2, master event
