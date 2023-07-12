import ccxt
import pandas as pd

# 获取当前价格
def get_btc_price(symbol):
    exchange = ccxt.binance()  # 连接到Binance交易所
    # symbol = 'BTC/USDT'  比特币对USDT的交易对

    ticker = exchange.fetch_ticker(symbol)
    btc_price = ticker['last']  # 获取最新的比特币价格

    print("BTC Price:", btc_price)

# 获取历史价格
def save_historical_data_to_csv(filename, symbol, timeframe, limit):
    exchange = ccxt.binance()  # 连接到Binance交易所

    # 获取历史K线数据
    candles = exchange.fetch_ohlcv(symbol, timeframe=timeframe, limit=limit)

    # 创建数据帧
    df = pd.DataFrame(candles, columns=['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume'])

    filename_save ="trade_data/" + filename + ".csv"

    # 将数据帧保存为Excel文件
    df.to_csv(filename_save, index=False)

    print("Historical data saved to", filename_save)
