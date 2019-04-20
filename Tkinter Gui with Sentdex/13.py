# this video modifying the animate using json pandas and urllib 
import okex.account_api as account
import okex.ett_api as ett
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot

import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use("TkAgg") # change the backend

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.ticker as mticker
from matplotlib import pyplot as plt

import numpy as np
import pandas as pd
import urllib
import json

pd.set_option('max_columns', 50)
pd.set_option('display.width', 200)
pd.set_option('display.max_rows', 200)


LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)


style.use('ggplot')

f = Figure()
a = f.add_subplot(111)


exchange = "BTC-e"
DatCounter = 9000
programeName = "btce"


def changeExchange(toWhat, pn):
    global exchange
    global DatCounter
    global programeName

    exchange = toWhat
    programName = pn
    DatCounter = 9000


def popupmsg(msg):
    popup = tk.Tk()
    
    popup.wm_title("!")
    label = ttk.Label(popup, text=msg, font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)
    B1 = ttk.Button(popup, text="Okey", command=popup.destroy)
    B1.pack()
    popup.mainloop()


def animate(i): # i for interval
    subjectName = 'BTC-USD-181228'
    granularity = 60
    s_Time = '2018-11-18T00:00:00.081Z'
    e_Time = '2018-11-19T18:00:00.081Z'

    api_key = 'd921914b-0693-4ed1-b27e-1f5679e612f5'
    seceret_key = 'CD7F96CD31ADB4CB5B3D8200EA20745A'
    passphrase = '111111'

    spotAPI = spot.SpotAPI(api_key, seceret_key, passphrase, True)
    data = spotAPI.get_deal('BTC-USDT', froms=1, to=60, limit=100)
    data = pd.DataFrame(data)
    

    buys = data.loc[data['side']=='buy', 'time'] 
    data.loc[data['side']=='buy', 'time'] = pd.to_datetime(buys.values,  utc=True).tz_convert('Asia/Shanghai')
    buyDates = data.loc[data['side']=='buy', 'time'].tolist()


    sells = data.loc[data['side']=='sell', 'time'] 
    data.loc[data['side']=='sell', 'time'] = pd.to_datetime(sells.values,  utc=True).tz_convert('Asia/Shanghai')
    sellDates = data.loc[data['side']=='sell', 'time'].tolist()


    buyPrice = data.loc[data['side']=='buy', 'price'].tolist()  
    sellPrice = data.loc[data['side']=='sell', 'price'].tolist()



    a.clear()

    a.plot_date(buyDates, buyPrice, '#00A3E0', label='buys')
    a.plot_date(sellDates, sellPrice, '#183A54', label='sells')

    title = "OKex BTC_USDT Prices: "+str(data['price'][0])
    a.set_title(title)
    a.yaxis.set_major_locator(mticker.MaxNLocator(nbins=8, prune='lower'))
    
    a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)


class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs) # arguments and keyword arguments

        tk.Tk.iconbitmap(self, default="KawsMiffy.ico")
        tk.Tk.wm_title(self, "Sea of BTC client")



        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        menubar = tk.Menu(container)
        filemenu = tk.Menu(menubar, tearoff=0)  # tear off the menu as independent window
        filemenu.add_command(label="Save settings", command=lambda: popupmsg("Not supported just yet!"))
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)
        menubar.add_cascade(label='File', menu=filemenu)

        exchangeChoice = tk.Menu(menubar, tearoff=1)
        exchangeChoice.add_command(label="BTC-e", command=lambda: changeExchange("BTC-e", "btce"))
        exchangeChoice.add_command(label="Bitfinex", command=lambda: changeExchange("Bitfinex", "bitfinex"))
        exchangeChoice.add_command(label="Bitstamp", command=lambda: changeExchange("Bitstamp", "bitstamp"))
        exchangeChoice.add_command(label="Huobi", command=lambda: changeExchange("Huobi", "huobi"))
        
        menubar.add_cascade(label='Exchange', menu=exchangeChoice)




        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, BTCe_Page):
            
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
        label = tk.Label(self, text="""ALPHA Bitcoin trading application, 
        use at your own risk. There is no promise of warranty""", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text="Agree", command=lambda :controller.show_frame(BTCe_Page))
        button1.pack()

        button2 = ttk.Button(self, text="Disagree", command=quit)
        button2.pack()





class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text="PageOne", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
        button1.pack()

        button2 = ttk.Button(self, text="PageTwo", command=lambda :controller.show_frame(PageTwo))
        button2.pack()


# class PageTwo(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)   
#         # super().__init__(parent) can also do, this is to call the parent tk.Frame __init__ method in order to use its variable
#         label = tk.Label(self, text="PageTwo", font=LARGE_FONT)
#         label.pack(pady=10, padx=10)
        
#         button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
#         button1.pack()

#         button2 = ttk.Button(self, text="Page One", command=lambda :controller.show_frame(PageOne))
#         button2.pack()


class BTCe_Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)   
        label = tk.Label(self, text="Graph Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Back to Home", command=lambda :controller.show_frame(StartPage))
        button1.pack()

        

        canvas = FigureCanvasTkAgg(f, self)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        toolbar = NavigationToolbar2Tk(canvas, self)
        toolbar.update()
        canvas._tkcanvas.pack()

app = SeaofBTCapp()
app.geometry("1280x720")

ani = animation.FuncAnimation(f, animate, interval=5000)
app.mainloop()













# print(help(SeaofBTCapp))
# print(help(StartPage))
    






