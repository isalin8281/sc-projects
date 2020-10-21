"""
File: best_photoshop_award.py
Name: Isabelle
----------------------------------
This file creates a photoshopped image
that is going to compete for the 2020 Best
Photoshop Award for SC101P.
Please put all the images you use in image_contest folder
and make sure to choose which award you are aiming at
"""
from simpleimage import SimpleImage

# Control the threshold of detecting green screen pixel
THRESHOLD = 1.1

# Control the upper bound for the black pixel
BLACK = 180


def combine(fg, bg):
    for y in range(fg.height):
        for x in range(fg.width):
            fg_pixel = fg.get_pixel(x, y)
            bg_pixel = bg.get_pixel(x, y)
            avg = (fg_pixel.red + fg_pixel.green + fg_pixel.blue) / 3
            total = fg_pixel.red + fg_pixel.green + fg_pixel.blue
            if fg_pixel.green > avg*THRESHOLD and total > BLACK:
                # Replace green pixel in Isabelle.jpg
                fg_pixel.red = bg_pixel.red
                fg_pixel.green = bg_pixel.green
                fg_pixel.blue = bg_pixel.blue
    return fg


def main():
    """
    Just want to tell everyone I have these two lovely dogs
    And I love Christmas!
    """
    fg = SimpleImage("images/Isabelle.jpg")
    bg = SimpleImage("images/woofy.jpg")
    bg.make_as_big_as(fg)
    combine_img = combine(fg, bg)
    combine_img.show()


if __name__ == '__main__':
    main()
