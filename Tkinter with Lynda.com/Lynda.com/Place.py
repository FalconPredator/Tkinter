from tkinter import *
from tkinter import ttk

root = Tk()

root.geometry('640x480+200+200')



ttk.Label(root, text='Yellow', background='yellow').place(x=100, y=50, width=100, height=50)
ttk.Label(root, text='Blue', background='blue').place(relx=0.9, rely=0.6, anchor='center', relwidth=0.5, relheight=0.5)
ttk.Label(root, text='Green', background='green').place(relx=0.5, x=100, rely=0.5, y=50)
ttk.Label(root, text='Orange', background='orange').place(relx=1.0, x=-5, y=5, anchor='ne')

# x, y is pixels placed in the parent
# relx, rely are the percentage rate between 0 and 1 placed in the parent
# relwidth, relheight: the height and width should be the percentage of the parent



root.mainloop()


# the other place methods, same with grid and pack:
place_slaves()
place_configure()
place_info()
place_forget()

























# Place Geometry Manager:
# Provides exact congrol of widget location and size
# Describe location in absolute and/or relative terms
# The major difference of place and grid/pack is it manage the widget in the parent itself rather than relative to the children

