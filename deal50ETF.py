import csv

csvfile = file('originalData/50ETF.csv', 'rb')
reader = csv.reader(csvfile)

merge = []

for line in reader:
    time =  line[0]
    price = line[1]
    time = time[:10]
    tmp = (time,float(price)*1000)
    merge.append(tmp)


with open('originalData/50ETF1000.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(merge)