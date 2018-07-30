Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def simple_addition(num1,num2):
	answer = num1 + num2
	print('num1 is',num1)
	print(answer)

	
>>> simple_addition(5,3)
num1 is 5
8
>>> # look out for order and quantity of variables
>>> # 5 + 3 = 8 so it printed it
>>> simple_addition(num1=5,num2=3)
num1 is 5
8
>>> # if you want to add another number to the equation you can do num3
>>> 
