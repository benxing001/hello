#!/usr/bin/env python3
# -*- coding:utf-8 -*-
classmate = ['adam','limei','hanmei']
age = 8
if age > 6:
	print('your age is',age)
	print('tennager')
elif age > 18:
	print ('adult')
else:
	print('your age is', age)
	print('kid')

if 0:
	print('true')

'''
input('birth:')	
birth = int
if birth > 2000:
	print('after 2000')
else:
	print ('before 2000')
'''
'''	
height = input('height:')
weight = input('weight:')
BMI = float(weight/height**2)
if BMI < 18.5:
	print(u'您的体重指数为：%.2f，体重过轻'% (BMI))
elif BMI < 25:
	print(u'正常')
elif BMI < 28:
	print (u'偏胖')
elif BMI < 32:
	print(u'肥胖')
else:
	PRINT (u'过度肥胖')
'''


#练习循环
sum = 0
for x in range(101):
	sum = sum + x
print (sum)
a = 101
x = 1
sum = 0
while x < a:
	sum = sum + x
	x = x + 1
print(sum)

L = ['lisa','lilei','hanmei','wang']
for ls in L:
	print('hello,',ls,'!') 

#break语句
n=0
while n < 101:
	if n > 10:
		break
	print (n)
	n = n + 1
print('END')

nn = 0
while nn < 10:
	nn = nn + 1
	if nn % 2 == 0:
		continue
	print(nn)
	#nn = nn + 1
print('END')










