import csv

import math
import pandas as pd

def strategy(filename):
    csvfile = file('modelPredict/'+filename+'/'+'resultPredict.csv', 'rb')
    reader = csv.reader(csvfile)

    data = pd.read_csv('originalData/'+filename+'.csv')
    data = data.as_matrix()

    p = 0.8
    test = data[int(len(data)*p)+80:,:]


    for l in reader:
        list = l

    sum = 0
    for i in range(len(list)):
        Rt = math.log(1/float(list[i])-1)/(-100)
        Pt = test[:,1][i]
        if i == len(list)-1:
            break
        Pt_next = test[:, 1][i + 1]
        Pt_predict = Rt*Pt+Pt
        # print Rt,Pt
        if Pt_predict > Pt + 2.5:
            sum = Pt_next - Pt + sum
            print i, Pt_next - Pt
        elif Pt_predict < Pt - 2.5:
            sum = Pt - Pt_next + sum
            print i, Pt - Pt_next
    print sum
    csvfile.close()