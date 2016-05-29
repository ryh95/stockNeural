import csv
import numpy as np

indicatorPath = '../data/indicator/'
csvfile = file(indicatorPath + '50ETF/' +'MACD/'+'5-55-10','rb')
reader = csv.reader(csvfile)

list_hist = []
for list in reader:
    list_hist = list

# print list_hist
i = 0
for item in list_hist:
    if i == 64:
        print item
    i+=1

print i
print len(list_hist)