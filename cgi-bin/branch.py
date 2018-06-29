#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

## 支行管理：提供支行所有信息的增、删、改、查功能；如果支行存在着关联信息，如员工、账户等，则不允许删除
## 支行名、城市、资产
## 贷款、账户、开户(储蓄、支票)

print('Content-type: text/html; charset = utf-8')
print('')

args = cgi.FieldStorage()
#print('<h1>Hello {}, Website {}</h1>'.format(args.getvalue('name'), args.getvalue('url')))
print('<div align="left"><form action="/cgi-bin/index.py" method="GET">')
print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #d9eef7;border: solid 1px #0076a3;background: #0095cd; " >')
print('返回主页</button></form></div>')
print('<body style="background-color: rgb(241, 247, 250);" align="center">')
print('<h1 align="center">支行管理</h1><br><hr/><br>')
print('<h2>增加支行</h2>')
print('<form action="/cgi-bin/branch_handler.py" method="GET">')
print('<p style="font-size:20px">支行名:&nbsp<input type="text" name="name"/></p>')
print('<p style="font-size:20px">城市:&nbsp&nbsp&nbsp<input type="text" name="city"/></p>')
print('<p style="font-size:20px">资产:&nbsp&nbsp&nbsp<input type="text" name="property"/></p>')
print('<p style="font-size:20px"><input type="submit" value="提交" name="add"/></p></form><hr/>')
print('</body>')
print('<body style="background-color: rgb(241, 247, 250);" align="center"><br>')
if args.getvalue('query') or args.getvalue('queryall'):
    print('<h2>查询结果</h2>')
    print('<form action="/cgi-bin/branch.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #d9eef7;border: solid 1px #0076a3;background: #0095cd; " >')
    print('返回重新查询</button></form>')
    # 进行对数据库的查询并返回结果，在下面显示
    # 显示结果的同时，增加删除、修改按钮
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = 'select * from 支行'
    name = args.getvalue('name')
    city = args.getvalue('city')
    property = args.getvalue('property')
    owners = args.getvalue('owners')
    type = args.getvalue('type')
    if(args.getvalue('query')):
        sql = sql + ' where '
        if(name):
            sql = sql + ' 支行名 = \''+name +'\' and '
        if(city):
            sql = sql + ' 城市 = \''+city +'\' and '
        if(property):
            sql = sql + ' 资产 = '+property+' and '
        # 支行名, 城市, 资产
        sql = sql + '1=1'  

    print('<p> %s </p>'% sql)

    cr.execute(sql)
    rs = cr.fetchall()
    cr.close()
    db.close()
    print('<table border="1" align="center">')
    print('<form action="/cgi-bin/branch_handler.py" method="GET"')
    print('<tr><th>支行名</th>')
    print('<th>城市</th>')
    print('<th>资产</th>')    
    #print('<th>修改</th>')
    #print('<th>删除</th></tr>')
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
        #print('<form action="/cgi-bin/branch.py" method="GET"')
        #print('<button type="submit" value="'+row[0]+ '" name="modify" class="btn"/>修改</button></form>')
        print('<input type="radio" name="m_branch" value="'+row[0]+'">')
        print('</td><td>')
        #print('<form action="/cgi-bin/branch.py" method="GET"')
        #print('<button type="submit" value="'+row[0]+ '" name="delete" />删除</button></form>')
        print('<input type="radio" name="d_branch" value="'+row[0]+'">')
        print('</td></tr>')
    print('</form>')
    print('</table>')
    

else:
    print('<h2>查询支行</h2>')
    print('<form action="/cgi-bin/branch.py" method="GET">')
    print('<p style="font-size:20px">支行名:&nbsp<input type="text" name="name"/>')
    print('<input type="submit" value="查询" name="query"/>')
    print('<input type="submit" value="查询全部" name="queryall"/></p>')
    print('<p style="font-size:20px">城市:&nbsp&nbsp&nbsp<input type="text" name="city"/>')
    print('资产:&nbsp&nbsp&nbsp<input type="text" name="property"/></p></form>')
print('</body>')

