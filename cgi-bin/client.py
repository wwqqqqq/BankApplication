#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

## 客户管理：提供客户所有信息的增删改查功能；如果客户存在着关联账户或者贷款记录，则不允许删除

## 身份证号_客户、身份证号_员工(贷款负责)、员工_身份证号_员工(银行账户负责)
## 姓名_客户、联系电话、家庭住址
## 联系人姓名、联系人手机号、联系人email、联系人与客户的关系

## FK：客户_贷款负责_员工(员工)、客户_银行账户负责_员工(员工)
## FK reference：借贷_借贷2_客户(借贷)
## FK reference：开户_储蓄_开户_储蓄_客户(开户_储蓄)、开户_支票_开户_支票_客户(开户_支票)

print('Content-type: text/html')
print('')

args = cgi.FieldStorage()
print('<div align="left"><form action="/cgi-bin/index.py" method="GET">')
print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #e8f0de;border: solid 1px #538312;background: #64991e; " >')
print('返回主页</button></form></div>')
print('<body style="background-color:#f7fdf7;" align="center">')
print('<h1 align="center">客户管理</h1><br><hr/><br>')
print('<h2>增加客户</h2>')
print('<form action="/cgi-bin/client_handler.py" method="GET">')
print('<p style="font-size:20px">姓名:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="name"/></p>')
print('<p style="font-size:20px">身份证号:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="id"/></p>')
print('<p style="font-size:20px">联系电话:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="tel"/></p>')
print('<p style="font-size:20px">家庭住址:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="address"/></p>')
print('<p style="font-size:20px">贷款负责人:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="creditmanager"/></p>')
print('<p style="font-size:20px">银行账户负责人:&nbsp<input type="text" name="accountmanager"/></p>')
print('<p style="font-size:20px">联系人姓名:&nbsp&nbsp<input type="text" name="contact_name"/>')
print('联系人手机号:&nbsp&nbsp<input type="text" name="contact_tel"/></p>')
print('<p style="font-size:20px">联系人email:&nbsp&nbsp<input type="text" name="contact_email"/>')
print('联系人与客户关系:&nbsp&nbsp<input type="text" name="contact_relation"/></p>')
print('<p style="font-size:20px"><input type="submit" value="提交" name="add"/></p></form><hr/>')
print('</body>')
print('<body style="background-color: #f7fdf7;" align="center"><br>')
if args.getvalue('query') or args.getvalue('queryall'):
    print('<h2>查询结果</h2>')
    print('<form action="/cgi-bin/client.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #e8f0de;border: solid 1px #538312;background: #64991e; " >')
    print('返回重新查询</button></form>')
    # 进行对数据库的查询并返回结果，在下面显示
    # 显示结果的同时，增加删除、修改按钮
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = "select * from 客户"
    name = args.getvalue('name')
    id = args.getvalue('id')
    tel = args.getvalue('tel')
    creditmanager = args.getvalue('creditmanager')
    accountmanager = args.getvalue('accountmanager')
    contact_name = args.getvalue('contact_name')
    contact_tel = args.getvalue('contact_tel')
    contact_email = args.getvalue('contact_email')
    if(args.getvalue('query')):
        sql = sql + " where "
        if(name):
            sql = sql + "姓名_客户 = '"+name+"' and "
        if(id):
            sql = sql + " 身份证号_客户 = '" +id +"' and "
        if(tel):
            sql = sql + "联系电话 = '"+tel+"' and "
        if(creditmanager):
            sql = sql + "身份证号_员工 = '"+creditmanager+"' and "
        if(accountmanager):
            sql = sql + " 员工_身份证号_员工 = '" +accountmanager +"' and "
        if(contact_name):
            sql = sql + "联系人姓名 = '"+contact_name+"' and "
        if(contact_tel):
            sql = sql + " 联系人手机号 = '" +contact_tel +"' and "
        if(contact_email):
            sql = sql + " \"联系人email\" = '" +contact_email +"' and "
        sql = sql + " 1=1"  

    print("<p> %s </p>" % sql)

    cr.execute(sql)
    rs = cr.fetchall()
    cr.close()
    db.close()
    print('<table border="1" align="center">')
    print('<form action="/cgi-bin/client_handler.py" method="GET"')
    print('<tr><th>姓名</th>')
    print('<th>身份证号</th>')
    print('<th>联系电话</th>')
    print('<th>家庭住址</th>')
    print('<th>贷款负责人</th>')
    print('<th>银行账户负责人</th>')
    print('<th>联系人姓名</th>')
    print('<th>联系人手机号</th>')
    print('<th>联系人email</th>')
    print('<th>联系人与客户关系</th>')    
    print('<th><input type="submit" value="修改" name="modify"/></th>')
    print('<th><input type="submit" value="删除" name="delete"/></th></tr>')
    for row in rs:
        print('<tr><td>')
        print(row[3])
        print('</td><td>')
        print(row[0])
        print('</td><td>')
        print(row[4])
        print('</td><td>')
        print(row[5])
        print('</td><td>')
        print(row[1])
        print('</td><td>')
        print(row[2])
        print('</td><td>')
        print(row[6])
        print('</td><td>')
        print(row[7])
        print('</td><td>')
        print(row[8])
        print('</td><td>')
        print(row[9])
        print('</td><td>')
        print('<input type="radio" name="m_id" value="'+row[0]+'">')
        print('</td><td>')
        print('<input type="radio" name="d_id" value="'+row[0]+'">')
        print('</td></tr>')
    print('</form>')
    print('</table>')

else:
    print('<h2>查询客户</h2>')
    print('<form action="/cgi-bin/client.py" method="GET">')
    print('<p style="font-size:20px">客户姓名:&nbsp&nbsp<input type="text" name="name"/>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp')
    print('<input type="submit" value="查询" name="query"/>')
    print('<input type="submit" value="查询全部" name="queryall"/></p>')
    print('<p style="font-size:20px">身份证号:&nbsp&nbsp&nbsp<input type="text" name="id"/>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp')
    print('联系电话:&nbsp&nbsp&nbsp<input type="text" name="tel"/></p>')
    print('<p style="font-size:20px">贷款负责人:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="creditmanager"/>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp')
    print('银行账户负责人:&nbsp<input type="text" name="accountmanager"/></p>')
    print('<p style="font-size:20px">联系人姓名:&nbsp&nbsp<input type="text" name="contact_name"/>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp')
    print('联系人手机号:&nbsp&nbsp<input type="text" name="contact_tel"/>&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp')
    print('联系人email:&nbsp&nbsp<input type="text" name="contact_email"/></p>')
    print('</form>')
print('</body>')