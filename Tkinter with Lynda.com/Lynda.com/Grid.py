from tkinter import *
from tkinter import ttk
root = Tk()

# the Grid/Pack/Place Manager will submmit to its parent manager
# eg., the first widget of the second frame will be row=0, column=0




##ttk.Label(root, text='Yellow', background='yellow').grid(row=1, column=1)
##ttk.Label(root, text='Blue', background='blue').grid(row=1, column=0)
##ttk.Label(root, text='Green', background='green').grid(row=0, column=0)
##ttk.Label(root, text='Orange', background='orange').grid(row=0, column=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=3)
# configure the root window: when row 0 expands 1 pixels when the window is reized, row 1 expands 3 pixels
# when resize is not defined, the grid cell will stays as small as possible when the parent widget is resized
# if weight=0, the widget will not expand
root.columnconfigure(2, weight=1)




ttk.Label(root, text='Yellow', background='yellow').grid(row=0, column=2, rowspan=2, sticky='nesw')
ttk.Label(root, text='Blue', background='blue').grid(row=1, column=0, columnspan=2, sticky='nesw')
ttk.Label(root, text='Green', background='green').grid(row=0, column=0, sticky='nesw', padx=10, pady=10)
ttk.Label(root, text='Orange', background='orange').grid(row=0, column=1, sticky='nesw', ipadx=25, ipady=25)

# rowspan will make the widget across two rows or columns, but it still be put in the center of the grid allocator
# row and column is not pixels
# sticky/stick = 'nwse', make the widget to stick to the very direction of its own cell
root.mainloop()




grid_slaves()
grid_configure()
grid_info()
grid_forget()
# this functions the same with pack manager
