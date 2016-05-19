import csv

csvfile = file('../data/originalData'+'/50ETF'+'.csv', 'r')
reader = csv.reader(csvfile)

list =[]
for line in reader:
    list.append(line)
print list


for item in list[400:]:
    print item
