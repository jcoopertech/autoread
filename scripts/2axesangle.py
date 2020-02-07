#!/usr/bin/env python3
# - Run in a py3 environment.
# No additional packages required, only using py standard lib.

__doc__ = """
This script takes two axes positions, then based on Y values from proscenium,
is able to calculate their angle - calculating the positions
Originally written for the Guildhall School of Music and Drama by James Cooper,
whilst studying on the BA Hons Technical Theatre Arts course.
"""

__author__ = "James Cooper"
__copyright__ = "Copyright 2019, James Cooper"
__credits__ = ["James Cooper"]
__license__ = "GNU AGPLv3"
__version__ = "0.1.0"
__maintainer__ = "James Cooper"
__email__ = "james@jcooper.tech"
__status__ = "Development"


import math
from read import read_main

def load_Y_values():
    with open("y_values.txt","r") as y_val_file:
        y_list = y_val_file.readlines()
    return y_list


def get_manual():
    z1 = int(input("Z1: "))
    z2 = int(input("Z2: "))
    ax1 = input("enter an axis: ")
    ax2 = input("enter an axis: ")
    return z1, z2, [ax1, ax2]


def calculate_y_diff(axes):
    """Accepts [n,n] type input for axis numbers eg. 1 thru 33."""
    y_list = load_Y_values()
    y1 = int(y_list[axes[0]+1])
    y2 = int(y_list[axes[1]+1])
    if y1 > y2:
        return y1-y2
    elif y2 > y1:
        return y2-y1


def calculateAngle(z1,z2,axes):
    y_diff = calculate_y_diff(axes)
    """First, calculate difference in height of the positions."""
    if z1 > z2:
        z_diff = z1-z2
    elif z2 > z1:
        z_diff = z2-z1
    else:
        z_diff = 0
    print(z_diff)
    """Z diff becomes the vertical side of the triangle.
    We then need to calculate the angle of the hypotenuse based on the """
    angle = math.degrees(math.atan2(z_diff,y_diff))
    return angle


def main():
    AxesArray = read_main()
    print(AxesArray)
    z1, z2, axes = get_manual()
    angle = calculateAngle(z1, z2, axes)
    print(angle)


if __name__ == "__main__":
    main()
