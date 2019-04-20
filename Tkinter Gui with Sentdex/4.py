import tkinter as tk

LARGE_FONT = ('Verdana', 12)

class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs) # arguments and keyword arguments
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne, PageTwo):
            
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

def qf(var):
    print(var)

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text="Visit Page 1", command=lambda :controller.show_frame(PageOne))
        button1.pack()

        button2 = tk.Button(self, text="Visit Page 2", command=lambda :controller.show_frame(PageTwo))
        button2.pack()



class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = tk.Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = tk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="PageTwo", command=lambda :controller.show_frame(PageTwo))
        button2.pack()


class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   
        # super().__init__(parent) can also do, this is to call the parent tk.Frame __init__ method in order to use its variable
        label = tk.Label(self, text="PageTwo", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = tk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
        button1.pack()

        button2 = tk.Button(self, text="Page One", command=lambda :controller.show_frame(PageOne))
        button2.pack()


app = SeaofBTCapp()
app.mainloop()
# print(help(SeaofBTCapp))
print(help(StartPage))
    






