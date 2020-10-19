"""
File: my_drawing.py
Name: Isabelle
----------------------
The file shows the picture
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    Try to find easy stuff to draw...
    """
    window = GWindow(width=320, height=500, title='my_drawing')
    rect = set_up_rect()
    window.add(rect)
    oval_a = set_up_oval_a()
    window.add(oval_a)
    oval_b = set_up_oval_b()
    window.add(oval_b)
    oval_c = set_up_oval_c()
    window.add(oval_c)
    oval_d = set_up_oval_d()
    window.add(oval_d)
    oval_e = set_up_oval_e()
    window.add(oval_e)
    oval_f = set_up_oval_f()
    window.add(oval_f)
    oval_g = set_up_oval_g()
    window.add(oval_g)
    oval_h = set_up_oval_h()
    window.add(oval_h)
    oval_i = set_up_oval_i()
    window.add(oval_i)
    oval_j = set_up_oval_j()
    window.add(oval_j)
    oval_k = set_up_oval_k()
    window.add(oval_k)
    label_one = set_up_label_one()
    window.add(label_one)
    oval_one = set_up_oval_one()
    window.add(oval_one)
    oval_two = set_up_oval_two()
    window.add(oval_two)
    oval_three = set_up_oval_three()
    window.add(oval_three)
    oval_four = set_up_oval_four()
    window.add(oval_four)
    oval_five = set_up_oval_five()
    window.add(oval_five)
    oval_six = set_up_oval_six()
    window.add(oval_six)
    oval_seven = set_up_oval_seven()
    window.add(oval_seven)
    oval_eight = set_up_oval_eight()
    window.add(oval_eight)
    rect_two = set_up_rect_two()
    window.add(rect_two)
    rect_three = set_up_rect_three()
    window.add(rect_three)
    oval_nine = set_up_oval_nine()
    window.add(oval_nine)
    oval_ten = set_up_oval_ten()
    window.add(oval_ten)
    oval_eleven = set_up_oval_eleven()
    window.add(oval_eleven)
    oval_twelve = set_up_oval_twelve()
    window.add(oval_twelve)
    oval_thirteen = set_up_oval_thirteen()
    window.add(oval_thirteen)
    oval_fourteen = set_up_oval_fourteen()
    window.add(oval_fourteen)
    oval_fifteen = set_up_oval_fifteen()
    window.add(oval_fifteen)
    oval_sixteen = set_up_oval_sixteen()
    window.add(oval_sixteen)
    oval_seventeen = set_up_oval_seventeen()
    window.add(oval_seventeen)
    oval_eighteen = set_up_oval_eighteen()
    window.add(oval_eighteen)
    oval_nineteen = set_up_oval_nineteen()
    window.add(oval_nineteen)
    oval_twenty = set_up_oval_twenty()
    window.add(oval_twenty)
    oval_twentyone = set_up_oval_twentyone()
    window.add(oval_twentyone)
    oval_twentytwo = set_up_oval_twentytwo()
    window.add(oval_twentytwo)
    rect_four = set_up_rect_four()
    window.add(rect_four)
    oval_twentythree = set_up_oval_twentythree()
    window.add(oval_twentythree)
    oval_twentyfour = set_up_oval_twentyfour()
    window.add(oval_twentyfour)
    oval_twentyfive = set_up_oval_twentyfive()
    window.add(oval_twentyfive)
    oval_twentysix = set_up_oval_twentysix()
    window.add(oval_twentysix)
    oval_twentyseven = set_up_oval_twentyseven()
    window.add(oval_twentyseven)
    oval_twentyeight = set_up_oval_twentyeight()
    window.add(oval_twentyeight)
    rect_five = set_up_rect_five()
    window.add(rect_five)
    rect_six = set_up_rect_six()
    window.add(rect_six)
    rect_seven = set_up_rect_seven()
    window.add(rect_seven)
    rect_eight = set_up_rect_eight()
    window.add(rect_eight)
    label_two = set_up_label_two()
    window.add(label_two)
    label_three = set_up_label_three()
    window.add(label_three)
    label_four = set_up_label_four()
    window.add(label_four)
    label_five = set_up_label_five()
    window.add(label_five)
    label_six = set_up_label_six()
    window.add(label_six)
    label_seven = set_up_label_seven()
    window.add(label_seven)
    label_eight = set_up_label_eight()
    window.add(label_eight)
    label_nine = set_up_label_nine()
    window.add(label_nine)
    label_ten = set_up_label_ten()
    window.add(label_ten)
    label_eleven = set_up_label_eleven()
    window.add(label_eleven)
    label_twelve = set_up_label_twelve()
    window.add(label_twelve)
    rect_nine = set_up_rect_nine()
    window.add(rect_nine)
    rect_ten = set_up_rect_ten()
    window.add(rect_ten)
    label_thirteen = set_up_label_thirteen()
    window.add(label_thirteen)
    rect_11 = set_up_rect_11()
    window.add(rect_11)
    rect_12 = set_up_rect_12()
    window.add(rect_12)
    rect_13 = set_up_rect_13()
    window.add(rect_13)
    rect_14 = set_up_rect_14()
    window.add(rect_14)
    rect_15 = set_up_rect_15()
    window.add(rect_15)



def set_up_rect():
    rect = GRect(320, 600, x=0, y=0)
    rect.filled = True
    rect.fill_color = 'skyblue'
    rect.color = 'skyblue'
    return rect


def set_up_oval_a():
    oval = GOval(30, 30, x=110, y=25)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_b():
    oval = GOval(30, 30, x=185, y=25)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_c():
    oval = GOval(15, 15, x=117, y=42)
    oval.filled = True
    return oval


def set_up_oval_d():
    oval = GOval(15, 15, x=192, y=42)
    oval.filled = True
    return oval


def set_up_oval_e():
    oval = GOval(40, 40, x=-20, y=80)
    oval.filled = True
    oval.fill_color = 'mediumpurple'
    oval.color = 'mediumpurple'
    return oval


def set_up_oval_f():
    oval = GOval(40, 35, x=100, y=200)
    oval.filled = True
    oval.fill_color = 'mediumpurple'
    oval.color = 'mediumpurple'
    return oval


def set_up_oval_g():
    oval = GOval(40, 35, x=10, y=350)
    oval.filled = True
    oval.fill_color = 'mediumpurple'
    oval.color = 'mediumpurple'
    return oval


def set_up_oval_h():
    oval = GOval(35, 30, x=300, y=400)
    oval.filled = True
    oval.fill_color = 'mediumpurple'
    oval.color = 'mediumpurple'
    return oval


def set_up_oval_i():
    oval = GOval(45, 45, x=260, y=280)
    oval.filled = True
    oval.fill_color = 'mediumpurple'
    oval.color = 'mediumpurple'
    return oval


def set_up_oval_j():
    oval = GOval(38, 50, x=295, y=10)
    oval.filled = True
    oval.fill_color = 'mediumpurple'
    oval.color = 'mediumpurple'
    return oval


def set_up_oval_k():
    oval = GOval(30, 30, x=120, y=470)
    oval.filled = True
    oval.fill_color = 'mediumpurple'
    oval.color = 'mediumpurple'
    return oval


def set_up_label_one():
    label = GLabel('Enter Passcode', x=60, y=105)
    label.font = '-30'
    label.color = 'dodgerblue'
    return label


def set_up_oval_one():
    oval = GOval(55, 55, x=35, y=115)
    oval.filled = True
    oval.fill_color = 'yellowgreen'
    oval.color = 'yellowgreen'
    return oval


def set_up_oval_two():
    oval = GOval(55, 55, x=100, y=115)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_three():
    oval = GOval(55, 55, x=165, y=115)
    oval.filled = True
    oval.fill_color = 'sage'
    oval.color = 'sage'
    return oval


def set_up_oval_four():
    oval = GOval(55, 55, x=230, y=115)
    oval.filled = True
    oval.fill_color = 'gold'
    oval.color = 'gold'
    return oval


def set_up_oval_five():
    oval = GOval(26, 26, x=50, y=120)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_six():
    oval = GOval(17, 17, x=55, y=125)
    oval.filled = True
    oval.fill_color = 'black'
    oval.color = 'black'
    return oval


def set_up_oval_seven():
    oval = GOval(5, 5, x=63, y=126)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_eight():
    oval = GOval(13, 8, x=55, y=153)
    oval.filled = True
    oval.fill_color = 'black'
    oval.color = 'black'
    return oval


def set_up_oval_nine():
    oval = GOval(14, 14, x=113, y=120)
    oval.filled = True
    oval.fill_color = 'lavender'
    oval.color = 'lavender'
    return oval


def set_up_oval_ten():
    oval = GOval(14, 14, x=133, y=123)
    oval.filled = True
    oval.fill_color = 'lavender'
    oval.color = 'lavender'
    return oval


def set_up_oval_eleven():
    oval = GOval(9, 9, x=115, y=122)
    oval.filled = True
    return oval


def set_up_oval_twelve():
    oval = GOval(9, 9, x=135, y=126)
    oval.filled = True
    return oval


def set_up_oval_thirteen():
    oval = GOval(4, 4, x=118, y=122)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_fourteen():
    oval = GOval(4, 4, x=137, y=127)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_rect_two():
    rect = GRect(5, 13, x=118, y=134)
    rect.filled = True
    rect.fill_color = 'plum'
    rect.color = 'plum'
    return rect


def set_up_rect_three():
    rect = GRect(5, 13, x=136, y=137)
    rect.filled = True
    rect.fill_color = 'plum'
    rect.color = 'plum'
    return rect


def set_up_oval_fifteen():
    oval = GOval(38, 25, x=108, y=140)
    oval.filled = True
    oval.fill_color = 'lavender'
    oval.color = 'lavender'
    return oval


def set_up_oval_sixteen():
    oval = GOval(33, 21, x=110, y=146)
    oval.filled = True
    oval.fill_color = 'plum'
    oval.color = 'plum'
    return oval


def set_up_oval_seventeen():
    oval = GOval(10, 10, x=185, y=123)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_eighteen():
    oval = GOval(6, 6, x=185, y=128)
    oval.filled = True
    return oval


def set_up_oval_nineteen():
    oval = GOval(10, 10, x=178, y=137)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_twenty():
    oval = GOval(6, 6, x=182, y=140)
    oval.filled = True
    return oval


def set_up_oval_twentyone():
    oval = GOval(10, 10, x=193, y=137)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_twentytwo():
    oval = GOval(6, 6, x=192, y=138)
    oval.filled = True
    return oval


def set_up_rect_four():
    rect = GRect(20, 1.5, x=182, y=155)
    rect.filled = True
    rect.fill_color = 'gray'
    rect.color = 'gray'
    return rect


def set_up_oval_twentythree():
    oval = GOval(20, 11, x=117, y=151)
    oval.filled = True
    oval.fill_color = 'darkgrey'
    oval.color = 'darkgrey'
    return oval


def set_up_oval_twentyfour():
    oval = GOval(11, 11, x=252, y=128)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_twentyfive():
    oval = GOval(11, 11, x=246, y=127)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_twentysix():
    oval = GOval(11, 11, x=259, y=127)
    oval.filled = True
    oval.fill_color = 'white'
    oval.color = 'white'
    return oval


def set_up_oval_twentyseven():
    oval = GOval(10, 10, x=253, y=128)
    oval.filled = True
    oval.fill_color = 'green'
    oval.color = 'green'
    return oval


def set_up_oval_twentyeight():
    oval = GOval(5, 5, x=255, y=130)
    oval.filled = True
    oval.fill_color = 'black'
    oval.color = 'black'
    return oval


def set_up_rect_five():
    rect = GRect(27, 1, x=245, y=150)
    rect.filled = True
    rect.fill_color = 'darkgrey'
    rect.color = 'darkgrey'
    return rect


def set_up_rect_six():
    rect = GRect(3, 3, x=250, y=152)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    return rect


def set_up_rect_seven():
    rect = GRect(5, 5, x=263, y=152)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    return rect


def set_up_rect_eight():
    rect = GRect(4, 4, x=256, y=152)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    return rect


def set_up_label_two():
    label = GLabel('1', x=50, y=248)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_three():
    label = GLabel('2', x=147, y=248)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_four():
    label = GLabel('3', x=243, y=248)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_five():
    label = GLabel('4', x=50, y=328)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_six():
    label = GLabel('5', x=147, y=328)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_seven():
    label = GLabel('6', x=243, y=328)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_eight():
    label = GLabel('7', x=50, y=408)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_nine():
    label = GLabel('8', x=147, y=408)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_ten():
    label = GLabel('9', x=243, y=408)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_eleven():
    label = GLabel('0', x=147, y=488)
    label.font = '-40'
    label.color = 'white'
    return label


def set_up_label_twelve():
    label = GLabel('stanCode', x=3, y=15)
    label.font = '-15'
    label.color = 'black'
    return label


def set_up_rect_nine():
    rect = GRect(17, 11, x=300, y=1)
    rect.color = 'black'
    return rect


def set_up_rect_ten():
    rect = GRect(6, 9, x=302, y=2)
    rect.filled = True
    rect.fill_color = 'yellow'
    rect.color = 'yellow'
    return rect


def set_up_label_thirteen():
    label = GLabel('5G', x=280, y=15)
    label.font = '-13'
    label.color = 'black'
    return label


def set_up_rect_11():
    rect = GRect(2, 9, x=275, y=1)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    return rect


def set_up_rect_12():
    rect = GRect(2, 7, x=271, y=3)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    return rect


def set_up_rect_13():
    rect = GRect(2, 5, x=267, y=5)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    return rect


def set_up_rect_14():
    rect = GRect(2, 3, x=263, y=7)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    return rect


def set_up_rect_15():
    rect = GRect(2, 1, x=259, y=9)
    rect.filled = True
    rect.fill_color = 'white'
    rect.color = 'white'
    return rect


if __name__ == '__main__':
    main()
