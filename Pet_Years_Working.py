Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> def program_thing():
	pet_age = input("Enter how long your pet has lived for: ")
	age_petyears = int(pet_age) * 7
	print("Your pets age in pet years is {}".format(age_petyears))

	
>>> age_program()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    age_program()
NameError: name 'age_program' is not defined
>>> program_thing()
Enter how long your pet has lived for: 2
Your pets age in pet years is 14
>>> program_thing()
Enter how long your pet has lived for: 8
Your pets age in pet years is 56
>>> 
