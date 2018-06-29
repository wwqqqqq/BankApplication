#!C:\Users\weiq6\Anaconda3\python.exe
import cgi

print('Content-type: text/html')
print('')

print('<body style="background-color: rgb(244, 244, 244);">')
print('<br><h1 align="center" style="color:darkblue">银行业务管理系统</h1><br><br><br>')

# branch.py
print('<form method="get" action="/cgi-bin/branch.py" align="center">')
print('<button type="submit" style="font-size:25px;padding: .5em 2em .55em; color: #d9eef7;border: solid 1px #0076a3;background: #0095cd; " >')
print('支行管理</button></form><br><br>')

# staff.py
print('<form method="get" action="/cgi-bin/staff.py" align="center">')
print('<button type="submit" style="font-size:25px;padding: .5em 2em .55em; color: #fae7e9; border: solid 1px #b73948; background: #da5867; " >')
print('员工管理</button></form><br><br>')

# client.py
print('<form method="get" action="/cgi-bin/client.py" align="center">')
print('<button type="submit" style="font-size:25px;padding: .5em 2em .55em; color: #e8f0de; border: solid 1px #538312; background: #64991e; " >')
print('客户管理</button></form><br><br>')

# account.py
print('<form method="get" action="/cgi-bin/account.py" align="center">')
print('<button type="submit" style="font-size:25px;padding: .5em 2em .55em; color: #feeef5; border: solid 1px #d2729e; background: #f895c2; " >')
print('账户管理</button></form><br><br>')

# loan.py
print('<form method="get" action="/cgi-bin/loan.py" align="center">')
print('<button type="submit" style="font-size:25px;padding: .5em 2em .55em; color: #fef4e9; border: solid 1px #da7c0c; background: #f78d1d; " >')
print('贷款管理</button></form><br><br>')

# business.py
print('<form method="get" action="/cgi-bin/business.py" align="center">')
print('<button type="submit" style="font-size:25px;padding: .5em 2em .55em; color: #faddde; border: solid 1px #980c10; background: #d81b21; " >')
print('业务统计</button></form><br><br>')

print("</body>")
