# -*- coding: utf-8 -*-
import datetime

def daterange(d1, d2):
	return (d1 + datetime.timedelta(days=i) for i in range((d2 - d1).days + 1))

def run():
	print("\n1. for with integer range(6)\n")
	for a in range(6):
		print(str(a))
	print("\n2. for with integer range(4,9)\n")
	for b in range(4,9):
		print(str(b))
	print("\n3. for with string list\n")
	fruits = ["maracuya (passion fruit)", "gulupa", "uchuva (golden berry)", "zapote (sapota)", "pitaya (dragon fruit)", "mangostino (mangosteen)", "borojó", "curuba (banana passion fruit)", "lulo", "níspero", "guanábana"]
	print("Colombian fruits:")
	for fruit in fruits:
		print(fruit)
	print("\n4. Looping through a string:\n")
	for char in "greetings":
		print(char)
	print("\n5. for with dates (timedelta):")
	date1 = datetime.date(2020,3,5)
	date2 = datetime.date(2020,3,15)
	print(str(date1) + " to " + str(date2) + "\n")
	for d in daterange(date1, date2):
		print(d.strftime('%Y-%m-%d'))

if __name__ == '__main__':
    run()