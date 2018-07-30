Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> x = 5
>>> y = 8
>>> if x < y:
	print('x is less than y')

	
x is less than y
>>> z = 5
>>> if z < y > x:
	print('y is greater than x and greater than x')

	
y is greater than x and greater than x
>>> if z <= x:
	print('z is less than or equal to x')

	
z is less than or equal to x
>>> if z == x:
	# if z = x: it will not work because you are basically asking if x is stored in the z variable, and it is not. So we use if z == x:
	print('z is equal to x')

	
z is equal to x
>>> # z is equal to x, so it prints the statement.
>>> 
