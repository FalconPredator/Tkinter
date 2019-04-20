from tkinter import *
from tkinter import ttk
root =  Tk()


entry = ttk.Entry(root, width=30) # width specify the width by character
entry.pack()
entry.get() # get the entry field

entry.delete(0, 1) # 1 ins not included
entry.delete(0, END) # to delete from 0 till end



entry.config(show='*') # to just show * when inputting

entry.state(['disabled']) # to disable the entry widget's state
entry.state(['!disabled'])

entry.state(['readonly']) # a special read-only state for entry
