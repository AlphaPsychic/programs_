Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # FAQ
>>> # !/usr/bin/python
>>> # this is a shabang line and it notifies Linux of the path to python so you can run your script as an executable
>>> def epic():
	print('wow this is great!')

	
>>> if __name__ == '__main__':
	print('very great module!')

	
very great module!
>>> # people use if __name__ == __main__ so that people can use the code as an example
>>> # if you want to import an executable you use import epicthing (epicthing is an example)
>>> # then after you use import epicthing then go to next line and do epicthing.epic()
>>> # and then it should print whatever was in the executable
>>> # we just treated epicthing as a module
>>> 
