from tkinter import *
from tkinter import ttk

root = Tk()



def callback():
    print(checkbutton.instate(['selected']))

checkbutton = ttk.Checkbutton(root, text='Spam?', command=callback)
checkbutton.pack()

spam = StringVar() # set a string variable
spam.set('SPAM!')
print(spam.get())

checkbutton.config(variable=spam, onvalue='Yes SPAM', offvalue='Not SPAM')


breakfast = StringVar()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()
ttk.Radiobutton(root, text='Eggs', variable=breakfast, value='Eggs').pack()
ttk.Radiobutton(root, text='Sausage', variable=breakfast, value='Sausage').pack()
ttk.Radiobutton(root, text='SPAM', variable=breakfast, value='SPAM').pack()


checkbutton.config(textvariable=breakfast)


# tkinter variable classes:
# BolleanVar DoubleVar IntVar StringVar




##>>> spam.get()
##'SPAM!'
##>>> True
##True
##True
##>>> spam.get()
##'Yes SPAM'
##>>> False
##False
##False
##>>> spam.get()
##'Not SPAM'
##>>> 
