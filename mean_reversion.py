import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import ccxt

def calculate_z_score(series):
    return (series - series.mean()) / np.std(series)

# 创建交易所，这里以 binance 为例
exchange = ccxt.binance()

# 获取历史数据
data = exchange.fetch_ohlcv('BTC/USDT', '1d', since=exchange.parse8601('2022-06-01T00:00:00Z'), limit=1000)
data = pd.DataFrame(data, columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])
data['Timestamp'] = pd.to_datetime(data['Timestamp'], unit='ms')
data.set_index('Timestamp', inplace=True)

# 使用过去30天的收盘价计算滑动平均值和滑动标准差
data['mean'] = data['Close'].rolling(window=12).mean()
data['std'] = data['Close'].rolling(window=12).std()

# 计算Z分数
data['z_score'] = (data['Close'] - data['mean']) / data['std']

# 创建一个空的"Positions"列
data['Positions'] = None

# 当Z分数低于-1时，我们将买入股票（假设价格会回归均值）
data.loc[data['z_score'] < -1, 'Positions'] = data['z_score']**1/3 - 1

# 当Z分数高于1时，我们将卖出股票（假设价格会回归均值）
data.loc[data['z_score'] > 1, 'Positions'] = data['z_score']**1/3 + 1

data['z_score'].plot()
plt.show()

# 填充其他位置
data['Positions'].fillna(method='ffill', inplace=True)

# 计算策略的日收益
data['Strategy Daily Returns'] = data['Close'].pct_change() * data['Positions'].shift()

# 计算策略的累计收益
data['Strategy Cumulative Returns'] = (1 + data['Strategy Daily Returns']).cumprod()

# 绘制策略的累计收益
data['Strategy Cumulative Returns'].plot()
plt.show()
