#!C:\Users\weiq6\Anaconda3\python.exe
import cgi
import cx_Oracle
import os
import traceback
import cgitb

cgitb.enable()

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'

'''
create table 客户 (
   身份证号_客户              CHAR(256)             not null,
   身份证号_员工              CHAR(256),
   员工_身份证号_员工           CHAR(256),
   姓名_客户                CHAR(256)             not null,
   联系电话                 CHAR(256)             not null,
   家庭住址                 CHAR(256)             not null,
   联系人姓名                CHAR(256)             not null,
   联系人手机号               CHAR(256)             not null,
   "联系人email"           CHAR(256)             not null,
   联系人与客户的关系            CHAR(256)             not null,
   constraint PK_客户 primary key (身份证号_客户)
);
alter table 客户
   add constraint FK_客户_贷款负责_员工 foreign key (员工_身份证号_员工)
      references 员工 (身份证号_员工);

alter table 客户
   add constraint FK_客户_银行账户负责_员工 foreign key (身份证号_员工)
      references 员工 (身份证号_员工);
'''


print('Content-type: text/html; charset = utf-8')
print('')

'''
add:
name, text, 姓名
id, text, 身份证号
tel, text, 联系电话
address, text, 家庭住址
creditmanager, text, 贷款负责人
accountmanager, text, 银行账户负责人
contact_name, text, 联系人姓名
contact_tel, text, 联系人手机号
contact_email, text, 联系人email
contact_relation, text, 联系人与客户关系
'''

def printinfo_add(name,id,tel,address,contact_name,contact_tel,contact_email,contact_relation,creditmanager=None,accountmanager=None):
    print('<body align="center"><br><h1>已成功添加新的客户信息</h1>')
    print('<p>姓名: %s </p>' % name)
    print('<p>身份证号: %s </p>' % id)
    print('<p>联系电话: %s </p>' % tel)
    print('<p>家庭住址: %s </p>' % address)
    if(creditmanager):
        print('<p>贷款负责人: %s </p>' % creditmanager)
    if(accountmanager):
        print('<p>银行账户负责人: %s </p>' % accountmanager)
    print('<p>联系人信息: </p>' )
    print('<p>姓名: %s </p>' % contact_name)
    print('<p>手机号: %s </p>' % contact_tel)
    print('<p>email: %s </p>' % contact_email)
    print('<p>与客户关系: %s </p>' % contact_relation)
    print('</body>')
def printinfo_modify(name,id,tel,address,contact_name,contact_tel,contact_email,contact_relation,creditmanager=None,accountmanager=None):
    print('<body align="center"><br><h1>已成功修改客户信息，新的客户信息如下</h1>')
    print('<p>姓名: %s </p>' % name)
    print('<p>身份证号: %s </p>' % id)
    print('<p>联系电话: %s </p>' % tel)
    print('<p>家庭住址: %s </p>' % address)
    if(creditmanager):
        print('<p>贷款负责人: %s </p>' % creditmanager)
    if(accountmanager):
        print('<p>银行账户负责人: %s </p>' % accountmanager)
    print('<p>联系人信息: </p>' )
    print('<p>姓名: %s </p>' % contact_name)
    print('<p>手机号: %s </p>' % contact_tel)
    print('<p>email: %s </p>' % contact_email)
    print('<p>与客户关系: %s </p>' % contact_relation)
    print('</body>')
def printinfo_delete(id):
    print('<body align="center"><br><h1>已成功删除身份证号为')
    print(id)
    print('的客户信息</h1></body>')
def ret_btn():
    print('<body align="center"><form action="/cgi-bin/client.py" method="GET">')
    print('<button type="submit" style="font-size:15px;padding: .5em 2em .25em; color: #e8f0de;border: solid 1px #538312;background: #64991e; " >')
    print('返回客户管理</button></form></body>')


args = cgi.FieldStorage()
'''
   身份证号_客户              CHAR(256)             not null,
   身份证号_员工              CHAR(256),
   员工_身份证号_员工           CHAR(256),
   姓名_客户                CHAR(256)             not null,
   联系电话                 CHAR(256)             not null,
   家庭住址                 CHAR(256)             not null,
   联系人姓名                CHAR(256)             not null,
   联系人手机号               CHAR(256)             not null,
   "联系人email"           CHAR(256)             not null,
   联系人与客户的关系            CHAR(256)             not null,
'''
if(args.getvalue('add')):
    name = args.getvalue('name')
    id = args.getvalue('id')
    tel = args.getvalue('tel')
    address = args.getvalue('address')
    creditmanager = args.getvalue('creditmanager')
    accountmanager = args.getvalue('accountmanager')
    contact_name = args.getvalue('contact_name')
    contact_tel = args.getvalue('contact_tel')
    contact_email = args.getvalue('contact_email')
    contact_relation = args.getvalue('contact_relation')
    try:
        sql = "insert into 客户 (身份证号_客户, 身份证号_员工, 员工_身份证号_员工, 姓名_客户, 联系电话, 家庭住址, 联系人姓名, 联系人手机号, \"联系人email\",联系人与客户的关系) values("
        sql = sql + "'" +id + "',"
        if(creditmanager):
            sql = sql + "'"+creditmanager+"',"
        else:
            sql = sql + "null, "
        if(accountmanager):
            sql = sql + "'"+accountmanager+"',"
        else:
            sql = sql + "null, "
        sql = sql + "'"+name+"','"+tel+"','"+address+"','"+contact_name+"','"+contact_tel+"','"+contact_email+"','"+contact_relation+"')"
        print("<p>"+sql+"</p>")
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_add(name,id,tel,address,contact_name,contact_tel,contact_email,contact_relation,creditmanager,accountmanager)
        ret_btn()
    except:
        #print(Exception+': '+e)
        print('<p>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!</p>')
elif(args.getvalue('modify')):
    print('<body align="center"><br><h1>直接在下面进行修改</h1>')
    id = args.getvalue('m_id')
    db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
    cr = db.cursor()
    sql = 'select * from 客户 where 身份证号_客户 = \''+id +'\' '
    cr.execute(sql)
    rs = cr.fetchall()
    cr.close()
    db.close()
    for row in rs:
        print('<p>')
        print(row)
        print('</p>')
    creditmanager = ""
    if(row[1]):
        creditmanager = row[1]
    accountmanager = ""
    if(row[2]):
        accountmanager = row[2]
    print('<form action="/cgi-bin/client_handler.py" method="GET">')
    print('<p style="font-size:20px">姓名:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="name" value="'+row[3]+'"/></p>')
    print('<p style="font-size:20px">身份证号:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="id" value="'+row[0]+'"/></p>')
    print('<p style="font-size:20px">联系电话:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="tel" value="'+row[4]+'"/></p>')
    print('<p style="font-size:20px">家庭住址:&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="address" value="'+row[5]+'"/></p>')
    print('<p style="font-size:20px">贷款负责人:&nbsp&nbsp&nbsp&nbsp&nbsp<input type="text" name="creditmanager" value="'+creditmanager+'"/></p>')
    print('<p style="font-size:20px">银行账户负责人:&nbsp<input type="text" name="accountmanager" value="'+accountmanager+'"/></p>')
    print('<p style="font-size:20px">联系人姓名:&nbsp&nbsp<input type="text" name="contact_name" value="'+row[6]+'"/>')
    print('联系人手机号:&nbsp&nbsp<input type="text" name="contact_tel" value="'+row[7]+'"/></p>')
    print('<p style="font-size:20px">联系人email:&nbsp&nbsp<input type="text" name="contact_email" value="'+row[8]+'"/>')
    print('联系人与客户关系:&nbsp&nbsp<input type="text" name="contact_relation" value="'+row[9]+'"/></p>')
    print('<p style="font-size:20px"><input type="submit" value="提交" name="modify2"/></p></form><hr/>')
    print('</body>')
elif(args.getvalue('modify2')):
    # stage2 of mofify
    name = args.getvalue('name')
    id = args.getvalue('id')
    tel = args.getvalue('tel')
    address = args.getvalue('address')
    creditmanager = args.getvalue('creditmanager')
    accountmanager = args.getvalue('accountmanager')
    contact_name = args.getvalue('contact_name')
    contact_tel = args.getvalue('contact_tel')
    contact_email = args.getvalue('contact_email')
    contact_relation = args.getvalue('contact_relation')
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        if(creditmanager):
            sql = "Update 客户 set 身份证号_员工='"+creditmanager+"' where 身份证号_客户='"+id+"'"
            print("<p>"+sql+"</p>")
            cr.execute(sql)
        if(accountmanager):
            sql = "Update 客户 set 员工_身份证号_员工='"+accountmanager+"' where 身份证号_客户='"+id+"'"
            print("<p>"+sql+"</p>")
            cr.execute(sql)
        sql = "Update 客户 set 姓名_客户='"+name+"' where 身份证号_客户='"+id+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "Update 客户 set 联系电话='"+tel+"' where 身份证号_客户='"+id+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "Update 客户 set 家庭住址='"+address+"' where 身份证号_客户='"+id+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "Update 客户 set 联系人姓名='"+contact_name+"' where 身份证号_客户='"+id+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "Update 客户 set 联系人手机号='"+contact_tel+"' where 身份证号_客户='"+id+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "Update 客户 set \"联系人email\"='"+contact_email+"' where 身份证号_客户='"+id+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        sql = "Update 客户 set 联系人与客户的关系='"+contact_relation+"' where 身份证号_客户='"+id+"'"
        print("<p>"+sql+"</p>")
        cr.execute(sql)
        
        cr.close()
        db.commit()
        db.close()
        printinfo_modify(name,id,tel,address,contact_name,contact_tel,contact_email,contact_relation,creditmanager,accountmanager)
        ret_btn()
    except:
        print('<br><br>')
        traceback.print_exc()
        print('<br>ERROR! Please check again!')
elif(args.getvalue('delete')):
    id = args.getvalue('d_id')
    #branch = branch
    #开户_储蓄，开户_支票，借贷
    try:
        db = cx_Oracle.connect('C##WQ/123456@localhost:1521/orcl')
        cr = db.cursor()
        sql = "select * from 开户_储蓄 where 身份证号_客户='"+id+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("存在该客户的开户记录，无法删除")
            raise Exception
        sql = "select * from 开户_支票 where 身份证号_客户='"+id+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("存在该客户的开户记录，无法删除")
            raise Exception
        sql = "select * from 借贷 where 身份证号_客户='"+id+"'"
        cr.execute(sql)
        rs=cr.fetchall()
        if(rs!=[]):
            print("存在该客户的借贷记录，无法删除")
            raise Exception
        sql = "Delete From 客户 where 身份证号_客户='"+id+"'"
        print('<p>'+sql+'</p>')
        cr.execute(sql)
        cr.close()
        db.commit()
        db.close()
        printinfo_delete(id)
        ret_btn()
    except:
        print('<p>')
        traceback.print_exc()
        print('<br>错误！无法删除！</p>')

