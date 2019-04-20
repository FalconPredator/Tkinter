from tkinter import *
from tkinter import ttk

root = Tk()

label = ttk.Label(root, text='hello, tkinter!', background='yellow', anchor='nw')
label.pack(fill=BOTH, expand=True, side=LEFT, padx=10, pady=10, ipadx=20, ipady=20)
# fill = Uppercase X, fill the x direction
# fill = Uppercase BOTH, fill the x direction, but pack manager does not expand to fill
# expand=True to tell pack manager to expand
# side=LEFT to deside which side the widget should be packed
# anchor='nswe' to anchor the label('text') to the direction, note that not changing the expand or fill
# padx=10, pady=10: pixels, add the outside padding of the widget
# ipadx=10, ipady=10: add internal padding of the widget

label = ttk.Label(root, text='hello, tkinter!', background='blue')
label.pack(fill=BOTH, expand=False, side=LEFT)

label = ttk.Label(root, text='hello, tkinter!', background='green')
label.pack(fill=BOTH, side=LEFT)



for widget in root.pack_slaves():
    widget.pack_configure(fill=BOTH, expand=True)
# configure all the widget using pack manager in root window
    print(widget.pack_info())
# show each widget's pack manager setting, but not the widget property itself, such as background, foreground.

# in this example, expand is False, but pack manager simply takes it to expand


label.pack_forget()
# to forget the pack method, or ommiting it


root.mainloop()


