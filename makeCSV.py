# coding: utf-8
#从中证500指数的csv文件中读取数据制成另一张excel

import csv
import os

import ma

# def findClose(date):
#     """
#     查找一个给定的时间点在csv文件中是否存在
#
#     :param date:指定的时间点,str,如'20061215'
#     :return: bool:是否有这个时间点
#     """
#     csvfile = file('000905_close.csv', 'rb')
#     reader = csv.reader(csvfile)
#
#     for line in reader:
#         if line[0].find(date) >= 0:
#             return True
#
#     return False
#
#     csvfile.close()

# 读取csv文件
def makeCSV(filename):
    csvfile = file('originalData/'+filename+'.csv', 'rb')
    reader = csv.reader(csvfile)

    all_close = []  #得到所有的收盘价和日期
    all_days = []
    for line in reader:
        all_close.append(line[1])
        all_days.append(line[0])

    # 获取第4天到最后一天的日期和对应的3日均值，合并他们，为写入csv文件做准备
    days = [3,5,10,15,30,90,200,400]

    for day in days:
        list_alldays = all_days[day:]
        list_ma =  ma.ma(day,all_close)
        merge = []
        for i in range(len(list_alldays)):
            tmp = (list_alldays[i],list_ma[i])
            merge.append(tmp)

        # 写入*ma.csv文件
        if not os.path.exists('stockMA/'+filename):
            os.mkdir('stockMA/'+filename)
        with open('stockMA/'+filename+'/'+str(day)+'ma.csv','w') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(merge)