#-*- coding: utf-8 -*-
#从中证500指数的csv文件中读取数据制成另一张excel

import csv

def findClose(date):
    """
    查找一个给定的时间点在csv文件中是否存在

    :param date:指定的时间点,str,如'20061215'
    :return: bool:是否有这个时间点
    """
    csvfile = file('000905_close.csv', 'rb')
    reader = csv.reader(csvfile)

    for line in reader:
        if line[0].find(date) >= 0:
            return True

    return False

    csvfile.close()

csvfile = file('000905_close.csv', 'rb')
reader = csv.reader(csvfile)
print reader
# def ma(day):
