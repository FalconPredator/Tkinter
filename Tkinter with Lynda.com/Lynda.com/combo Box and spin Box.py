from tkinter import *
from tkinter import ttk
root = Tk()
month = StringVar()
combobox = ttk.Combobox(root, textvariable=month)
combobox.pack()
combobox.config(values=('Jan','Feb','Mar','Apr','May','Jun','Jul',
                        'Aug','Sep','Oct','Nov','Dec')) # a tuple


month.set('Dec') # to preset the value
print(month.get())


# spin box is not available in the ttk widgets !
year =StringVar()
Spinbox(root, from_=1990, to=2014, textvariable=year).pack()
# if I dont specify textvariable in this case still works, but set and get method are not able to use

year.get()
year.set(2005)
