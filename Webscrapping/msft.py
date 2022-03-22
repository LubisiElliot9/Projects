import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
from bs4 import BeautifulSoup 
import urllib.request as ur
import yfinance as yf 
import cufflinks as cf
import plotly.graph_objects as go
from plotly.offline import iplot, init_notebook_mode
cf.go_offline()
init_notebook_mode()

msft = yf.Ticker("MSFT")
history = pd.read_csv("Microsoft_data/Microsoft_Stock_data.csv")
today_1 = msft.history(period="1d")
data = history.append(today_1)
data.to_csv("Data/Microsoft_Stock_data.csv")
print("Data is ready!!")

msft2 = yf.Ticker("MSFT")
history = msft2.history(period="1y")

history['Close'].plot(figsize=(16,9))
plt.xlabel("Date")
plt.ylabel("StockPrice")
plt.title("Line Chart for MSFT stock Price")
plt.savefig("Charts/Linechart.png")


qf = cf.QuantFig(history, title="Microsoft Stock Prices From 2020 March", name='MSFT')
qf.add_sma(periods=10, column='Close', color='blue')
qf.add_sma(periods=20, column='Close', color='red')
qf.iplot()
plt.savefig("Charts/CandleChart.png")




