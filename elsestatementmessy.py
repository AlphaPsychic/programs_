Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> y = 8
>>> 
>>> if x > y:
	print('x is greater than y')
else:
	print('x is not greater than y')

	
x is not greater than y
>>> if x < y:
	print('x is greater than y')

if x > 55:
	print('x is greater than 55')
else:
	print('x is not greater than y')
	
SyntaxError: invalid syntax
>>> # else onlz applys to most recent if
>>> # else happens when outcoem is different to if
>>> #e.g
>>> x = 5
>>> y = 8
>>> if x > y:
	print('x is greater than y')
else:
	print('x is not greater than y')

	
x is not greater than y
>>> 
