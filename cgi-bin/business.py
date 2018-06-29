#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
# import numpy as np
import matplotlib.pyplot as plt 
import io
import numpy as np
import time
import cx_Oracle
import os
import traceback

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
## 业务统计：按业务分类(储蓄、贷款)和时间(月、季、年)统计各个支行的业务总金额数和用户数
## 选做：对统计结果以饼图或曲线图显示


## use pyplot to draw pictures

current_date = time.localtime()
db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
cr = db.cursor()
sql = "select sum(余额) from 储蓄账户"
cr.execute(sql)
rs = cr.fetchall()
saving_total = rs[0][0]

sql = "select sum(所贷金额) from 贷款"
cr.execute(sql)
rs = cr.fetchall()
loan_total = rs[0][0]
sql = "select count(身份证号_客户) from 借贷"
cr.execute(sql)
rs = cr.fetchall()
loan_users = rs[0][0]
sql = "select count(身份证号_客户) from 开户_储蓄"
cr.execute(sql)
rs = cr.fetchall()
saving_users = rs[0][0]
cr.close()
db.close()

plt.figure(figsize=(6,6)) #调节图形大小
labels = ['loan','saving'] #定义标签
sizes = [loan_total,saving_total] #每块值
colors = ['aquamarine','lightskyblue'] #每块颜色定义
explode = (0,0) #将某一块分割出来，值越大分割出的间隙越大
patches,text1,text2 = plt.pie(sizes,
                      explode=explode,
                      labels=labels,
                      colors=colors,
                      autopct = '%3.2f%%', #数值保留固定小数位
                      shadow = False, #无阴影设置
                      startangle =90, #逆时针起始角度设置
                      pctdistance = 0.6) #数值距圆心半径倍数距离
plt.axis('equal')
plt.savefig("../htdocs/images/test3.png")

plt.figure(figsize=(6,6)) #调节图形大小
labels = ['loan','saving'] #定义标签
sizes = [loan_users,saving_users] #每块值
width = 0.5
colors = ['aquamarine','lightskyblue'] #每块颜色定义
plt.bar(range(2),sizes,width=width,tick_label=labels)
plt.savefig("../htdocs/images/test4.png")




# current_date + ":"+str(saving_total)+","+str(loan_total)+","+str(saving_users)+","+str(loan_users)+"\n"
s_amount = {}
s_users = {}
l_amount = {}
l_users = {}
with open("log.txt","r+") as f:
    for line in f.readlines():
        temp = line.split(' ')
        if(len(temp)!=5):
            continue
        date = temp[0]
        temp2 = date.split("-")
        year = temp2[0]
        month = str(int(temp2[1]))
        day = str(int(temp2[2]))
        if(s_amount.get(year)==None):
            s_amount[year] = {}
            s_users[year] = {}
            l_amount[year] = {}
            l_users[year] = {}
        if(s_amount[year].get(month)==None):
            s_amount[year][month] = {}
            s_users[year][month] = {}
            l_amount[year][month] = {}
            l_users[year][month] = {}
        s_amount[year][month][day] = float(temp[1])
        s_users[year][month][day] = int(temp[3])
        l_amount[year][month][day] = float(temp[2])
        l_users[year][month][day] = int(temp[4])

current_year = time.strftime("%Y", time.localtime())
current_month = time.strftime("%m", time.localtime()) 
current_day = time.strftime("%d", time.localtime())

years = sorted(s_amount.keys())

def getcount_sum(dic):
    count = 0
    sum = 0
    for item in dic.values():
        if isinstance(item,dict):
            c,s = getcount_sum(item)
            count = count + c
            sum = sum + s
        elif(isinstance(item,int) or isinstance(item,float)):
            count = count+1
            sum = sum + item
    return count,sum
def sum(dict):
    count,sum = getcount_sum(dict)
    return sum

year_sum1 = [0 for i in range(len(years))]
year_sum2 = [0 for i in range(len(years))]
for i in range(len(years)):
    year_sum1[i] = sum(s_amount[years[i]])
    year_sum2[i] = sum(l_amount[years[i]])

plt.figure(figsize=(6,6)) #调节图形大小
x = [i for i in range(len(years))]
width = 0.4
plt.bar(x,year_sum1,width=width,label="saving")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x,year_sum2,width=width,label="loan",tick_label=years)
plt.savefig("../htdocs/images/test5.png")


for i in range(len(years)):
    year_sum1[i] = sum(s_users[years[i]])
    year_sum2[i] = sum(l_users[years[i]])

plt.figure(figsize=(6,6)) #调节图形大小
x = [i for i in range(len(years))]
width = 0.4
plt.bar(x,year_sum1,width=width,label="saving")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x,year_sum2,width=width,label="loan",tick_label=years)
plt.savefig("../htdocs/images/test6.png")


month_sum1 = [0 for i in range(12)]
month_sum2 = [0 for i in range(12)]
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
for i in range(12):
    if(s_amount[current_year].get(str(i+1))):
        month_sum1[i] = sum(s_amount[current_year][str(i+1)])
        month_sum2[i] = sum(l_amount[current_year][str(i+1)])

plt.figure(figsize=(10,6)) #调节图形大小
x = [i for i in range(12)]
width = 0.4
plt.bar(x,month_sum1,width=width,label="saving")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x,month_sum2,width=width,label="loan",tick_label=months)
plt.savefig("../htdocs/images/test7.png")


for i in range(12):
    if(s_amount[current_year].get(str(i+1))):
        month_sum1[i] = sum(s_users[current_year][str(i+1)])
        month_sum2[i] = sum(l_users[current_year][str(i+1)])

plt.figure(figsize=(10,6)) #调节图形大小
x = [i for i in range(12)]
width = 0.4
plt.bar(x,month_sum1,width=width,label="saving")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x,month_sum2,width=width,label="loan",tick_label=months)
plt.savefig("../htdocs/images/test8.png")


season1 = [0 for i in range(4)]
season2 = [0 for i in range(4)]
seasons = ['Season1','Season2','Season3','Season4']
for i in range(4):
    season1[i] = month_sum1[3*i]+month_sum1[3*i+1]+month_sum1[3*i+2]
    season2[i] = month_sum2[3*i]+month_sum2[3*i+1]+month_sum2[3*i+2]


plt.figure(figsize=(6,6)) #调节图形大小
x = [i for i in range(4)]
width = 0.4
plt.bar(x,season1,width=width,label="saving")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x,season2,width=width,label="loan",tick_label=seasons)
plt.savefig("../htdocs/images/test9.png")


for i in range(4):
    season1[i] = month_sum1[3*i]+month_sum1[3*i+1]+month_sum1[3*i+2]
    season2[i] = month_sum2[3*i]+month_sum2[3*i+1]+month_sum2[3*i+2]

plt.figure(figsize=(6,6)) #调节图形大小
x = [i for i in range(4)]
width = 0.4
plt.bar(x,season1,width=width,label="saving")
for i in range(len(x)):
    x[i] = x[i] + width
plt.bar(x,season2,width=width,label="loan",tick_label=seasons)
plt.savefig("../htdocs/images/test10.png")




print('Content-type: text/html')
print('')

args = cgi.FieldStorage()
print('<div align="left"><form action="/cgi-bin/index.py" method="GET">')
print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #faddde;border: solid 1px #980c10;background: #d81b21; " >')
print('返回主页</button></form></div>')
print('<body style="background-color: #fdf7f7;" align="center">')
print('<h1 align="center">业务统计</h1><br><hr/><br>')
print('<h2>当前贷款和储蓄在业务总金额中所占比例</h2>')
print('<img src="/images/test3.png" />')
print('<h2>当前贷款和储蓄的总用户数</h2>')
print('<img src="/images/test4.png" />')
print('<h2>每年的贷款/储蓄业务总金额</h2>')
print('<img src="/images/test5.png" />')
print('<h2>每年的贷款/储蓄业务总用户数变化</h2>')
print('<img src="/images/test6.png" />')
print('<h2>今年各月的贷款/储蓄业务总金额</h2>')
print('<img src="/images/test7.png" />')
print('<h2>今年各月的贷款/储蓄业务总用户数</h2>')
print('<img src="/images/test8.png" />')
print('<h2>今年各季度的贷款/储蓄业务总金额</h2>')
print('<img src="/images/test9.png" />')
print('<h2>今年各季度的贷款/储蓄业务总用户数</h2>')
print('<img src="/images/test10.png" />')
print('<p>注：橙色为贷款，蓝色为储蓄</p>')
print('<p>'+str(s_amount)+'</p>')
print('<p>'+current_month+'</p>')

print('</body>')


