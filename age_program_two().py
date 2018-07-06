Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def ask_age():
	age = input("Enter your age: ")
	return int(age)

>>> def calculate_seconds_from_years(age_years):
	return age_years * 365 * 24 * 3600

>>> def prompt_user_and_calculate_age():
	age = ask_age()
	seconds_lived = calculate_seconds_from_years(age)
	print("You have lived for {} seconds".format(seconds_lived))

	
>>> prompt_user_and_calculate_age():
	
SyntaxError: invalid syntax
>>> prompt_user_and_calculate_age()
Enter your age: 14
You have lived for 441504000 seconds
>>> 
