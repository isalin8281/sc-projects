"""
File: largest_digit.py
Name: Isabelle
----------------------------------
This file recursively prints the biggest digit in
5 different integers, 12345, 281, 6, -111, -9453
If your implementation is correct, you should see
5, 8, 6, 1, 9 on Console.
"""


def main():
	print(find_largest_digit(12345))      # 5
	print(find_largest_digit(281))        # 8
	print(find_largest_digit(6))          # 6
	print(find_largest_digit(-111))       # 1
	print(find_largest_digit(-9453))      # 9


def find_largest_digit(n):
	"""
	Set default value, turn negative into positive int, and find biggest digit in n
	:param n: int
	:return: biggest digit in n
	"""
	# Turn negative into positive int
	if n < 0:
		n = -1 * n
	# Use last digit of n as default value
	x = n % 10
	return find_largest_digit_helper(n, x)


def find_largest_digit_helper(n, x):
	"""
	Find biggest digit in n
	:param n: int
	:param x: a digit, last digit of n
	:return: biggest digit in n
	"""
	# When n is smaller than 1, stop comparing
	if n < 1:
		return x
	else:
		# take last digit of n
		digit = n % 10
		# take off last digit of n
		n = int(n / 10)
		# Compare each digit of n
		if digit > x:
			x = digit
		return find_largest_digit_helper(n, x)


if __name__ == '__main__':
	main()
