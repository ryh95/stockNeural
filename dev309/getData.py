import tushare as ts
import pandas as pd

df =  ts.get_hist_data('600848')
df.to_excel('50ETF.xlsx',sheet_name='Sheet1')
