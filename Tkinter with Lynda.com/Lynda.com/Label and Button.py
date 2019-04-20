from tkinter import *
from tkinter import ttk

root = Tk()
Label(root, text="Hello, Tkinter").pack()
# wraplength=300: to change the text variable not running horizontally


def callback():
    print('Clicked!')
button = ttk.Button(root, text='Click Me')
button.config(command=callback) # config a command



#button.invoke() # simulate a click on the button
button.state(['disabled']) # disable the button
button.instate(['disabled']) # check if the button in the sate of ['disabled']
button.state(['!disabled']) # enable the button
button.instate(['!disabled']) # check if the button in the sate of ['not disabled']

logo = PhotoImage(file = 'python.gif')

logo = PhotoImage(file = 'python.gif') # make an image object, gif is preffered
button.config(image = logo, compound =LEFT) # config a image into button

small_logo = logo.subsample(5, 5) # resample the image sorted by 5*5 pixels
button.config(image = small_logo) # reconfigure the button
button.pack()
root.mainloop()
