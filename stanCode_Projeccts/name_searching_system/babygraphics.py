"""
File: babygraphics.py
Name: Isabelle
----------------------------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.

This file creates canvas, and shows the change of rank of name in different years
"""

import tkinter 
import babynames
import babygraphicsgui as gui


FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                              with the specified year.
    """
    # divide canvas equally
    width_of_yr = (width - GRAPH_MARGIN_SIZE) / len(YEARS)
    # x coordinate changed with year_index
    x = int(width_of_yr * year_index + GRAPH_MARGIN_SIZE)
    return x


def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.

    Returns:
        This function does not return any value.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # Write your code below this line
    #################################
    # create horizontal line on top of canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE, \
        (CANVAS_WIDTH - GRAPH_MARGIN_SIZE), GRAPH_MARGIN_SIZE, \
        width=LINE_WIDTH)
    # create horizontal line on bottom of canvas
    canvas.create_line(GRAPH_MARGIN_SIZE, \
        (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), (CANVAS_WIDTH - GRAPH_MARGIN_SIZE), \
        (CANVAS_HEIGHT - GRAPH_MARGIN_SIZE), width=LINE_WIDTH)
    # create vertical line and add year on canvas
    for i in range(len(YEARS)):
        # get x coordinate of line and text
        x = get_x_coordinate(CANVAS_WIDTH, i)
        # vertical line
        canvas.create_line(x, 0, x, CANVAS_HEIGHT, width=LINE_WIDTH)
        # year
        canvas.create_text((x + TEXT_DX), CANVAS_HEIGHT, text=YEARS[i], \
            anchor=tkinter.SW)


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # Write your code below this line
    ################################
    # create line and text (name + rank) on canvas
    # the number of c controls change of color
    c = 0
    # run each name in lookup_names list
    for i in range(len(lookup_names)):
        # run each year in YEARS list
        for j in range(len(YEARS)-1):
            # x coordinate
            x1 = get_x_coordinate(CANVAS_WIDTH, j)
            # x coordinate
            x2 = get_x_coordinate(CANVAS_WIDTH, (j+1))
            # get y coordinate, and add name and rank on canvas
            y1 = get_y_canvas(canvas, CANVAS_HEIGHT, name_data, lookup_names, i, j, x1, c)
            # see if j on last ele
            if j == (len(YEARS) - 2):
                # OBOB, add name and rank on canvas
                y2 = get_y_canvas(canvas, CANVAS_HEIGHT, name_data, lookup_names, i, (j+1), x2, c)
            else:
                # get y coordinate
                y2 = get_y(CANVAS_HEIGHT, name_data, lookup_names, i, (j+1))
            # create line from (x1, y1) to (x2, y2)
            canvas.create_line(x1, y1, x2, y2, width=LINE_WIDTH, fill=COLORS[c])
        # changes c to change color of line
        if c != (len(COLORS)-1):
            c += 1
        # on last ele of COLORS list, return c to 0
        else:
            c = 0
    

def get_y_canvas(canvas, height, name_data, lookup_names, i, j, x, c):
    """
    get y coordinate, and put name and rank on canvas
    : param canvas: (Tkinter Canvas) The canvas on which we are drawing.
    : param height: CANVANS_HEIGHT
    : param name_data: (dict) Dictionary holding baby name data
    : param lookup_names: (List[str]) A list of names whose data you want to plot
    : param i: int, stands for item in lookup_names(list)
    : param j: int, stands for item in YEARS(list)
    : param c: int, stands for item in COLORS(list
    : return y: integer, y coordinate
    """
    # divide canvas height equally
    height_of_1000 = (height - GRAPH_MARGIN_SIZE * 2) / 1000
    # turn into string
    year = str(YEARS[j])
    # check if the year exists in name_dara[name] dict
    if year in name_data[lookup_names[i]]:
        # y coordinate
        y = GRAPH_MARGIN_SIZE + (height_of_1000 * int(name_data[lookup_names[i]][year]))
        # text
        canvas.create_text((x + TEXT_DX), y, \
                           text=lookup_names[i] + ' ' + name_data[lookup_names[i]][year], \
                           fill=COLORS[c], anchor=tkinter.SW)
    else:
        # y coordinate
        y = GRAPH_MARGIN_SIZE + (height_of_1000 * 1000)
        # text
        canvas.create_text((x + TEXT_DX), y, \
                           text=lookup_names[i] + ' *', fill=COLORS[c], anchor=tkinter.SW)
    return y


def get_y(height, name_data, lookup_names, i, j):
    """
    get y coordinate
    : param height: CANVANS_HEIGHT
    : param name_data: (dict) Dictionary holding baby name data
    : param lookup_names: (List[str]) A list of names whose data you want to plot
    : param i: int, stands for item in lookup_names(list)
    : param j: int, stands for item in YEARS(list)
    : return y: integer, y coordinate
    """
    # divide canvas height equally
    height_of_1000 = (height - GRAPH_MARGIN_SIZE * 2) / 1000
    # turn into string
    year = str(YEARS[j])
    # check if the year exists in name_dara[name] dict
    if year in name_data[lookup_names[i]]:
        # y coordinate
        y = GRAPH_MARGIN_SIZE + (height_of_1000 * int(name_data[lookup_names[i]][year]))
    else:
        # y coordinate
        y = GRAPH_MARGIN_SIZE + (height_of_1000 * 1000)
    return y


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
