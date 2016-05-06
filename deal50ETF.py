import csv

csvfile = file('50ETF.csv', 'rb')
reader = csv.reader(csvfile)

merge = []

for line in reader:
    time =  line[0]
    price = line[1]
    time = time[:10]
    tmp = (time,price)
    merge.append(tmp)


with open('50ETF.csv','w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(merge)