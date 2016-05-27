# coding: utf-8
#从中证500指数的csv文件中读取数据制成另一张excel

import csv
import numpy as np
import os

import talib


# 读取csv文件
def getIndicators(filename,*indicator):
    originalDataPath = 'data/originalData/'
    indicatorPath = 'data/indicator/'

    csvfile = file(originalDataPath + filename +'.csv', 'rb')
    reader = csv.reader(csvfile)

    all_close = []  # 得到所有的收盘价和日期
    all_days = []
    for line in reader:
        all_close.append(line[1])
        all_days.append(line[0])

    float_data = [float(x) for x in all_close]

    # 获取第4天到最后一天的日期和对应的3日均值，合并他们，为写入csv文件做准备
    days = [3, 5, 10, 15, 30, 90, 200, 400]

    for day in days:
        list_alldays = all_days

        for item in indicator:
            if item == 'MA':
                list_ma = talib.MA(np.array(float_data), timeperiod=day)
                mergeMA = []
                for i in range(len(list_alldays)):
                    tmp = (list_alldays[i], list_ma[i])
                    mergeMA.append(tmp)
            if item == 'RSI':
                list_rsi = talib.RSI(np.array(float_data), timeperiod=day)
                mergeRSI = []
                for i in range(len(list_alldays)):
                    tmp = (list_alldays[i], list_rsi[i])
                    mergeRSI.append(tmp)



        # 写入*ma.csv文件
        if not os.path.exists(indicatorPath+filename+'/MA'):
            os.mkdir(indicatorPath+filename+'/MA')
        with open(indicatorPath+filename+'/MA/'+str(day)+'ma.csv','w') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(mergeMA)

        # 写入*rsi.csv文件
        if not os.path.exists(indicatorPath+filename+'/RSI'):
            os.mkdir(indicatorPath+filename+'/RSI')
        with open(indicatorPath+filename+'/RSI/'+ str(day) + 'rsi.csv', 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(mergeRSI)

