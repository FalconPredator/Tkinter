from tkinter import *
from tkinter import ttk
root = Tk()
frame = ttk.Frame(root)
frame.pack()
frame.config(height=100, width=200)
# There are 6 diferent types of frame "Relief" you can choose
frame.config(relief=RIDGE)
ttk.Button(frame, text='Click Me').grid()


frame.config(padding=(30, 15))
# with padding could add a buffering space for the children widgets

ttk.LabelFrame(root, height=100, width=200, text='My Frame').pack()
# downside with labelframe: there is no relief in labelframe
