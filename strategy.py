import csv

import math
import pandas as pd

csvfile = file('csvStrategy.csv', 'rb')
reader = csv.reader(csvfile)

data = pd.read_csv('000905_close.csv')
data = data.as_matrix()

p = 0.8
test = data[int(len(data)*p)+80:,:]


for l in reader:
    list = l

sum = 0
for i in range(len(list)):
    Rt = math.log(1/float(list[i])-1)/(-100)
    Pt = test[:,1][i]
    Pt_next = Rt*Pt+Pt
    # print Rt,Pt
    if Pt_next>Pt+0.025:
        sum = Pt_next-Pt+sum
    elif Pt_next<Pt-0.025:
        sum = Pt-Pt_next+sum
print sum
csvfile.close()