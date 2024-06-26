# File to calculate shapes

import math

def calc_circle_area(radius):
    return radius * radius * math.pi

def calc_triangle_area(base, height):
    return 1/2 * base * height

def square(side):
    return side * side

def calc_square_perimiter(side):
    return side * 4

def main():
    print(f"\n A square with a side length of 5 has an area of {square(5)}")
    print(f"Circle with radius of 5 has area of {calc_circle_area(5):.2f}")
    print(f"A triangle with base of 5 has height of 5 has an area of {calc_triangle_area(5, 5):.2f}\n")


if __name__ == "__main__":
    main()