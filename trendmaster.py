import ccxt
import pandas as pd

# 建立交易所连接
exchange = ccxt.binance()

# 获取历史K线数据
bars = exchange.fetch_ohlcv('BTC/USDT', timeframe='1d', limit=100)
df = pd.DataFrame(bars, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

# 转换时间戳
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

# 计算移动平均线
df['MA20'] = df['close'].rolling(window=20).mean()
df['MA50'] = df['close'].rolling(window=50).mean()

# 打印DataFrame
print(df)

# 交易逻辑
# 当MA20从下方穿过MA50时，这通常被视为一个上升趋势的开始，也就是买入信号。在这个时间点，策略会做多（即买入）,反之则做空
for i in range(1, len(df)):
    if df['MA20'][i] > df['MA50'][i] and df['MA20'][i-1] < df['MA50'][i-1]:
        print("Buy at $", df['close'][i])
    if df['MA20'][i] < df['MA50'][i] and df['MA20'][i-1] > df['MA50'][i-1]:
        print("Sell at $", df['close'][i])
