import json
from pprint import pprint
import pandas as pd
import matplotlib.pyplot as plt
class information:
    def __init__(self,arr,sareaen):
        self.arr = arr
        self.sareaen = sareaen
        count = 0
        left = []
        right = []
        for i in arr:
            if i[0] == sareaen:
                count += 1
                left.append(i[1])
                right.append(i[2])
                if count == 5:
                    break
        left.reverse()
        right.reverse()
        plt.title(sareaen + "Top 5", fontsize="20") 
        plt.barh(range(len(left)), right, tick_label=left)
with open('/Users/eric/Desktop/data/ibike.json') as file:
    data = file.read()
jdata = json.loads(data)
d = jdata['retVal'].values()
area = []
for i in d:
    per = int(i['sbi']) / int(i['tot'])
    i['per'] = per
for st in d:
    if st['act'] == '1':
        sareaen,snaen,sbi,per = st['sareaen'],st['snaen'],st['sbi'],st['per']
        item = (sareaen,snaen,sbi,per)
        area.append(list(item))
area = sorted(area,key = lambda x:x[3],reverse = True)
str = input('要查詢哪區可租借數量最多的前5個iBike租借站點')
test = information(area,str)