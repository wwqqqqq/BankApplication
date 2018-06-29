#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

## 贷款管理：提供贷款信息的增删查功能，提供贷款发放功能；贷款信息一旦添加成功后不允许修改；
## 要求能查询每笔贷款的当前状态(未开始发放、发放中、已全部发放)；
## 处于发放中状态的贷款记录不允许删除

## 贷款: 贷款号、支行名、所贷金额
## 借贷: 贷款号、身份证号_客户
## 贷款支付: 贷款号、日期、金额

print('Content-type: text/html')
print('')

args = cgi.FieldStorage()
print('<html><div align="left"><form action="/cgi-bin/index.py" method="GET">')
print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #fef4e9;border: solid 1px #da7c0c;background: #f78d1d; " >')
print('返回主页</button></form></div>')
print('<body style="background-color: #fdfaf7;" align="center">')
print('<h1 align="center">贷款管理</h1><br><hr/><br>')
print('<h2>添加贷款</h2>')
print('<form action="/cgi-bin/loan_handler.py" method="GET">')
print('<p style="font-size:20px">贷款号:&nbsp<input type="text" name="loanid"/></p>')
print('<p style="font-size:20px">支行名:&nbsp&nbsp&nbsp<input type="text" name="branch"/></p>')
print('<p style="font-size:20px">所贷金额:&nbsp&nbsp&nbsp<input type="text" name="amount"/></p>')
print('<p style="font-size:20px">贷款人身份证号 (多个贷款人时用";"分开):<br><br><input type="text" name="lenders"/></p>')
print('<p style="font-size:20px"><input type="submit" value="提交" name="add"/></p></form><hr/><br>')

print('<h2>发放贷款</h2>')
print('<form action="/cgi-bin/loan_handler.py" method="GET">')
print('<p style="font-size:20px">贷款号:&nbsp<input type="text" name="loanid"/></p>')
print('<p style="font-size:20px">日期:&nbsp&nbsp&nbsp<input type="date" name="time"/></p>')
print('<p style="font-size:20px">金额:&nbsp&nbsp&nbsp<input type="text" name="amount"/></p>')
print('<p style="font-size:20px"><input type="submit" value="提交" name="pay"/></p></form><hr/><br>')

if args.getvalue('query') or args.getvalue('queryall'):
    print('<h2>查询结果</h2>')
    print('<form action="/cgi-bin/loan.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #fef4e9;border: solid 1px #da7c0c;background: #f78d1d; " >')
    print('返回重新查询</button></form>')
    # 进行对数据库的查询并返回结果，在下面显示
    # 显示结果的同时，增加删除、修改、查询支付记录按钮

    # 状态：未开始发放，发放中，已全部发放
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = 'select * from 贷款'

    loanid = args.getvalue('loanid')
    lenders = args.getvalue('lenders')
    branch = args.getvalue('branch')

    if(args.getvalue('query')):
        sql = sql + ' where '
        if(loanid):
            sql = sql + ' 贷款号 = '+loanid +' and '
        if(branch):
            sql = sql + ' 支行名 = '+branch +' and '
        if(lenders):
            lender_list = lenders.split(';')
            sql = sql + ' 贷款号 in (select 贷款号 from 借贷 '
            sql = sql + ' where '
            for lender in lender_list:
                sql = sql + '身份证号_客户 = ' + lender + ' or '
            sql = sql + '1=0)'
        else:
            sql = sql + '1=1'

    print('<p> %s </p>'% sql)

    cr.execute(sql)
    rs = cr.fetchall()
    print('<table border="1" align="center">')
    print('<form action="/cgi-bin/loan_handler.py" method="GET"')
    print('<tr><th>贷款号</th>')
    print('<th>支行名</th>')
    print('<th>金额</th>')
    print('<th>状态</th>')
    print('<th><input type="submit" value="删除" name="delete"/></th></tr>')
    for row in rs:
        print('<tr><td>')
        print(row[0])
        print('</td><td>')
        print(row[1])
        print('</td><td>')
        print(row[2])
        print('</td><td>')
        sql = "select * from 贷款支付 where 贷款号 = '"+row[0]+"'"
        cr.execute(sql)
        r = cr.fetchall()
        sum = 0
        for i in r:
            sum = sum + i[2]
        if(sum==0):
            print('未开始发放</td><td>')
            print('<input type="radio" name="d_loanid" value="'+row[0]+'">')
        elif(sum>=row[2]):
            print('已全部发放</td><td>')
            print('<input type="radio" name="d_loanid" value="'+row[0]+'">')
        else:
            print('发放中</td><td>')
            print('无法删除')
        print('</td></tr>')
    print('</form>')
    print('</table>')
    cr.close()
    db.close()


else:
    print('<h2>查询贷款</h2>')
    print('<form action="/cgi-bin/loan.py" method="GET">')
    print('<p style="font-size:20px">贷款号:&nbsp<input type="text" name="loanid"/>')
    print('<input type="submit" value="查询" name="query"/>')
    print('<input type="submit" value="查询全部" name="queryall"/></p>')
    print('<p style="font-size:20px">贷款人身份证号:&nbsp<input type="text" name="lenders"/></p>')
    print('<p style="font-size:20px">支行名:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="branch"/></p></form>')
print('</body></html>')