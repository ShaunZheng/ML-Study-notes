# -*-coding:utf-8-*-
import re 

test = '101-12345'
if re.match(r'^\d{3}\-\d{3,8}', test):
    print('ok')
else:
    print('failed')

t = '9:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print m.group(0),m.group(1),m.group(2),m.group(3)

# 请尝试写一个验证Email地址的正则表达式。版本一应该可以验证出类似的Email：
# someone@gmail.com
# bill.gates@microsoft.com

# 版本二可以提取出带名字的Email地址：
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob
def is_email(addr):
    if re.match(r'[a-zA-Z.]*@\w*.\w{6}',addr):
    	print 'true'
    else:
    	print 'flase'

def is_email2(addr):
	m = re.match(r'(<?)([\w\s.]*)(>?)([\w.\s]*)@(\w*.)',addr)
	if m:
		print m.group(2)
	else:
		print error

is_email('bill.gates@microsoft.coma')
is_email2('<shaun zheng> tom.zz@voyager.org')