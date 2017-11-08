import requests
from bs4 import BeautifulSoup
import json
import csv
import operator

res = requests.get('http://www.lotto-8.com/listltobig.asp')
max_time = 60
while(max_time > 30):
    try:
        max_time = int(input("input(2-30):"))        
    except:
        print (u'請輸入正確數字!')
    
bs = BeautifulSoup(res.text,'lxml')
table = bs.select('.auto-style4')[0]
trs = table.select('tr')
total = {}
#for i in range(1,len(trs)):
for i in range(1,max_time):
    tds = trs[i].select('td')
    for t in range(1,len(tds)):
        for s in tds[t].text.split(","):
            try:
                s = s.strip()	    
                s = str(int(s))
                if s in total.keys():
                    #print (s,total[s])         
                    total[s] += 1
                else:
                    total[s] = 1               
            except:
                print('not int!!')
jsonarray = json.dumps(total)
#del total['']
f = open('mycsvfile1.csv','w')
head = u'數字,次數\n'  
f.write(head)
for i in range(1,50):
    if str(i) in total.keys():
        data = str(i)+','+str(total[str(i)])
    else:
        data = str(i)+',0'
    data += "\n"
    f.write(data)        
f.close()

sorted_h = sorted(total.items(), key=operator.itemgetter(1), reverse=True)
sorted_l = sorted(total.items(), key=operator.itemgetter(1))
index = 0
for (k,v) in sorted_h:
    if index < 6:
        print (k,v)          
    else:
        break
    index += 1