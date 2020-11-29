#!/usr/bin/env python3

# Created by: Nicholas Graziano
# Created on: November 2020
# This program calculates the circumference of a circle
#    with user input

import constants


def main():
    # this function calculates circumference

    # input
    radius = int(input("Enter radius of the circle (mm):"))

    # process
    circumference = constants.TAU*radius

    # output
    print("")
    print("Circumference is {}mm^2".format(circumference))


if __name__ == "__main__":
    main()
