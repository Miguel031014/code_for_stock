import yfinance as yf # 匯入yahoo finance套件，用來下載股價
import pandas as pd # 資料處理套件
import numpy as np # 運算的基礎套件
import matplotlib.pyplot as plt # 繪圖工具
import seaborn as sns # 高階繪圖套件

# Set the aesthetic style of the plots
sns.set_style("whitegrid")
plt.rcParams['axes.unicode_minus'] = False

ticker = input("請輸入股票代碼（以逗號分隔）: ").split(",") # 股票代碼
start_date = '2020-01-01' # 開始日期
end_date = '2025-09-20' # 結束日期

def fetch_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date, auto_adjust=False) # 下載資料
    adj_close = data["Adj Close"] # 取出調整後收盤價
    adj_close = adj_close.dropna() # 去除缺失值
    return adj_close
data = fetch_stock_data(ticker, start_date, end_date) # 呼叫函數下載資料

print(data)
# 顯示前五筆資料
print("前五筆資料")
print(data.head())  
# 顯示後五筆資料
print("後五筆資料")
print(data.tail())
# 顯示資料摘要
print("資料摘要")
print(data.info())

print("complete") # 完成下載
output_path ='stock_daily_return.csv' # 輸出檔案路徑
data.to_csv(output_path) # 儲存為CSV檔案
print(f"Data saved to {output_path}") # 確認儲存成功
