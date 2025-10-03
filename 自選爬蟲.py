import yfinance as yf # 匯入yahoo finance套件，用來下載股價
import pandas as pd # 資料處理套件

ticker = input("請輸入股票代碼（以逗號分隔）: ").split(",") # 股票代碼
start_date=input('請輸入開始日期(格式:YYYY-MM-DD)')
end_date=input('請輸入結束日期(格式:YYYY-MM-DD)')

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
