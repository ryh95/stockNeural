import csv

import math
import pandas as pd
import matplotlib.pyplot as plt

def strategy(filename):
    csvfile = file('data/modelPredict/'+filename+'/real/'+'resultPredictRSI.csv', 'rb')
    reader = csv.reader(csvfile)

    data = pd.read_csv('data/originalData/'+filename+'.csv')
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
        p = math.log(1/float(list[i])-1)/(-100)
        Pt = test[:,1][i]
        if i == len(list)-1:
            break
        Pt_next = test[:, 1][i + 1]
        Pt_predict = p*Pt+Pt
        # print Rt,Pt
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
    plt.plot(x,y)
    plt.show()
    csvfile.close()