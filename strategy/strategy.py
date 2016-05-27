import csv

import math
import pandas as pd
import matplotlib.pyplot as plt

def getProfit(filename,type,indicator):
    neuralOutputPath = 'data/neuralOutput/' + filename + '/' + type + '/'
    originalDataPath = 'data/originalData/'

    csvfile = file(neuralOutputPath + 'resultPredict' + indicator +'.csv', 'rb')
    reader = csv.reader(csvfile)

    data = pd.read_csv(originalDataPath+filename+'.csv')
    data = data.as_matrix()
    data = data[400:,:]

    t = 0.8
    test = data[int(len(data) * t):, :]

    list = []
    for l in reader:
        list = l

    sum = 0
    x = []
    y = []
    for i in range(len(list)):

        Pt = test[:,1][i]
        if i == len(list)-1:
            break
        Pt_next = test[:, 1][i + 1]

        if type == 'binary':
            if list[i]=='1':
                sum = Pt_next - Pt + sum
                print i, Pt_next - Pt
            elif list[i]=='0':
                sum = Pt - Pt_next + sum
                print i, Pt - Pt_next
            x.append(i)
            y.append(sum)
        elif type == 'real':
            p = math.log(1 / float(list[i]) - 1) / (-100)
            Pt_predict = p * Pt + Pt
            # 2.21 000905_close
            if Pt_predict > Pt + 0.00121:
                sum = Pt_next - Pt + sum
                print i, Pt_next - Pt
                x.append(i)
                y.append(sum)
            elif Pt_predict < Pt - 0.00121:
                sum = Pt - Pt_next + sum
                print i, Pt - Pt_next
                x.append(i)
                y.append(sum)

    print sum
    list_sum = []
    list_sum.append(sum)
    with open('sum.csv', 'a+') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(list_sum)

    # plt.plot(x,y)
    # plt.show()
    csvfile.close()