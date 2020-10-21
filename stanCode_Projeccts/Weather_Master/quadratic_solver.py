"""
File: quadratic_solver.py
-----------------------
This program should implement a console program
that asks 3 inputs (a, b, and c)
from users to compute the roots of equation
ax^2 + bx + c = 0
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

import math


def main():
	"""
	Calculate the number of roots and the root(s).
	"""
	print("stanCode Quadratic Solver!")
	a=int(input('Enter a:'))
	b=int(input('Enter b:'))
	c=int(input('Enter c:'))
	discriminant=int(b*b-4*a*c)

	if discriminant<0:
		print('No real roots')

	elif discriminant>0:
		y = math.sqrt(discriminant)
		x1 = float((-b + y) / (2 * a))
		x2 = float((-b - y) / (2 * a))
		print('Two roots: '+str(x1)+', '+str(x2))

	else:
	#discriminant==0
		y = math.sqrt(discriminant)
		x1 = float((-b + y) / (2 * a))
		print('One root: '+str(x1))







###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
