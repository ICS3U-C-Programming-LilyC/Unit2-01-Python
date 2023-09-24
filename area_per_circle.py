#!/usr/bin/env python3
# Created By: Lily Carroll
# Date: Sept/22/2023
# This program calculates the area and circumference of a circle, with a radius of 4 cm.

import math

rad = 4


def main():
    print("If the radius of a circle is 4 cm:")
    print("The area is = {:.2f} cm^2".format(math.pi * rad**2))
    print("The circumference is = {:.2f} cm".format(math.pi * 2 * rad))


if __name__ == "__main__":
    main()
