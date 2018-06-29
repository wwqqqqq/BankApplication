#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

## 员工管理：提供支行员工所有信息的增、删、改、查功能
## 如果员工存在关联数据，则不允许删除

## 身份证号_员工、部门号、员工_身份证号_员工(manager)、开始工作的日期
## 姓名_员工、电话号码_员工、家庭住址_员工

## FK: 部门(部门号)、员工(员工_身份证号_员工(manager))
## FK reference: 客户(贷款负责_员工)、客户(银行账户负责_员工)、员工(管理)

print('Content-type: text/html')
print('')

args = cgi.FieldStorage()
print('<div align="left"><form action="/cgi-bin/index.py" method="GET">')
print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #fae7e9;border: solid 1px #b73948;background: #da5867; " >')
print('返回主页</button></form></div>')
print('<body style="background-color:#fdf7f7;" align="center">')
print('<h1 align="center">员工管理</h1><br><hr/><br>')
print('<h2>增加员工</h2>')
print('<form action="/cgi-bin/staff_handler.py" method="GET">')
print('<p style="font-size:20px">姓名:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="name"/></p>')
print('<p style="font-size:20px">身份证号:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="id"/></p>')
print('<p style="font-size:20px">电话号码:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="tel"/></p>')
print('<p style="font-size:20px">家庭住址:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="address"/></p>')
print('<p style="font-size:20px">部门号:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="department"/></p>')
print('<p style="font-size:20px">部门经理身份证号:&nbsp<input type="text" name="manager"/></p>')
print('<p style="font-size:20px">开始工作的日期:&nbsp&nbsp<input type="date" name="begindate"/></p>')
print('<p style="font-size:20px"><input type="submit" value="提交" name="add"/></p></form><hr/>')
print('</body>')
print('<body style="background-color: #fdf7f7;" align="center"><br>')
if args.getvalue('query') or args.getvalue('queryall'):
    print('<h2>查询结果</h2>')
    print('<form action="/cgi-bin/staff.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #fae7e9;border: solid 1px #b73948;background: #da5867; " >')
    print('返回重新查询</button></form>')
    # 进行对数据库的查询并返回结果，在下面显示
    # 显示结果的同时，增加删除、修改按钮
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = 'select * from 员工'
    # name, id, tel, department, begindate
    name = args.getvalue('name')
    id = args.getvalue('id')
    tel = args.getvalue('tel')
    department = args.getvalue('department')
    begindate = args.getvalue('begindate')
    if(args.getvalue('query')):
        sql = sql + ' where '
        if(name):
            sql = sql + ' 姓名_员工 = \''+name +'\' and '
        if(id):
            sql = sql + ' 身份证号_员工 = \''+id +'\' and '
        if(tel):
            sql = sql + ' 电话号码_员工 = \''+tel+'\' and '
        if(department):
            sql = sql + ' 部门号 = \''+department+'\' and '
        if(begindate):
            sql = sql + ' 开始工作的日期 = to_date(\''+begindate+'\',\'yyyy-mm-dd\') and '
        sql = sql + '1=1'  
    print('<p> %s </p>'% sql)
    cr.execute(sql)
    rs = cr.fetchall()
    cr.close()
    db.close()
    print('<table border="1" align="center">')
    print('<form action="/cgi-bin/staff_handler.py" method="GET"')
    print('<tr><th>身份证号</th>')
    print('<th>部门号</th>') 
    print('<th>部门经理</th>')
    print('<th>开始工作的日期</th>')
    print('<th>姓名</th>')
    print('<th>电话号码</th>')
    print('<th>家庭住址</th>')             
    #print('<th>修改</th>')
    #print('<th>删除</th></tr>')
    print('<th><input type="submit" value="修改" name="modify"/></th>')
    print('<th><input type="submit" value="删除" name="delete"/></th></tr>')
    for row in rs:
        '''print('<tr><td>')
        print(row[0])
        print('</td><td>')
        print(row[1])
        print('</td><td>')
        print(row[2])
        print('</td><td>')'''
        print('<tr>')
        for item in row:
            if(isinstance(item, str)):
                print('<td>'+item+'</td>')
            else: #datetime
                t = item.strftime("%Y-%m-%d")
                print('<td>'+t+'</td>')
        print('<td>')
        #print('<form action="/cgi-bin/branch.py" method="GET"')
        #print('<button type="submit" value="'+row[0]+ '" name="modify" class="btn"/>修改</button></form>')
        print('<input type="radio" name="m_id" value="'+row[0]+'">')
        print('</td><td>')
        #print('<form action="/cgi-bin/branch.py" method="GET"')
        #print('<button type="submit" value="'+row[0]+ '" name="delete" />删除</button></form>')
        print('<input type="radio" name="d_id" value="'+row[0]+'">')
        print('</td></tr>')
    print('</form>')
    print('</table>')

else:
    print('<h2>查询员工</h2>')
    print('<form action="/cgi-bin/staff.py" method="GET">')
    print('<p style="font-size:20px">员工姓名:&nbsp&nbsp<input type="text" name="name"/>')
    print('<input type="submit" value="查询" name="query"/>')
    print('<input type="submit" value="查询全部" name="queryall"/></p>')
    print('<p style="font-size:20px">身份证号:&nbsp&nbsp&nbsp<input type="text" name="id"/></p>')
    print('<p style="font-size:20px">电话号码:&nbsp&nbsp&nbsp<input type="text" name="tel"/></p>')
    print('<p style="font-size:20px">部门号:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="department"/></p>')
    print('<p style="font-size:20px">开始工作的日期:&nbsp<input type="date" name="begindate"/></p>')
    print('</form>')
print('</body>')