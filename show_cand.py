import pandas as pd
import matplotlib.pyplot as plt
import mplfinance as mpf
import os

# 指定CSV文件所在的目录
csv_directory = "trade_data/"

# 获取指定目录中所有的CSV文件
csv_files = [f for f in os.listdir(csv_directory) if f.endswith('.csv')]

# 显示CSV文件列表
for i, file in enumerate(csv_files):
    print(f"{i}: {file}")

# 根据索引选择特定的CSV文件
selected_file_index = 0  # 更换为你想要的索引
selected_file = csv_files[selected_file_index]

# 将选定的CSV文件读入Pandas DataFrame
data = pd.read_csv(os.path.join(csv_directory, selected_file))

# 确保'Timestamp'列为datetime数据类型
data['Timestamp'] = pd.to_datetime(data['Timestamp'])

# 将'Timestamp'列设置为DataFrame的索引
data.set_index('Timestamp', inplace=True)

# 使用mplfinance绘制蜡烛图
mpf.plot(data, type='candle', style='charles', volume=True)
plt.show()
