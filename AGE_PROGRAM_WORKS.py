Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def age_program():
	user_age = input("Enter your age: ")
	age_seconds = int(user_age) * 365 * 24 * 60 * 60
	print("Your age in seconds is {}".format(age_seconds))

	
>>> age_program()
Enter your age: 39
Your age in seconds is 1229904000
>>> 
