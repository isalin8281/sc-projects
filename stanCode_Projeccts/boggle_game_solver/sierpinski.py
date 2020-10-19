"""
File: sierpinski.py
Name: Isabelle
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 8                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	Draw sierpinski Triangle
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	Draw 「Sierpinski Triangle」
	:param order: int, controls the order of Sierpinski Triangle
	:param length: int, the length of order 1 Sierpinski Triangle
	:param upper_left_x: int, the upper left x coordinate of order 1 Sierpinski Triangle
	:param upper_left_y: int, the upper left y coordinate of order 1 Sierpinski Triangle
	"""
	if order == 0:
		return
	else:
		triangle(length, upper_left_x, upper_left_y)
		# upper left triangle
		sierpinski_triangle(order-1, length/2, upper_left_x, upper_left_y)
		# upper right triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+length/2, upper_left_y)
		# lower triangle
		sierpinski_triangle(order-1, length/2, upper_left_x+(length/4), \
			upper_left_y+(length*0.5*0.866))


def triangle(length, x, y):
	"""
	Draw triangle on each order
	:param length: int, the length of triangle
	:param x: the upper left x coordinate of triangle
	:param y: the upper left y coordinate of triangle
	"""
	# left line of triangle
	line_1 = GLine(x, y, x+length, y)
	window.add(line_1)
	# right line of triangle
	line_2 = GLine(x, y, x+(length/2), y+(length*0.866))
	window.add(line_2)
	# upper line of triangle
	line_3 = GLine(x+length, y, x+(length/2), y+(length*0.866))
	window.add(line_3)


if __name__ == '__main__':
	main()