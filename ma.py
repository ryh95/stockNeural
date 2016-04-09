# coding: utf-8
# 这个模块用于计算ma
import csv
import numpy as np

def ma(days,all_close):
    '''
    这个函数用于计算从days+1天到all_close天的前days天的均值（MA）
    比如：ma(3,all_close)
    计算从第四天到最后一天的前3天的均值（不算当日！注意‘前’）
    :param days: 计算均值的天数
    :param all_close: 总的天数对应的收盘价，每个元素需要是str
    :return: days天均值的list
    '''
    list = []
    for pos in range(days, len(all_close)):
        tmp_pct_chg = []
        for i in range(pos - days, pos):
            tmp_pct_chg.append(float(all_close[i]))
        # print tmp_pct_chg
        var =  np.mean(np.array(tmp_pct_chg))
        list.append(var)
    return list

# # 下面的是测试代码,测试正常
#
# # 读取csv文件
# csvfile = file('000905_close.csv', 'rb')
# reader = csv.reader(csvfile)
#
# all_close = []  #得到所有的收盘价和日期
# all_days = []
# for line in reader:
#     all_close.append(line[1])
#     all_days.append(line[0])
#
# # 获取第4天到最后一天的日期和对应的3日均值，合并他们，为写入csv文件做准备
# day = 3
# list_alldays = all_days[day:]
# list_ma =  ma(day,all_close)
# merge = []
# for i in range(len(list_alldays)):
#     tmp = (list_alldays[i],list_ma[i])
#     merge.append(tmp)
#
# # 写入3ma.csv文件
# with open('3ma.csv','w') as f:
#     f_csv = csv.writer(f)
#     f_csv.writerows(merge)
#
#
