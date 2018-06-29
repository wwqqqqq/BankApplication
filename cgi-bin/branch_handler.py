#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os
import traceback
import cgitb

cgitb.enable()

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

## 支行管理：提供支行所有信息的增、删、改、查功能；如果支行存在着关联信息，如员工、账户等，则不允许删除
## 支行名、城市、资产
## 贷款、账户、开户(储蓄、支票)


print('Content-type: text/html; charset = utf-8')
print('')

'''
add:
name, text, 支行名
city, text, 城市
property, text, 资产
'''

def printinfo_add(name, city, property):
    print('<body align="center"><br><h1>已成功添加新的支行</h1>')
    print('<p>支行名: %s </p>' % name)
    print('<p>城市: %s </p>' % city)
    print('<p>资产: %s </p>' % property)
    print('</body>')
def printinfo_modify(name, city, property):
    print('<body align="center"><br><h1>已成功修改支行，新的支行信息如下</h1>')
    print('<p>支行名: %s </p>' % name)
    print('<p>城市: %s </p>' % city)
    print('<p>资产: %s </p>' % property)
    print('</body>')
def printinfo_delete(name):
    print('<body align="center"><br><h1>已成功删除支行')
    print(name)
    print('</h1></body>')
def ret_btn():
    print('<body align="center"><form action="/cgi-bin/branch.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #d9eef7;border: solid 1px #0076a3;background: #0095cd; " >')
    print('返回支行管理</button></form></body>')


args = cgi.FieldStorage()
if(args.getvalue('add')):
    # >>> db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    name = args.getvalue('name')
    city = args.getvalue('city')
    property = args.getvalue('property')
    try:
        sql = 'insert into 支行 (支行名, 城市, 资产) values('
        sql = sql + '\'' + name +'\', \'' + city + '\', '+ property + ')'
        print('<p>'+sql+'</p>')
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_add(name, city, property)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<p>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!</p>')
elif(args.getvalue('modify')):
    print('<body align="center"><br><h1>直接在下面进行修改</h1>')
    branch = args.getvalue('m_branch')
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = 'select * from 支行 where 支行名 = \''+branch +'\' '
    cr.execute(sql)
    rs = cr.fetchall()
    cr.close()
    db.close()
    for row in rs:
        print('<p>')
        print(row)
        print('</p>')
    print('<form action="/cgi-bin/branch_handler.py" method="GET">')
    print('<p style="font-size:20px">支行名:&nbsp<input type="text" name="name" value="'+branch+'"/></p>')
    print('<p style="font-size:20px">城市:&nbsp&nbsp&nbsp<input type="text" name="city" value="'+row[1]+'"/></p>')
    print('<p style="font-size:20px">资产:&nbsp&nbsp&nbsp<input type="text" name="property" value="'+row[2]+'"/></p>')
    print('<p><input type="hidden" name="old_branch" value="'+branch+'"/></p>')
    print('<p style="font-size:20px"><input type="submit" value="提交" name="modify2"/></p></form><hr/>')
    print('</body>')
elif(args.getvalue('modify2')):
    # stage2 of mofify
    name = args.getvalue('name')
    city = args.getvalue('city')
    branch = args.getvalue('old_branch')
    property = args.getvalue('property')
    try:
        #sql = 'insert into 支行 (支行名, 城市, 资产) values('
        #sql = sql + '\'' + name +'\', \'' + city + '\', '+ property + ')'
        sql1 = "Update 支行 set 城市='"+city+"' where 支行名='"+branch+"'"
        sql2 = "Update 支行 set 资产="+property+" where 支行名='"+branch+"'"
        print('<p>'+sql1+'</p>')
        print('<p>'+sql2+'</p>')
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        cr.execute(sql1)
        cr.execute(sql2)
        if(branch!=name):
            sql = "Update 支行 set 支行名='"+name+"' where 支行名='"+branch+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
            sql = "Update 开户_支票 set 支行名='"+name+"' where 支行名='"+branch+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
            sql = "Update 开户_储蓄 set 支行名='"+name+"' where 支行名='"+branch+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
            sql = "Update 贷款 set 支行名='"+name+"' where 支行名='"+branch+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
            sql = "Update 账户 set 支行名='"+name+"' where 支行名='"+branch+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
            sql = "Update 储蓄账户 set 支行名='"+name+"' where 支行名='"+branch+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
            sql = "Update 支票账户 set 支行名='"+name+"' where 支行名='"+branch+"'"
            print('<p>'+sql+'</p>')
            cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_modify(name, city, property)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<br><br>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!')
elif(args.getvalue('delete')):
    branch = args.getvalue('d_branch')
    #branch = branch
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql = "select * from 开户_支票 where 支行名='"+branch+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("该支行存在关联信息，无法删除")
            raise Exception
        sql = "select * from 开户_储蓄 where 支行名='"+branch+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("该支行存在关联信息，无法删除")
            raise Exception
        sql = "select * from 账户 where 支行名='"+branch+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("该支行存在关联信息，无法删除")
            raise Exception
        sql = "select * from 贷款 where 支行名='"+branch+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("该支行存在关联信息，无法删除")
            raise Exception
        sql = "Delete From 支行 where 支行名='"+branch+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        #cr.execute(sql2)
        cr.close()
        db.commit()
        db.close()
        printinfo_delete(branch)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<p>')
        traceback.print_exc()
        print('<br>错误！无法删除！</p>')

