Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def age_program():
	seconds_or_years = input("Give me seconds (s) or years (y)?")
	if seconds_or_years == "s":
		# Covert seconds to years
		user_value = input("Enter the number of seconds you've lived for: ")
		print("You've lived for {} years ".format(int(user_value)/60/60/24/365)
		      elif seconds_or_years == "y":
		      
SyntaxError: invalid syntax
>>> if seconds_or_years == "y":
		      # Convert years to seconds
		      user_value = input("Enter the number of years you've lived for: ")
		      print("You've lived for {} seconds ".format(int(user_value)*365*24*60*60)



age_program()
			    
SyntaxError: invalid syntax
>>> seconds_or_years
			    
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    seconds_or_years
NameError: name 'seconds_or_years' is not defined
>>> 
