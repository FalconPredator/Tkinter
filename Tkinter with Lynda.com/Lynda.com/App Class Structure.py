from tkinter import *
from tkinter import ttk

class HelloApp:
    def __init__(self, master): # master will be equals to root(its parent)
        self.label = ttk.Label(master, text='Hello, tkinter!')
        self.label.grid(row=0, column=0, columnspan=4)

        ttk.Button(master, text='Texas', command=self.texasHello).grid(row=1, column=0)
        ttk.Button(master, text='Hawaii', command=self.hawaiiHello).grid(row=1, column=1)

    def texasHello(self):
        self.label.config(text='Howdy, Texas')

    def hawaiiHello(self):
        self.label.config(text='Howdy, Hawaii')


def main():
    root = Tk()
    app = HelloApp(root)
    root.mainloop()

if __name__ == '__main__':
    main()
