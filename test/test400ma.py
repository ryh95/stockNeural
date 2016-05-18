import csv

csvfile = file('originalData/'+'000905_close'+'.csv', 'rb')
reader = csv.reader(csvfile)

i=0
list =[]
for line in reader:
    list.append(line)
    i+=1
    if i == 400:
        break
print list

sum=0
for item in list:
    price = item[1]
    sum+=float(price)

print sum/400