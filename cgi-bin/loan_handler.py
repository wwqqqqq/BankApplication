#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os
import traceback
import time

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

## 贷款管理：提供贷款信息的增删查功能，提供贷款发放功能；贷款信息一旦添加成功后不允许修改；
## 要求能查询每笔贷款的当前状态(未开始发放、发放中、已全部发放)；
## 处于发放中状态的贷款记录不允许删除

## 贷款: 贷款号、支行名、所贷金额
## 借贷: 贷款号、身份证号_客户
## 贷款支付: 贷款号、日期、金额


print('Content-type: text/html')
print('')


'''
add:
loanid, text, 贷款号
branch, text, 支行名
amount, text, 所贷金额
lenders, text, 贷款人身份证号
pay:
loadid, text, 贷款号
time, date, 日期
amount, text, 金额
'''
change_amount = 0
change_users = 0

def printinfo_add(loanid,branch,amount,lenders):
    print('<body align="center"><br><h1>已成功添加贷款信息</h1>')
    print('<p>贷款号: %s </p>' % loanid)
    print('<p>支行名: %s </p>' % branch)
    print('<p>所贷金额: %s </p>' % amount)
    print('<p>贷款人身份证号:')
    lender_list = lenders.split(';')
    for lender in lender_list:
        print('<br> %s' % lender)
    print('</p>')
    print('</body>')

def printinfo_pay(loanid,time,amount):
    print('<body align="center"><br><h1>已成功添加贷款支付信息</h1>')
    print('<p>贷款号: %s </p>' % loanid)
    print('<p>日期: %s </p>' % time)
    print('<p>支付金额: %s </p>' % amount)
    print('</body>')
def printinfo_delete(loanid):
    print('<body align="center"><br><h1>已成功删除贷款')
    print(loanid)
    print('</h1></body>')
def ret_btn():
    print('<form action="/cgi-bin/loan.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #fef4e9;border: solid 1px #da7c0c;background: #f78d1d; " >')
    print('返回贷款管理</button></form>')

## 贷款: 贷款号、支行名、所贷金额
## 借贷: 贷款号、身份证号_客户
args = cgi.FieldStorage()
if(args.getvalue('add')):
    # >>> db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    loanid = args.getvalue('loanid')
    branch = args.getvalue('branch')
    amount = args.getvalue('amount')
    lenders = args.getvalue('lenders')
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql1 = 'insert into 贷款 (贷款号, 支行名, 所贷金额) values('
        sql1 = sql1 + '\'' + loanid + '\', \'' + branch + '\', ' + amount + ')' 
        print(sql1)
        cr.execute(sql1)
        change_amount = change_amount + int(amount)
        sql2 = 'insert into 借贷 (贷款号, 身份证号_客户) values(' + '\'' + loanid + '\', \''
        lender_list = lenders.split(';')
        for lender in lender_list:
            temp = sql2 + lender + '\')'
            print(temp)
            cr.execute(temp)
            change_users = change_users + 1
        cr.close()
        db.commit()
        db.close()
        printinfo_add(loanid,branch,amount,lenders)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<br><br>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!')
elif(args.getvalue('pay')):
    ## 贷款支付: 贷款号、日期、金额
    loanid = args.getvalue('loanid')
    time = args.getvalue('time')
    amount = args.getvalue('amount')
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql = 'insert into 贷款支付 (贷款号, 日期, 金额) values('
        sql= sql + '\'' + loanid + '\', to_date(\''+time+'\',\'yyyy-mm-dd\'), ' + amount + ')' 
        print(sql)
        cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_pay(loanid,time,amount)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<br><br>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!')
elif(args.getvalue('delete')):
    loanid = args.getvalue('d_loanid')
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql = "Delete From 贷款支付 where 贷款号='"+loanid+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        #change_amount = 0  
        sql = "select count(身份证号_客户) from 借贷 where 贷款号='"+loanid+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        rs = cr.fetchall()
        change_users = change_users - rs[0][0]
        sql = "Delete From 借贷 where 贷款号='"+loanid+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "select 所贷金额 from 贷款 where 贷款号='"+loanid+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        rs = cr.fetchall()
        change_amount = change_amount - rs[0][0]
        sql = "Delete From 贷款 where 贷款号='"+loanid+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_delete(loanid)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<p>')
        traceback.print_exc()
        print('<br>错误！无法删除！</p>')

'''
current_date = time.strftime("%Y-%m-%d", time.localtime())
data = ""
with open("log.txt","r+") as f:
    f.seek(0,0)

    find = False
    for line in f.readlines():
        if(line.startswith(current_date)):
            temp = line.split(" ")
            line = temp[0] + " "+temp[1]+" "+str(int(temp[2])+change_amount)+" "+temp[3]+" "+str(int(temp[4])+change_users)+"\n"
            find = True
        data = data + line
    if not find:
        data = data + current_date + " 0 "+str(change_amount)+" 0 "+str(change_users)+"\n"
    

with open("log.txt","w+") as f:
    f.writelines(data) 
'''