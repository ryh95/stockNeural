import csv

csvfile = file('data/originalData/' + '50ETF' + '.csv', 'rb')
reader = csv.reader(csvfile)


data = []
for line in reader:
    date = line[0]
    list = date.split('-')
    time =''
    for item in list:
        time += item
    tmp = (time,line[1])
    data.append(tmp)

with open('data/originalData/' + '50ETF' + '.csv', 'w') as f:
    f_csv = csv.writer(f)
    f_csv.writerows(data)