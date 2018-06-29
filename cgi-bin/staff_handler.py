#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os
import traceback
import cgitb

cgitb.enable()

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

'''create table 员工 (
   身份证号_员工              CHAR(256)             not null,
   部门号                  CHAR(256)             not null,
   员工_身份证号_员工           CHAR(256),
   开始工作的日期              DATE                  not null,
   姓名_员工                CHAR(256)             not null,
   电话号码_员工              CHAR(256)             not null,
   家庭地址_员工              CHAR(256)             not null,
   constraint PK_员工 primary key (身份证号_员工)
);
'''


print('Content-type: text/html; charset = utf-8')
print('')

'''
add:
name, text, 员工姓名
id, text, 身份证号
tel, text, 电话号码
address, text, 家庭住址
department, text, 部门号
begindate, date, 开始工作的日期
manager, text, 部门经理身份证号
'''


def printinfo_add(name, id, tel, address, department, begindate, manager):
    print('<body align="center"><br><h1>已成功添加新的员工信息</h1>')
    print('<p>员工姓名: %s </p>' % name)
    print('<p>身份证号: %s </p>' % id)
    print('<p>电话号码: %s </p>' % tel)
    print('<p>家庭住址: %s </p>' % address)
    print('<p>部门号: %s </p>' % department)
    print('<p>部门经理身份证号: %s </p>' % manager)
    print('<p>开始工作的日期: %s </p>' % begindate)
    print('</body>')
def printinfo_modify(name, id, tel, address, department, begindate, manager):
    print('<body align="center"><br><h1>已成功修改员工信息，修改后如下</h1>')
    print('<p>员工姓名: %s </p>' % name)
    print('<p>身份证号: %s </p>' % id)
    print('<p>电话号码: %s </p>' % tel)
    print('<p>家庭住址: %s </p>' % address)
    print('<p>部门号: %s </p>' % department)
    print('<p>部门经理身份证号: %s </p>' % manager)
    print('<p>开始工作的日期: %s </p>' % begindate)
    print('</body>')
def printinfo_delete(id):
    print('<body align="center"><br><h1>已成功删除身份证号为')
    print(id)
    print('的员工信息</h1></body>')
def ret_btn():
    print('<form action="/cgi-bin/staff.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #fae7e9;border: solid 1px #b73948;background: #da5867; " >')
    print('返回员工管理</button></form>')


args = cgi.FieldStorage()

'''
alter table 员工
   add constraint FK_员工_供职_部门 foreign key (部门号)
      references 部门 (部门号);

alter table 员工
   add constraint FK_员工_管理_员工 foreign key (员工_身份证号_员工)
      references 员工 (身份证号_员工);

alter table 客户
   add constraint FK_客户_贷款负责_员工 foreign key (员工_身份证号_员工)
      references 员工 (身份证号_员工);

alter table 客户
   add constraint FK_客户_银行账户负责_员工 foreign key (身份证号_员工)
      references 员工 (身份证号_员工);
'''
if(args.getvalue('add')):
    # >>> db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    name = args.getvalue('name')
    id = args.getvalue('id')
    tel = args.getvalue('tel')
    address = args.getvalue('address')
    department = args.getvalue('department')
    begindate = args.getvalue('begindate')
    manager = args.getvalue('manager')
    try:
        sql = "insert into 员工 (身份证号_员工, 部门号, 员工_身份证号_员工, 开始工作的日期, 姓名_员工, 电话号码_员工, 家庭地址_员工) values("
        sql = sql + "'" + id +"', '" + department + "', '"+ manager + "', to_date('"+begindate+"','yyyy-mm-dd'), '"+name+"', '"+tel+"', '"+address+"')"
        print("<p>"+sql+"</p>")
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        if(id == manager):
            sql1 = "Alter Table 员工 Drop Constraint FK_员工_管理_员工"
            cr.execute(sql1)
            cr.execute(sql)
            sql2 = "alter table 员工 add constraint FK_员工_管理_员工 foreign key (员工_身份证号_员工) references 员工 (身份证号_员工)"
            cr.execute(sql2)
        else:
            cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_add(name, id, tel, address, department, begindate, manager)
        ret_btn()
    except:
        print('<p>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!</p>')
elif(args.getvalue('modify')):
    print('<body align="center"><br><h1>直接在下面进行修改</h1>')
    id = args.getvalue('m_id')
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = 'select * from 员工 where 身份证号_员工 = \''+id +'\' '
    cr.execute(sql)
    rs = cr.fetchall()
    cr.close()
    db.close()
    for row in rs:
        print('<p>')
        print(row)
        print('</p>')
    t = row[3].strftime("%Y-%m-%d")
    print('<form action="/cgi-bin/staff_handler.py" method="GET">')
    print('<p style="font-size:20px">姓名:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="name", value="'+row[4]+'"/></p>')
    print('<p style="font-size:20px">身份证号:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="id", value="'+row[0]+'"/></p>')
    print('<p style="font-size:20px">电话号码:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="tel", value="'+row[5]+'"/></p>')
    print('<p style="font-size:20px">家庭住址:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="address", value="'+row[6]+'"/></p>')
    print('<p style="font-size:20px">部门号:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="department", value="'+row[1]+'"/></p>')
    print('<p style="font-size:20px">部门经理身份证号:&nbsp<input type="text" name="manager", value="'+row[2]+'"/></p>')
    print('<p style="font-size:20px">开始工作的日期:&nbsp&nbsp<input type="date" name="begindate", value="'+t+'"/></p>')
    print('<p style="font-size:20px"><input type="submit" value="提交" name="modify2"/></p></form><hr/>')
    print('</body>')
elif(args.getvalue('modify2')):
    # stage2 of mofify
    name = args.getvalue('name')
    id = args.getvalue('id')
    tel = args.getvalue('tel')
    address = args.getvalue('address')
    department = args.getvalue('department')
    begindate = args.getvalue('begindate')
    manager = args.getvalue('manager')
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql = "Update 员工 set 部门号='"+department+"' where 身份证号_员工='"+id+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        sql = "Update 员工 set 员工_身份证号_员工='"+manager+"' where 身份证号_员工='"+id+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        sql = "Update 员工 set 开始工作的日期=to_date('"+begindate+"','yyyy-mm-dd') where 身份证号_员工='"+id+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        sql = "Update 员工 set 姓名_员工='"+name+"' where 身份证号_员工='"+id+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        sql = "Update 员工 set 电话号码_员工='"+tel+"' where 身份证号_员工='"+id+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        sql = "Update 员工 set 家庭地址_员工='"+address+"' where 身份证号_员工='"+id+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_modify(name, id, tel, address, department, begindate, manager)
        ret_btn()
    except:
        print('<br><br>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!')
elif(args.getvalue('delete')):
    id = args.getvalue('d_id')
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql = "select * from 员工 where 员工_身份证号_员工='"+id+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("该员工为部门经理，无法删除")
            raise Exception
        sql = "select * from 客户 where 员工_身份证号_员工='"+id+"' or 身份证号_员工 = '"+id+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("该员工为某客户的贷款或银行账户负责人，无法删除")
            raise Exception
        sql = "Delete From 员工 where 身份证号_员工='"+id+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_delete(id)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<p>')
        traceback.print_exc()
        print('<br>错误！无法删除！</p>')

