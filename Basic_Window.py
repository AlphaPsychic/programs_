Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def simple(num1,num2):
	pass

>>> def simple(num1,num2=5):
	print(num1,num2)

	
>>> simple(2)
2 5
>>> def basic_window(width,height,font='TNR',)
SyntaxError: invalid syntax
>>> def basic_window(width,height,font='TNR',
		 bgc='w',scrollbar=True):
	print(width,height,font,bgc)

	
>>> basic_window(500,350)
500 350 TNR w
>>> # we did the 500,350 because we originally did not specify the value of width and height but we did with font,bgc,scrollbar
>>> basic_window(500,350,'a')
500 350 a w
>>> basic_window(500,350,bgc='w')
500 350 TNR w
>>> basic_window(500,350,bgc='b')
500 350 TNR b
>>> # w and b are white and black, bgc is background colour
>>> 
