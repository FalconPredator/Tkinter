from tkinter import *
from tkinter import ttk
root = Tk()

button1 = ttk.Button(root, text='Button 1')
button2 = ttk.Button(root, text='Button 2')

button1.pack()
button2.pack() # .pack() if added in the line above, will not get a button type calling button1

style = ttk.Style()
# style constructor method
print(style.theme_names())
# get all the theme names available

print(style.theme_use())
# get the current theme

style.theme_use('classic')
style.theme_use('vista')
# change the theme


# Widget Style Names:
# Tbutton, TFrame, TCombobox, TPanedwindow are the default style widget name
# Treeview (no extra "T") 
# Horizontal.TScale or Vertical.TScale
# Horizontal.TScrollbar or Vertical.TScrollbar
# Horizontal.TProgressbar or Vertical.TProgressbar


print(button1.winfo_class())
# get the current style name of button1

style.configure('TButton', foreground='blue')
# configure the default style

style.configure('Alarm.TButton', foreground='orange', font=('Arial', 24, 'bold'))
# create a new custumed style named Alarm, derived from TButton default style
# all the TButton style properties will be inherited except for new configuration

##style.configure('Alarm.Tbutton') # this not working

button2.config(style='Alarm.TButton')

style.map('Alarm.TButton', foreground=[('pressed', 'pink'), ('disabled','grey')])
# map method to the style when events happend, foreground will be change to pink when its pressed :[(state1, property1), (state2, property2)]




# each style is composed of different elements. each element contains different options:

print(style.layout('TButton'))
# get the elements of TButton Style

print(style.element_options('Button.label'))
# get all the available options for the label element, which is a layout of TButton Style

print(style.lookup('TButton', 'foreground'))
# to lookup the current property value of a style 



