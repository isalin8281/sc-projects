"""
File: stanCodoshop.py
Name: Isabelle
----------------------------------------------
SC101_Assignment3
Adapted from Nick Parlante's
Ghost assignment by Jerry Liao.

-----------------------------------------------

"""

import os
import sys
from simpleimage import SimpleImage


def get_pixel_dist(pixel, red, green, blue):
    """
    Returns the color distance between pixel and mean RGB value

    Input:
        pixel (Pixel): pixel with RGB values to be compared
        red (int): average red value across all images
        green (int): average green value across all images
        blue (int): average blue value across all images

    Returns:
        dist (int): color distance between red, green, and blue pixel values

    """
    red_dis = (red-pixel.red) ** 2
    green_dis = (green - pixel.green) ** 2
    blue_dis = (blue - pixel.blue) ** 2
    # distance
    dist = (red_dis + green_dis + blue_dis) ** 0.5
    return dist


def get_average(pixels):
    """
    Given a list of pixels, finds the average red, blue, and green values

    Input:
        pixels (List[Pixel]): list of pixels to be averaged
    Returns:
        rgb (List[int]): list of average red, green, blue values across pixels respectively

    Assumes you are returning in the order: [red, green, blue]

    """
    red = 0
    green = 0
    blue = 0
    for pix in pixels:
        red += pix.red
        green += pix.green
        blue += pix.blue
    # average red value
    red = red // len(pixels)
    # average green value
    green = green // len(pixels)
    # average blue value
    blue = blue // len(pixels)
    # list of average values
    rgb = [red, green, blue]
    return rgb


def get_best_pixel(pixels):
    """
    Given a list of pixels, returns the pixel with the smallest
    distance from the average red, green, and blue values across all pixels.

    Input:
        pixels (List[Pixel]): list of pixels to be averaged and compared
    Returns:
        best (Pixel): pixel closest to RGB averages

    """
    # pixel. use pixels[0] as default value
    best = pixels[0]
    # list of average red, green, blue values across pixels respectively
    rgb = get_average(pixels)
    # distance. use pixels[0] as default value
    def_v = get_pixel_dist(pixels[0], rgb[0], rgb[1], rgb[2])
    # get best pixel
    for pix in pixels:
        # distance
        dis = get_pixel_dist(pix, rgb[0], rgb[1], rgb[2])
        # compare and get smallest value
        if dis < def_v:
            def_v = dis
            best = pix
    return best


def solve(images):
    """
    Given a list of image objects, compute and display a Ghost solution image
    based on these images. There will be at least 3 images and they will all
    be the same size.

    Input:
        images (List[SimpleImage]): list of images to be processed
    """
    width = images[0].width
    height = images[0].height
    result = SimpleImage.blank(width, height)
    ######## YOUR CODE STARTS HERE #########
    # Wre to populate image and create the 'ghost' effect
    for y in range(result.height):
        for x in range(result.width):
            # empty list
            pixels = []
            # get pixel on (x, y)
            result_pix = result.get_pixel(x, y)
            # get pixels on (x, y) from each image
            for img in images:
                img_pixel = img.get_pixel(x, y)
                # list of pixels from each image
                pixels += [img_pixel]
            # get smallest distance
            best = get_best_pixel(pixels)
            # best pixels on blank image
            result_pix.red = best.red
            result_pix.green = best.green
            result_pix.blue = best.blue
    ######## YOUR CODE ENDS HERE ###########
    print("Displaying image!")
    result.show()


def jpgs_in_dir(dir):
    """
    (provided, DO NOT MODIFY)
    Given the name of a directory, returns a list of the .jpg filenames
    within it.

    Input:
        dir (string): name of directory
    Returns:
        filenames(List[string]): names of jpg files in directory
    """
    filenames = []
    for filename in os.listdir(dir):
        if filename.endswith('.jpg'):
            filenames.append(os.path.join(dir, filename))
    return filenames


def load_images(dir):
    """
    (provided, DO NOT MODIFY)
    Given a directory name, reads all the .jpg files within it into memory and
    returns them in a list. Prints the filenames out as it goes.

    Input:
        dir (string): name of directory
    Returns:
        images (List[SimpleImages]): list of images in directory
    """
    images = []
    jpgs = jpgs_in_dir(dir)
    for filename in jpgs:
        print("Loading", filename)
        image = SimpleImage(filename)
        images.append(image)
    return images


def main():
    # (provided, DO NOT MODIFY)
    args = sys.argv[1:]
    # We just take 1 argument, the folder containing all the images.
    # The load_images() capability is provided above.
    images = load_images(args[0])
    solve(images)


if __name__ == '__main__':
    main()
