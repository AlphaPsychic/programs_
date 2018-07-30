Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # error handling
>>> 
>>> try:
	whatColor = input('What color do you wish to know the date of?')
	coldex = colors.index(whatColor.lower())
	theDate = dates[coldex]
	print('The date of',whatColor,'is:',theDate)

    except Exception as e:
	    
SyntaxError: unindent does not match any outer indentation level
>>> 
