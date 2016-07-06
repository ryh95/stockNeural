import talib
import tushare as ts
import pandas as pd
import numpy as np
code = '510050'

def getData(code):
    df =  ts.get_hist_data(code)
    df.to_excel(code+'.xlsx',sheet_name='Sheet1')

def prepareData(code):
    df =  pd.read_excel(code+'.xlsx')
    list_close = df['close'].tolist()
    float_tmp = [float(x) for x in list_close]
    float_tmp.reverse()


    ma5 = talib.MA(np.array(float_tmp),timeperiod=5)
    ma10 = talib.MA(np.array(float_tmp),timeperiod=10)
    ma20 = talib.MA(np.array(float_tmp),timeperiod=20)
    ma30 = talib.MA(np.array(float_tmp),timeperiod=30)
    ma60 = talib.MA(np.array(float_tmp),timeperiod=60)
    rsi6 = talib.RSI(np.array(float_tmp),timeperiod=6)
    rsi12 = talib.RSI(np.array(float_tmp),timeperiod=12)
    rsi24 = talib.RSI(np.array(float_tmp),timeperiod=24)
    macd,macdsignal,macdhist = talib.MACD(np.array(float_tmp))

    df2 = pd.DataFrame(index=df['date'])
    df2.loc[:,'ma5'] = ma5[::-1]
    df2.loc[:,'ma10'] = ma10[::-1]
    df2.loc[:,'ma20'] = ma20[::-1]
    df2.loc[:,'ma30'] = ma30[::-1]
    df2.loc[:,'ma60'] = ma60[::-1]
    df2.loc[:,'rsi6'] = rsi6[::-1]
    df2.loc[:,'rsi12'] = rsi12[::-1]
    df2.loc[:,'rsi24'] = rsi24[::-1]
    df2.loc[:,'macd'] = macdhist[::-1]

    for i in range(60):
        tmp = df['close'][i:].tolist()
        float_tmp = [float(x) for x in tmp]
        df2.loc[:len(df2.index)-i,'close'+str(i)] = np.array(float_tmp)

    for i in range(60):
        tmp = df['open'][i:].tolist()
        float_tmp = [float(x) for x in tmp]
        df2.loc[:len(df2.index) - i, 'open' + str(i)] = np.array(float_tmp)

    for i in range(60):
        tmp = df['high'][i:].tolist()
        float_tmp = [float(x) for x in tmp]
        df2.loc[:len(df2.index) - i, 'high' + str(i)] = np.array(float_tmp)

    for i in range(60):
        tmp = df['low'][i:].tolist()
        float_tmp = [float(x) for x in tmp]
        df2.loc[:len(df2.index) - i, 'low' + str(i)] = np.array(float_tmp)

    for i in range(60):
        tmp = df['volume'][i:].tolist()
        float_tmp = [float(x) for x in tmp]
        df2.loc[:len(df2.index) - i, 'volume' + str(i)] = np.array(float_tmp)

    df2.loc[:len(df2.index) - 1,'result'] = np.array(getResult(code))

    df2 = df2[:len(df2.index) - 59]

    df2.to_excel('input.xlsx',sheet_name='Sheet1')

def getResult(code):
    df = pd.read_excel(code + '.xlsx')
    list_close = df['close'].tolist()
    results = []
    for i,close in enumerate(list_close):
        if i == len(list_close)-1:
            break
        if list_close[i] < list_close[i+1]:
            results.append(0)
        else:
            results.append(1)
    return results


if __name__ == '__main__':
    prepareData(code)

