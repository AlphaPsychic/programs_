Python 3.5.3 (default, Jan 19 2017, 14:11:04) 
[GCC 6.3.0 20170124] on linux
Type "copyright", "credits" or "license()" for more information.
>>> # reading from a CSV spreadsheet
>>> import csv
>>> # csv stands for 'comma separated variables'
>>> with open('example.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		print(row)

		
['balls']
>>> # we printed what teh text was in the example.csv file!
>>> 
>>> 
>>> with open('example.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		print(row)
		print(row[0])
		print(row[0],row[1])

		
['balls']
balls
Traceback (most recent call last):
  File "<pyshell#17>", line 6, in <module>
    print(row[0],row[1])
IndexError: list index out of range
>>> # I did not have enough text to do that, but it basically just makes things more tidy.
>>> #--- random stuff from here ---
>>> 
>>> with open('example.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	dates = []
	colors = []
	for row in readCSV:
		color = row[3]
		date = row[0]
		dates.append(date)
		colors.append(color)

		
Traceback (most recent call last):
  File "<pyshell#30>", line 6, in <module>
    color = row[3]
IndexError: list index out of range
>>> print(dates)
[]
>>> # at the end of the last long script we should put print(dates)
>>> # and print(colors)
>>> # after that it will just show all of the dates and colors
>>> # need to finish this make a part 2 later :/
>>> 
