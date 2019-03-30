from xlwt import *

filename = Workbook(encoding='utf-8')
table = filename.add_sheet('data')

data = {'1':['values_one', 'values_two', 'values_three'],
        '2':[15,16,17],
        '3':[19,20,21],
        '4':[22,23,24]
        }

ldata = list()
num = sorted([a for a in data])

for x in num:
    t = [int(x)]
    for a in data[x]:
        t.append(a)
    ldata.append(t)

for i, p in enumerate(ldata):
    for j, q in enumerate(p):
        table.write(i, j, q)

filename.save('data.xlsx')
