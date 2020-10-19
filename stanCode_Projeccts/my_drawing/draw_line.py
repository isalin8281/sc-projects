"""
File: draw_line.py
Name: Isabelle
-------------------------
The file shows how to create a line by mouse clicking
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

window = GWindow()
# size of circle on an instance of GWindow class
SIZE = 10
# x stands for the number of click
x = 0
# record the position of first click
circle = None


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(first_point)


def first_point(mouse):
    global x, circle
    oval = set_up_oval()
    window.add(oval, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
    x += 1
    # circle appears at first click
    if x == 1:
        # circle is the position of first click
        circle = oval
    elif x == 2:
        # line created at second click, started from position of first click  to second click
        line = GLine(mouse.x, mouse.y, circle.x+SIZE/2, circle.y+SIZE/2)
        window.add(line)
        window.remove(oval)
        # circle disappears as line is created
        window.remove(circle)
        # after second click, x returns to 0
        x = 0


def set_up_oval():
    oval = GOval(SIZE, SIZE)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'black'
    return oval


if __name__ == "__main__":
    main()
