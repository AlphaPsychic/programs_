Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # strings as keys and values
>>> countries = {"NZ": "New Zealand",
	     "AUS": "Australia",
	     "US": "United States"}
>>> print(countries)
{'AUS': 'Australia', 'US': 'United States', 'NZ': 'New Zealand'}
>>> # a dictionary is an unordered collection of items. As a result, there is no guarantee that the items in a dictionary remain in the same order.
>>> codes = list(countries.keys())
>>> codes.sort()
>>> for code in codes:
	print(code + "      " + countries[code])

	
AUS      Australia
NZ      New Zealand
US      United States
>>> 
