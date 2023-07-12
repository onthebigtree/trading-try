# 一个完整的套利程序会涉及非常多的细节，包括帐户管理、错误处理、网络延迟等
# 此处程序仅为演示套利的核心原理

import ccxt
import time

# 实例化交易所
bn = ccxt.binance()
okx = ccxt.okex()

# BTC价格套利阈值
THRESHOLD = 1

# 交易函数 - 根据不同交易所的 api 填写不同的交易函数，此处仅举例
def buy_on_bn():
    print("在Binance购买",bn_price)

def sell_on_bn():
    print("在Binance出售",bn_price)

def buy_on_okx():
    print("在OKX购买",okx_price)

def sell_on_okx():
    print("在OKX出售",okx_price)

# 交易程序
while True:

    # 获取价格
    try:
        bn_ticker = bn.fetch_ticker('BTC/USDT')
        okx_ticker = okx.fetch_ticker('BTC/USDT')

        bn_price = bn_ticker['last']
        okx_price = okx_ticker['last']

        # 判断是否有利可图
        if bn_price > okx_price + THRESHOLD:
            buy_on_okx()
            sell_on_bn()
        elif okx_price > bn_price + THRESHOLD:
            buy_on_bn()
            sell_on_okx()

    # 错误处理
    except ccxt.NetworkError as e:
        print(bn.id, '获取行情失败，由于网络错误:', str(e))
    except ccxt.ExchangeError as e:
        print(bn.id, '获取行情失败，由于交易所错误:', str(e))
    except Exception as e:
        print(bn.id, '获取行情失败，错误是:', str(e))

    time.sleep(1)  # 确保不要频繁地请求API
