import matplotlib.pyplot as plt
import pandas as pd
import  datetime
import  pandas_datareader.data  as web
# https://pythonprogramming.net/stock-data-manipulation-python-programming-for-finance/?completed=/handling-stock-data-graphing-python-programming-for-finance/
# https://ntguardian.wordpress.com/2018/07/17/stock-data-analysis-python-v2/



start=datetime.datetime(2015,1,1)
# end=datetime.datetime(2017,1,1)

end = datetime.datetime.now()
Symbol = "POWERGRID.NS"
df = web.DataReader(Symbol, 'yahoo', start, end)
df.dropna(inplace=True)

df.reset_index(inplace=True)
df.set_index("Date", inplace=True)
# df = df.drop('Volume',axis='columns')
print(df.head(7).to_string())

# print(df['High'])

LastPrice=web.get_data_yahoo(Symbol)
# print(LastPrice.tail(2))
LastPrice = LastPrice.at[LastPrice.index[-1],'Adj Close']
print( round(LastPrice,2))

# df.plot(grid=True)
# df['Adj Close'].plot(grid=True)
df['100ma'] = df['Adj Close'].rolling(window=100,min_periods=0).mean()
print(df.head())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=1, colspan=1,sharex=ax1)
ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()