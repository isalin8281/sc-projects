"""
File: rocket.py
Name: Isabelle
-----------------------
This program should implement a console program
that draws ASCII art - a rocket.
The size of rocket is determined by a constant
defined as SIZE at top of the file.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This number controls the size of rocket.
SIZE = 5



def main():
	"""
	This program print the different size of rocket.
	"""
	head()
	belt()
	upper()
	lower()
	belt()
	head()

def head():
	"""
	Print the head of rocket.
	"""
	for i in range(SIZE):
		for j in range(SIZE-i):
			print(' ',end='')
		for j in range(i+1):
			print('/',end='')
		for j in range(i+1):
			print('\\',end='')
		print('')

def belt():
	"""
	The connection between the head and the body of rocket.
	"""
	print('+', end='')
	for i in range(1):
		for j in range(SIZE):
			print('==', end='')
	print('+')

def upper():
	"""
	The upper body of rocket.
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(SIZE-i-1):
			print('.',end='')
		for j in range(i+1):
			print('/\\',end='')
		for j in range(SIZE-i-1):
			print('.',end='')
		print('|')

def lower():
	"""
	The lower body of rocket.
	"""
	for i in range(SIZE):
		print('|', end='')
		for j in range(i):
			print('.',end='')
		for j in range(SIZE-i):
			print('\\/',end='')
		for j in range(i):
			print('.',end='')
		print('|')




###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()