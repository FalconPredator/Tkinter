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
# from matplotlib.figure import Figure
import matplotlib.animation as animation
from matplotlib import style
import matplotlib.ticker as mticker
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc

import numpy as np
import pandas as pd
import urllib
from urllib import request
import json

pd.set_option('max_columns', 50)
pd.set_option('display.width', 200)
pd.set_option('display.max_rows', 200)


LARGE_FONT = ('Verdana', 12)
NORM_FONT = ('Verdana', 10)
SMALL_FONT = ('Verdana', 8)


style.use('ggplot')

f = plt.figure()
# a = f.add_subplot(111)


exchange = "BTC-e"
DatCounter = 9000
programeName = "btce"
resampleSize = "15Min"
DataPace = "tick"    
candleWidth = 0.008
paneCount = 1

topIndicator = "none"
bottomIndicator = "none"
middleIndicator = "none"
chartLoad = True

darkColor = "#183A54"
lightColor = "#00A3E0"

EMAs = []
SMAs = []


""" default settings"""


def tutorial():
    # def leavemini(what):
    #     what.destroy()

    def page2():
        tut.destroy()
        tut2 = tk.Tk()

        def page3():
            tut2.destroy()
            tut3 = tk.Tk()

            tut3.wm_title("Part 3!")
            label = ttk.Label(tut3, text="Part 3", font=NORM_FONT)
            label.pack(side="top", fill="x", pady=10)
            B1 = ttk.Button(tut3, text="Done!", command=tut3.destroy)
            B1.pack()
            tut3.mainloop()

        tut2.wm_title("Part 2!")
        label = ttk.Label(tut2, text="Part 2", font=NORM_FONT)
        label.pack(side="top", fill="x", pady=10)
        B1 = ttk.Button(tut2, text="Next", command=page3)
        B1.pack()
        tut2.mainloop()

    tut = tk.Tk()
    tut.wm_title("Tutorial")
    label = ttk.Label(tut, text="What do you need help with?", font=NORM_FONT)
    label.pack(side="top", fill="x", pady=10)

    B1 = ttk.Button(tut, text="Overview of the application", command=page2)
    B1.pack()

    B2 = ttk.Button(tut, text="How do I trade with this client", command=lambda: popupmsg("Not yet completed"))
    B2.pack()

    B3 = ttk.Button(tut, text="Indicator Questions/Help", command=lambda: popupmsg("Not yet completed"))
    B3.pack()

    tut.mainloop()









def loadChart(run):
    global chartLoad
    if run == "start":
        chartLoad = True

    elif run == "stop":
        chartLoad = False


def addMiddleIndicator(what):
    global middleIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")

    if what != "none":
        if middleIndicator == "none": # currently not none
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want the SMA to be")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicator = []
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middleIndicator set to: ", middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

            elif what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want the EMA to be")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()

                def callback():
                    global middleIndicator
                    global DatCounter

                    middleIndicators = []
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middleIndicator set to: ", middleIndicator)
                    midIQ.destroy()

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()

        else:
            if what == "sma":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want the SMA to be")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()
                    
                def callback():
                    global middleIndicator
                    global DatCounter

                   
                    periods = (e.get())
                    group = []
                    group.append("sma")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middleIndicator set to: ", middleIndicator)
                    midIQ.destroy() 
                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()           
            
            elif what == "ema":
                midIQ = tk.Tk()
                midIQ.wm_title("Periods?")
                label = ttk.Label(midIQ, text="Choose how many periods you want the EMA to be")
                label.pack(side="top", fill="x", pady=10)
                e = ttk.Entry(midIQ)
                e.insert(0, 10)
                e.pack()
                e.focus_set()
                    
                def callback():
                    global middleIndicator
                    global DatCounter

                   
                    periods = (e.get())
                    group = []
                    group.append("ema")
                    group.append(int(periods))
                    middleIndicator.append(group)
                    DatCounter = 9000
                    print("middleIndicator set to: ", middleIndicator)
                    midIQ.destroy() 

                b = ttk.Button(midIQ, text="Submit", width=10, command=callback)
                b.pack()
                tk.mainloop()     
    else:
        middleIndicator == "none"






def addTopIndicator(what):
    global topIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")

    elif what == "none":
        topIndicator = what
        DatCounter = 9000

    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        def callback():
            global topIndicator
            global DatCounter

            periods = (e.get())  # similar to input()
            group = []
            group.append('rsi')
            group.append(periods)

            topIndicator = group
            DatCounter = 9000
            print("set top imdicator to ", group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Sumbmit", width=10, command=callback)
        b.pack()
        tk.mainloop()

    elif what == "macd":
        topIndicator = "macd"
        DatCounter = 9000



def addBottomIndicator(what):
    global bottomIndicator
    global DatCounter

    if DataPace == "tick":
        popupmsg("Indicators in Tick Data not available.")

    elif what == "none":
        bottomIndicator = what
        DatCounter = 9000

    elif what == "rsi":
        rsiQ = tk.Tk()
        rsiQ.wm_title("Periods?")
        label = ttk.Label(rsiQ, text="Choose how many periods you want each RSI calculation to consider")
        label.pack(side="top", fill="x", pady=10)

        e = ttk.Entry(rsiQ)
        e.insert(0, 14)
        e.pack()
        e.focus_set()

        def callback():
            global bottomIndicator
            global DatCounter

            periods = (e.get())  # similar to input()
            group = []
            group.append('rsi')
            group.append(periods)

            bottomIndicator = group
            DatCounter = 9000
            print("set bottom imdicator to ", group)
            rsiQ.destroy()

        b = ttk.Button(rsiQ, text="Sumbmit", width=10, command=callback)
        b.pack()
        tk.mainloop()

    elif what == "macd":
        bottomIndicator = "macd"
        DatCounter = 9000





def changeTimeFrame(tf):
    global DataPace
    global DatCounter
    if tf == "7d" and resampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smaller time frame or higher OHLC interval")
    else:
        DataPace = tf
        DatCounter = 9000

def changeSampleSize(size, width):
    global resampleSize
    global DatCounter
    global candleWidth
    if DataPace == "7d" and resampleSize == "1Min":
        popupmsg("Too much data chosen, choose a smller time frame or higher OHLC interval")
    elif DataPace == "tick":
        popupmsg("You're currently viewing tick data, not OHLC.")
    else:
        resampleSize = size
        DatCounter = 9000
        candleWidth = width

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
    global refreshRate
    global DatCounter

    if chartLoad:
        if paneCount == 1:



            if DataPace == "tick":
                try:
                    if exchange == "BTC-e":
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)

                        subjectName = 'EOS-USDT'
                        granularity = 60
                        s_Time = '2018-11-18T00:00:00.081Z'
                        e_Time = '2018-11-19T18:00:00.081Z'

                        api_key = 'd921914b-0693-4ed1-b27e-1f5679e612f5'
                        seceret_key = 'CD7F96CD31ADB4CB5B3D8200EA20745A'
                        passphrase = '111111'

                        spotAPI = spot.SpotAPI(api_key, seceret_key, passphrase, True)
                        data = spotAPI.get_deal(subjectName, froms=1, to=60, limit=100)
                        data = pd.DataFrame(data)

                        buys = data.loc[data['side']=='buy', 'time'] 
                        data.loc[data['side']=='buy', 'time'] = pd.to_datetime(buys.values,  utc=True).tz_convert('Asia/Shanghai')
                        buyDates = data.loc[data['side']=='buy', 'time'].tolist()


                        sells = data.loc[data['side']=='sell', 'time'] 
                        data.loc[data['side']=='sell', 'time'] = pd.to_datetime(sells.values,  utc=True).tz_convert('Asia/Shanghai')
                        sellDates = data.loc[data['side']=='sell', 'time'].tolist()


                        buyPrice = data.loc[data['side']=='buy', 'price'].tolist()  
                        sellPrice = data.loc[data['side']=='sell', 'price'].tolist()

                        allDates = data['time'].tolist()

                        volume = data['size']

                        a.clear()

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
                        plt.setp(a.get_xticklabels(), visible=False)


                        a.yaxis.set_major_locator(mticker.MaxNLocator(8))

                        # a.yaxis.set_major_locator(mticker.MaxNLocator(3))

                        a.plot_date(buyDates, buyPrice, lightColor, label='buys')
                        a.plot_date(sellDates, sellPrice, darkColor, label='sells')

                        a2.fill_between(allDates, 0, volume, facecolor=darkColor)
                        a2.yaxis.set_major_locator(mticker.MaxNLocator(5))
                        
                        title = "OKex "+subjectName+" Prices: "+str(data['price'][0])
                        a.set_title(title)
                        
                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)
                        

                    if exchange == "Bitstamp":
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)

                        dataLink = "https://www.bitstamp.net/api/transactions/"
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode("utf-8")
                        data = json.loads(data)

                        data = pd.DataFrame(data)

                        data['date'] = pd.to_datetime(data['date'], unit='s')
                        dateStamp = data['date'].tolist()

                        volume = data["amount"].apply(float).tolist()

                        a.clear()

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
                        plt.setp(a.get_xticklabels(), visible=False)

                        # a.yaxis.set_major_locator(mticker.MaxNLocator(8))
                       
                        a.plot_date(dateStamp, data["price"], lightColor, label='buys')


                        a2.fill_between(dateStamp, 0, volume, facecolor=darkColor)
                        a2.yaxis.set_major_locator(mticker.MaxNLocator(5))
                        
                        title = "BTCUSD BTC-USD Prices:\nLastprice: "+str(data['price'][0])
                        a.set_title(title)
                        
                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)


                    if exchange == "Bitfinex":
                        a = plt.subplot2grid((6,4), (0,0), rowspan=5, colspan=4)
                        a2 = plt.subplot2grid((6,4), (5,0), rowspan=1, colspan=4, sharex=a)
                          

                        dataLink = "https://api.bitfinex.com/v1/trades/btcusd?limit=2000"
                        data = urllib.request.urlopen(dataLink)
                        data = data.read().decode("utf-8")
                        data = json.loads(data)

                        data = pd.DataFrame(data)

                        data["timestamp"] = pd.to_datetime(data["timestamp"], unit='s')
                        dateStamp = data["timestamp"].tolist()


                        buys = data[(data["type"]=="buy")]
                        buyDates = (buys["timestamp"]).tolist()

                        sells = data[(data["type"]=="sell")]
                        sellDates = (sells["timestamp"]).tolist()



                        volume = data["amount"].apply(float).tolist()

                        a.clear()

                        a.xaxis.set_major_locator(mticker.MaxNLocator(5))
                        a.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
                        a.yaxis.set_major_locator(mticker.MaxNLocator(8)) 


                        plt.setp(a.get_xticklabels(), visible=False)

                        
                       
                        a.plot_date(buyDates, buys["price"], lightColor, label='buy')
                        a.plot_date(sellDates, sells["price"], darkColor, label='sell')


                        a2.fill_between(dateStamp, 0, volume, facecolor=darkColor)
                        a2.yaxis.set_major_locator(mticker.MaxNLocator(5))
                        
                        title = "Bitfinex BTC-USD Prices:\nLastprice: "+str(data['price'][0])
                        a.set_title(title)
                        
                        a.legend(bbox_to_anchor=(0, 1.02, 1, .102), loc=3, ncol=2, borderaxespad=0)



                except Exception as e:
                    print("Exception: "+str(e))

            else:
                if DatCounter > 12:
                    try:
                        if exchange == "Huobi":
                            if topIndicator != "none":
                                a = plt.subplot2grid((6,4), (1,0), rowspan=5, colspan=4)
                                a2 = plt.subplot2grid((6,4), (0,0), shareex=a, rowspan=5, colspan=4)
                            else:
                                a = plt.subplot2grid((6,4), (0,0), rowspan=6, colspan=4)
                        else:
                            if topIndicator != "none" and bottomIndicator !="none":
                                # main graph
                                a = plt.subplot2grid((6,4), (1,0), rowspan=3, colspan=4)
                                # volume
                                a2 = plt.subplot2grid((6,4), (4,0), sharex=a, rowspan=1, colspan=4)
                                # bottom indicator
                                a3 = plt.subplot2grid((6,4), (5,0), sharex=a, rowspan=1, colspan=4)
                                # top indicator
                                a0 = plt.subplot2grid((6,4), (0,0), sharex=a, rowspan=1, colspan=4)

                            elif topIndicator != "none":
                                # main graph
                                a = plt.subplot2grid((6,4), (1,0), rowspan=3, colspan=4)
                                # volume
                                a2 = plt.subplot2grid((6,4), (5,0), sharex=a, rowspan=1, colspan=4)
                               
                                # top indicator
                                a0 = plt.subplot2grid((6,4), (0,0), sharex=a, rowspan=1, colspan=4)

                            elif bottomIndicator !="none":
                                 # main graph
                                a = plt.subplot2grid((6,4), (0,0), rowspan=3, colspan=4)
                                # volume
                                a2 = plt.subplot2grid((6,4), (4,0), sharex=a, rowspan=1, colspan=4)
                               
                                # bottom indicator
                                a3 = plt.subplot2grid((6,4), (5,0), sharex=a, rowspan=1, colspan=4)

                            else:
                                 # main graph
                                a = plt.subplot2grid((6,4), (0,0), rowspan=3, colspan=4)
                                # volume
                                a2 = plt.subplot2grid((6,4), (5,0), sharex=a, rowspan=1, colspan=4)

                        ohlcData = spotAPI.get_kline('EOS-USDT', granularity=300)
                        for oneDict in ohlcData:
                            t = oneDict['time']
                            parsed_t = dp.parse(t)
                            time = parsed_t.strftime("%Y-%m-%d-%H-%M-%S")
                            oneDict['time'] = time
                            
                        OHLC = pd.DataFrame(ohlcData, columns=['time','open','high','low','close','volume'])
                        OHLC['time'] = pd.to_datetime(OHLC['time'])
                        
                        OHLC['MPLDate'] = mdates.date2num(OHLC['time'])
                        OHLC.set_index('time', inplace=True)

                        a.clear()

                        if middleIndicator != "none":
                            for eachMA in middleIndicator:
                                ewma = pd.stats.moments.ewma
                                if eachMA[0] == 'sma':
                                    sma = pd.rolling_mean(OHLC["close"], eachMA[1])


                        



                        


                        
                    except Exception as e:
                        print("failed in the non-tick animate: ", str(e))



class SeaofBTCapp(tk.Tk):
    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs) # arguments and keyword arguments

        
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

        dataTF = tk.Menu(menubar, tearoff=1)
        dataTF.add_command(label="Tick", command=lambda: changeTimeFrame("tick"))
        dataTF.add_command(label="1 Day", command=lambda: changeTimeFrame("1d"))
        dataTF.add_command(label="3 Day", command=lambda: changeTimeFrame("3d"))
        dataTF.add_command(label="1 Week", command=lambda: changeTimeFrame("7d"))

        menubar.add_cascade(label='Data Time Frame', menu=dataTF)

        OHLCI = tk.Menu(menubar, tearoff=1)
        OHLCI.add_command(label="Tick", command=lambda: changeTimeFrame('tick'))
        OHLCI.add_command(label="1 minute", command=lambda: changeSampleSize('1Min', 0.0005))
        OHLCI.add_command(label="5 minute", command=lambda: changeSampleSize('5Min', 0.003))
        OHLCI.add_command(label="15 minute", command=lambda: changeSampleSize('15Min', 0.008))
        OHLCI.add_command(label="30 minute", command=lambda: changeSampleSize('30Min', 0.016))
        OHLCI.add_command(label="1 Hour", command=lambda: changeSampleSize('1H', 0.032))
        OHLCI.add_command(label="3 Hour", command=lambda: changeSampleSize('3H', 0.096))
        menubar.add_cascade(label="OHLC Interval", menu=OHLCI)


        
        topIndi = tk.Menu(menubar, tearoff=1)
        topIndi.add_command(label='None', command= lambda: addTopIndicator('none'))
        topIndi.add_command(label='RSI', command= lambda: addTopIndicator('rsi'))
        topIndi.add_command(label='MACD', command= lambda: addTopIndicator('macd'))
        menubar.add_cascade(label="Top Indicator", menu=topIndi)


        
        mainI = tk.Menu(menubar, tearoff=1)
        mainI.add_command(label='None', command= lambda: addMiddleIndicator('none'))
        mainI.add_command(label='SMA', command= lambda: addMiddleIndicator('sma'))
        mainI.add_command(label='EMA', command= lambda: addMiddleIndicator('ema'))
        menubar.add_cascade(label="Main/middle Indicator", menu=mainI)


        

        bottomI = tk.Menu(menubar, tearoff=1)
        bottomI.add_command(label='None', command= lambda: addBottomIndicator('none'))
        bottomI.add_command(label='RSI', command= lambda: addBottomIndicator('rsi'))
        bottomI.add_command(label='MACD', command= lambda: addBottomIndicator('macd'))
        menubar.add_cascade(label="Bottom Indicator", menu=bottomI)

        tradeButton = tk.Menu(menubar, tearoff=1)
        tradeButton.add_command(label="Manul Trading", command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label="Automated Trading", command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_separator()
        tradeButton.add_command(label="Quick Buy", command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_command(label="Quick Sell", command=lambda: popupmsg("This is not live yet"))
        tradeButton.add_separator()
        tradeButton.add_command(label="Set-up Quick Buy/Sell", command=lambda: popupmsg("This is not live yet"))
        
        menubar.add_cascade(label="Trading", menu=tradeButton)


        startStop = tk.Menu(menubar, tearoff=1)
        startStop.add_command(label="Resume", command=lambda: loadChart("start"))
        startStop.add_command(label="Pause", command=lambda: loadChart("stop"))

        menubar.add_cascade(label="Resume/Pause client", menu=startStop)

        helpMenu = tk.Menu(menubar, tearoff=0)
        helpMenu.add_command(label="Tutorial", command=tutorial)
        menubar.add_cascade(label="Help", menu=helpMenu)





        tk.Tk.config(self, menu=menubar)

        self.frames = {}

        for F in (StartPage, BTCe_Page):
            
            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(StartPage)
            tk.Tk.iconbitmap(self, default="KawsMiffy.ico")

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
    






