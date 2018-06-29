#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os
import traceback
import time

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

## 账户管理：提供账户开户、销户、修改、查询功能，包括储蓄账户和支票账户；账户号不允许修改
## 账户号、支行名、余额、开户日期

## FK 账户_开户_支行(支行)
## FK reference 储蓄账户、支票账户

## 支票账户：账户号、支行名、余额、开户日期、透支额
## 储蓄账户：账户号、支行名、余额、开户日期、利率、货币类型



print('Content-type: text/html')
print('')

'''
add:
account, text, 账户号
balance, text, 余额
branch, text, 支行名
begindate, date, 开户日期
owners, text, 开户人身份证号 (多个开户人时用";"分开)
type = checking 支票账户; type = saving 储蓄账户
overdraft, text, 支票账户 - 透支额
rate, text, 储蓄账户 - 利率
currency, text, 货币类型
'''

db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
cr = db.cursor()
sql = "select sum(余额) from 储蓄账户"
cr.execute(sql)
rs = cr.fetchall()
saving_total = rs[0][0]

sql = "select count(身份证号_客户) from 开户_储蓄"
cr.execute(sql)
rs = cr.fetchall()
saving_users = rs[0][0]

cr.close()
db.close()


current_date = time.strftime("%Y-%m-%d", time.localtime())
    

def printinfo_add(account,balance,branch,begindate,owners,type,overdraft=None,rate=None,currency=None):
    print('<body align="center"><br><h1>已成功开户</h1>')
    print('<p>账户号: %s </p>' % account)
    print('<p>余额: %s </p>' % balance)
    print('<p>支行名: %s </p>' % branch)
    print('<p>开户日期 %s </p>' % begindate)
    print('<p>开户人身份证号:')
    owner_list = owners.split(';')
    for owner in owner_list:
        print('<br> %s' % owner)
    print('</p>')
    if(type=='checking'):
        print('<p>类型: 支票账户</p>')
        print('<p>透支额: %s</p>' % overdraft)
    else:
        print('<p>类型: 储蓄账户</p>')
        print('<p>利率: %s</p>' % rate)
        print('<p>货币类型: %s</p>' % currency)
    print('</body>')
def printinfo_modify(account,balance,branch,begindate,type,overdraft=None,rate=None,currency=None):
    print('<body align="center"><br><h1>已成功修改账户信息</h1>')
    print('<p>账户号: %s </p>' % account)
    print('<p>余额: %s </p>' % balance)
    print('<p>支行名: %s </p>' % branch)
    print('<p>开户日期 %s </p>' % begindate)
    if(type=='checking'):
        print('<p>类型: 支票账户</p>')
        print('<p>透支额: %s</p>' % overdraft)
    else:
        print('<p>类型: 储蓄账户</p>')
        print('<p>利率: %s</p>' % rate)
        print('<p>货币类型: %s</p>' % currency)
    print('</body>')
def printinfo_delete(account):
    print('<body align="center"><br><h1>已成功删除账户')
    print(account)
    print('</h1></body>')
def ret_btn():
    print('<form action="/cgi-bin/account.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #feeef5;border: solid 1px #d2729e;background: #f895c2; " >')
    print('返回账户管理</button></form>')




args = cgi.FieldStorage()
if(args.getvalue('add')):
    # >>> db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    current_date = args.getvalue('begindate')
    account = args.getvalue('account')
    balance = args.getvalue('balance')
    branch = args.getvalue('branch')
    begindate = args.getvalue('begindate')
    owners = args.getvalue('owners')
    type = args.getvalue('type')
    overdraft = args.getvalue('overdraft')
    rate = args.getvalue('rate')
    currency = args.getvalue('currency')
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql1 = 'insert into 账户 (账户号, 支行名, 余额, 开户日期) values('
        sql1 = sql1 + '\'' + account + '\', \'' + branch + '\', ' + balance + ', to_date(\''+begindate+'\',\'yyyy-mm-dd\') )' 
        print(sql1)
        cr.execute(sql1)
        sql2 = 'insert into '
        if(type=='checking'):
            sql2 = sql2 + '支票账户 '
            sql2 = sql2 + '(账户号, 支行名, 余额, 开户日期, 透支额) values('
            sql2 = sql2 + '\'' + account + '\', \'' + branch + '\', ' + balance + ', to_date(\''+begindate+'\',\'yyyy-mm-dd\'), '+overdraft+')' 
        else:
            sql2 = sql2 + '储蓄账户'
            sql2 = sql2 + '(账户号, 支行名, 余额, 开户日期, 利率, 货币类型) values('
            sql2 = sql2 + '\'' + account + '\', \'' + branch + '\', ' + balance + ', to_date(\''+begindate+'\',\'yyyy-mm-dd\'), '+rate+',\''+currency+'\')' 
        print(sql2)
        cr.execute(sql2)
        current_date = time.strftime('%Y-%m-%d',time.localtime(time.time())) # 当前时间
        sql3 = "insert into "
        if(type=='checking'):
            sql3 = sql3 + '开户_支票 (身份证号_客户, 账户号, 支行名, 所有者最近访问账户日期_支票) '
        else:
            sql3 = sql3 + '开户_储蓄 (身份证号_客户, 账户号, 支行名, 所有者最近访问账户日期_储蓄) '
        sql3 = sql3 + 'values(' +'\''
        owner_list = owners.split(';')
        for owner in owner_list:
            temp = sql3 + owner +'\', \''+ account + '\', \'' + branch + '\', to_date(\''+current_date+'\',\'yyyy-mm-dd\'))'
            print(temp)
            cr.execute(temp)
        cr.close()
        db.commit()
        db.close()
        printinfo_add(account,balance,branch,begindate,owners,type,overdraft,rate,currency)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<br><br>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!')
elif(args.getvalue('modify')):
    print('<body align="center"><br><h1>直接在下面进行修改</h1>')
    account = args.getvalue('m_account')
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = 'select * from 储蓄账户 where 账户号 = \''+account +'\' '
    cr.execute(sql)
    rs = cr.fetchall()
    type = "saving"
    if(rs==[]):
        type="checking"
        sql = 'select * from 支票账户 where 账户号 = \''+account +'\' '
        cr.execute(sql)
        rs = cr.fetchall()
    cr.close()
    db.close()
    for row in rs:
        print('<p>')
        print(row)
        print('</p>')
    t = row[3].strftime("%Y-%m-%d")
    print('<form action="/cgi-bin/account_handler.py" method="GET">')
    print('<p style="font-size:20px">账户号:&nbsp&nbsp&nbsp<input type="text" name="account" value="'+row[0]+'"/>&nbsp&nbsp')
    print('余额:&nbsp&nbsp&nbsp<input type="text" name="balance" value="'+str(row[2])+'"/></p>')
    print('<p style="font-size:20px">支行名:&nbsp&nbsp&nbsp<input type="text" name="branch" value="'+row[1]+'"/>&nbsp&nbsp')
    print('开户日期:&nbsp<input type="date" name="begindate" value="'+t+'"/></p>')
    if(type=='checking'):
        print('<p style="font-size:20px">透支额:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="overdraft" value="'+str(row[4])+'"/></p>')
    else:
        print('<p style="font-size:20px">利率:&nbsp&nbsp<input type="text" name="rate" value="'+str(row[4])+'"/>')
        print('&nbsp&nbsp&nbsp&nbsp&nbsp货币类型:&nbsp&nbsp<input type="text" name="currency" value="'+row[5]+'"/></p>')
    print('<p style="font-size:20px"><input type="submit" value="提交" name="modify2"/></p></form><hr/>')
    print('</body>')
elif(args.getvalue('modify2')):
    # stage2 of mofify
    account = args.getvalue('account')
    balance = args.getvalue('balance')
    branch = args.getvalue('branch')
    begindate = args.getvalue('begindate')
    owners = args.getvalue('owners')
    overdraft = args.getvalue('overdraft')
    rate = args.getvalue('rate')
    currency = args.getvalue('currency')
    type = "checking"
    db_name = " 支票账户 "
    if(rate):
        type = "saving"
        db_name = " 储蓄账户 "
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql = "Update"+db_name+"set 支行名='"+branch+"' where 账户号='"+account+"'"
        sql2 = "Update 账户 set 支行名='"+branch+"' where 账户号='"+account+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        print('<p>'+sql2+'</p>')
        cr.execute(sql2)
        sql = "Update"+db_name+"set 余额='"+balance+"' where 账户号='"+account+"'"
        sql2 = "Update 账户 set 余额='"+balance+"' where 账户号='"+account+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        print('<p>'+sql2+'</p>')
        cr.execute(sql2)
        sql = "Update"+db_name+"set 开户日期=to_date('"+begindate+"','yyyy-mm-dd') where 账户号='"+account+"'"
        sql2 = "Update 账户 set 开户日期=to_date('"+begindate+"','yyyy-mm-dd') where 账户号='"+account+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        print('<p>'+sql2+'</p>')
        cr.execute(sql2)
        if(type=="checking"):
            sql = "Update"+db_name+"set 透支额='"+overdraft+"' where 账户号='"+account+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
        else:
            sql = "Update"+db_name+"set 利率='"+rate+"' where 账户号='"+account+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
            sql = "Update"+db_name+"set 货币类型='"+currency+"' where 账户号='"+account+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_modify(account,balance,branch,begindate,type,overdraft,rate,currency)
        ret_btn()
    except:
        print('<br><br>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!')
elif(args.getvalue('delete')):
    account = args.getvalue('d_account')
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql = 'select * from 储蓄账户 where 账户号 = \''+account +'\' '
        cr.execute(sql)
        rs = cr.fetchall()
        db_name = " 储蓄账户 "
        db_name2 = " 开户_储蓄 "
        if(rs==[]):
            db_name = " 支票账户 "
            db_name2 = " 开户_支票 "
        sql = "Delete From "+ db_name +" where 账户号='"+account+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "Delete From "+ db_name2 +" where 账户号='"+account+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "Delete From 账户 where 账户号='"+account+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_delete(account)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<p>')
        traceback.print_exc()
        print('<br>错误！无法删除！</p>')



data = ""

db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
cr = db.cursor()
sql = "select sum(余额) from 储蓄账户"
cr.execute(sql)
rs = cr.fetchall()
change_amount = rs[0][0] - saving_total

sql = "select count(身份证号_客户) from 开户_储蓄"
cr.execute(sql)
rs = cr.fetchall()
change_users = rs[0][0] - saving_users

cr.close()
db.close()

with open("log.txt","r+") as f:
    f.seek(0,0)

    find = False
    for line in f.readlines():
        if(line.startswith(current_date)):
            temp = line.split(" ")
            line = temp[0] + " "+str(int(temp[1])+change_amount)+" "+temp[2]+" "+str(int(temp[3])+change_users)+" "+temp[4]+"\n"
            find = True
        data = data + line
    if not find:
        data = data + current_date + " "+str(change_amount)+" 0 "+str(change_users)+" 0\n"
    

with open("log.txt","w+") as f:
    f.writelines(data) 
        

