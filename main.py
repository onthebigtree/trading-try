from utils import get_btc_price, save_historical_data_to_csv

user_input = str(input("选择你需要的数据进行爬取,用逗号分隔："))
user_input_parts = user_input.split(",")

filename = user_input_parts[0]  # Change to 0 if it's the first part
token_name = user_input_parts[1] + '/USDT'  # Change to 1 if it's the second part
time_span = user_input_parts[2]  # Change to 2 if it's the third part

# 调用函数将历史数据保存到csv文件
save_historical_data_to_csv(filename,token_name,time_span,365)

get_btc_price('BTC/USDT')