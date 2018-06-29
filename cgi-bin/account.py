#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

## 账户管理：提供账户开户、销户、修改、查询功能，包括储蓄账户和支票账户；账户号不允许修改
## 账户号、支行名、余额、开户日期

## FK 账户_开户_支行(支行)
## FK reference 储蓄账户、支票账户

## 支票账户：账户号、支行名、余额、开户日期、透支额
## 储蓄账户：账户号、支行名、余额、开户日期、利率、货币类型


print('Content-type: text/html')
print('')

args = cgi.FieldStorage()
print('<div align="left"><form action="/cgi-bin/index.py" method="GET">')
print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #feeef5;border: solid 1px #d2729e;background: #f895c2; " >')
print('返回主页</button></form></div>')
print('<body style="background-color: #fdf7fa;" align="center">')
print('<h1 align="center">账户管理</h1><br><hr/><br>')
print('<h2>账户开户</h2>')
print('<form action="/cgi-bin/account_handler.py" method="GET">')
print('<p style="font-size:20px">账户号:&nbsp&nbsp&nbsp<input type="text" name="account"/>&nbsp&nbsp')
print('余额:&nbsp&nbsp&nbsp<input type="text" name="balance"/></p>')
print('<p style="font-size:20px">支行名:&nbsp&nbsp&nbsp<input type="text" name="branch"/>&nbsp&nbsp')
print('开户日期:&nbsp<input type="date" name="begindate"/></p>')
print('<p style="font-size:20px">开户人身份证号 (多个开户人时用";"分开):<br><br><input type="text" name="owners"/></p>')
print('<p style="font-size:20px"><input type="radio" name="type" value="checking" checked> 支票账户')
print('<input type="radio" name="type" value="saving"> 储蓄账户</p>')
print('<p style="font-size:20px">支票账户 - 透支额:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="overdraft"/></p>')
print('<p style="font-size:20px">储蓄账户 - 利率:&nbsp&nbsp<input type="text" name="rate"/>')
print('&nbsp&nbsp&nbsp&nbsp&nbsp货币类型:&nbsp&nbsp<input type="text" name="currency"/></p>')
print('<p style="font-size:20px"><input type="submit" value="提交" name="add"/></p></form><hr/>')
print('</body>')
print('<body style="background-color: #fdf7fa;" align="center"><br>')
if args.getvalue('query') or args.getvalue('queryall'):
    print('<h2>查询结果</h2>')
    print('<form action="/cgi-bin/account.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #feeef5;border: solid 1px #d2729e;background: #f895c2; " >')
    print('返回重新查询</button></form>')
    # 进行对数据库的查询并返回结果，在下面显示
    # 显示结果的同时，增加删除、修改按钮
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = 'select * from '
    account = args.getvalue('account')
    branch = args.getvalue('branch')
    begindate = args.getvalue('begindate')
    owners = args.getvalue('owners')
    type = args.getvalue('type')
    if(type=='checking'):
        sql = sql + '支票账户'
    else:
        sql = sql + '储蓄账户'
    if(args.getvalue('query')):
        sql = sql + ' where '
        if(account):
            sql = sql + ' 账户号 = '+account +' and '
        if(branch):
            sql = sql + ' 支行名 = '+branch +' and '
        #if(begindate):
        #    sql = sql + 'begindate = '+begindate+' and '
        if(owners):
            owner_list = owners.split(';')
            sql = sql + ' 账户号 in (select 账户号 from '
            if(type=='checking'):
                sql = sql + '开户_支票'
            else:
                sql = sql + '开户_储蓄'
            sql = sql + ' where '
            for owner in owner_list:
                sql = sql + '身份证号_客户 = ' + owner + ' or '
            sql = sql + '1=0)'
        else:
            sql = sql + '1=1'

    print('<p> %s </p>'% sql)

    cr.execute(sql)
    rs = cr.fetchall()
    cr.close()
    db.close()
    print('<table border="1" align="center">')
    print('<form action="/cgi-bin/account_handler.py" method="GET"')
    print('<tr><th>账户号</th>')
    print('<th>支行名</th>')
    print('<th>余额</th>')    
    print('<th>开户日期</th>')
    if(type=="checking"):
        print('<th>透支额</th>')
    else:
        print('<th>利率</th>')
        print('<th>货币类型</th>')
    print('<th><input type="submit" value="修改" name="modify"/></th>')
    print('<th><input type="submit" value="删除" name="delete"/></th></tr>')
    for row in rs:
        print('<tr><td>')
        print(row[0])
        print('</td><td>')
        print(row[1])
        print('</td><td>')
        print(row[2])
        print('</td><td>')
        t = row[3].strftime("%Y-%m-%d")
        print(t) # 开户日期
        print('</td><td>')
        print(row[4])
        print('</td><td>')
        if(type=="saving"):
            print(row[5])
            print('</td><td>')
        print('<input type="radio" name="m_account" value="'+row[0]+'">')
        print('</td><td>')
        print('<input type="radio" name="d_account" value="'+row[0]+'">')
        print('</td></tr>')
    print('</form>')
    print('</table>')

    


else:
    print('<h2>账户查询</h2>')
    print('<form action="/cgi-bin/account.py" method="GET">')
    print('<p style="font-size:20px">账户号:&nbsp<input type="text" name="account"/>')
    print('<input type="radio" name="type" value="checking" checked> 支票账户')
    print('<input type="radio" name="type" value="saving"> 储蓄账户')
    print('<input type="submit" value="查询" name="query"/>')
    print('<input type="submit" value="查询全部" name="queryall"/></p>')
    print('<p style="font-size:20px">开户人身份证号:&nbsp<input type="text" name="owners"/></p>')
    print('<p style="font-size:20px">支行名:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="branch"/></p>')
    print('<p style="font-size:20px">开户日期:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="date" name="begindate"/></p></form>')
print('</body>')