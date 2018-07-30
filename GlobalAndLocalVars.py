Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # global and local variables
>>> x = 6
>>> #that is a local variable
>>> def example():
	z = 5
	print(z)

	
>>> example():
	
SyntaxError: invalid syntax
>>> example()
5
>>> def example():
	print(x)

	
>>> example()
6
>>> def example():
	print(x)
	print(x+5)

	
>>> example()
6
11
>>> def example():
	print(x)
	print(x+5)
	x+=6

	
>>> example()
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    example()
  File "<pyshell#22>", line 2, in example
    print(x)
UnboundLocalError: local variable 'x' referenced before assignment
>>> # the reason that did not ork is because x is not a global variable
>>> # too fix:
>>> 
>>> def example():
	global x
	print(x)
	x+=5
	print(x)

	
>>> example()
6
11
>>> # x+=5 is basically just x+
>>> def example():
	globx = x
	print(globx)
	globx+=5
	print(globx)

	
>>> example()
11
16
>>> # that is a way around having to make x global
>>> # you cannot access globx outside of the function
>>> def example():
	globx = x
	print(globx)
	globx+=5
	print(globx)

	
>>> def example():
	globx = x
	print(globx)
	globx+=5
	print(globx)
	return globx

>>> x = example()
11
16
>>> print(x)
16
>>> x
16
>>> 
