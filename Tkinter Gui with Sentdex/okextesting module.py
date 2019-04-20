import okex.account_api as account
import okex.ett_api as ett
import okex.futures_api as future
import okex.lever_api as lever
import okex.spot_api as spot
import pandas as pd
import numpy as np
import time
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from mpl_finance import candlestick_ohlc
from matplotlib import dates
from matplotlib import style
import matplotlib.animation as animation
from matplotlib.figure import Figure
import csv
import json
pd.set_option('max_columns', 50)
pd.set_option('display.width', 200)
pd.set_option('display.max_rows', 200)



subjectName = 'BTC-USD-181228'
granularity = 60
s_Time = '2018-11-18T00:00:00.081Z'
e_Time = '2018-11-19T18:00:00.081Z'

api_key = 'd921914b-0693-4ed1-b27e-1f5679e612f5'
seceret_key = 'CD7F96CD31ADB4CB5B3D8200EA20745A'
passphrase = '111111'

spotAPI = spot.SpotAPI(api_key, seceret_key, passphrase, True)
# result = spotAPI.get_ticker()#s_Time, e_Time)
# result = spotAPI.get_specific_ticker('BTC-USDT')
# 不提供历史ticker数据历史数据的话只能用k线接口拿到最近2000条数据
# result = spotAPI.get_deal('BTC-USDT', froms=1, to=100, limit=100)
# result = spotAPI.get_depth('BTC-USDT', 200)





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




f = Figure(figsize=(10,6), dpi=100)
a = f.add_subplot(111)

a.plot_date(buyDates, buyPrice)
a.plot_date(sellDates, sellPrice)

print(data.price[59], data.time[59])
print(data.price[0], data.time[0])
print(data.price[10], data.time[10])












