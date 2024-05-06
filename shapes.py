# File to calculate shapes

import math

def calc_circle_area(radius):
    return radius * radius * math.pi

def square(side):
    return side * side

def main() -> None:
    print(f"\n A square with a side length of 5 has an area of {square(5)}")
    print(f"Circle with radius of 5 has area of {calc_circle_area(5):.2f}\n")

if __name__ == "__main__":
    main()