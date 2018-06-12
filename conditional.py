#!/bin/usr/python
x=10
if 10>x:
	print("x is above 10")
elif 20>x:
	print("x id above 20")



print('aa'>'ab')
print('ab'>'aa')


x=12
if x>=12 or x<12:
	print("all condition are gd")



while True:
	answer=raw_input("what is your answer:")
	if answer=='x':
		break
	
#function


def count(n1=1,n2=10):
	for i in range(n1,n2+1):
		print(i)





count(1,30)
count()




def ret(a):

	return a +"please"


print(ret("dheere dheere"))
