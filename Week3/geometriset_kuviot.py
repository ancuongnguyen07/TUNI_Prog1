"""
COMP.CS.100 Programming 1
Code template for geometric shapes.
"""

from math import pi

def checkPos(prompt):
    """
    Check the input is positive or not and return the positive value

    :return value: float > 0
    """
    while True:
        value = float(input(prompt))
        if value > 0: break
    return value

def printCircumference(value):
    """
    print the area of a shape
    """
    print(f"The total circumference is {value:.2f}")

def printArea(value):
    """
    print the circumference of a shape
    """
    print(f"The surface area is {value:.2f}")

def square():
    """
    Calculate and print the area and the circumference of a square

    :return : no return
    """

    side = checkPos("Enter the length of the square's side: ")
    printCircumference(4 * side)
    printArea(side * side)

def rectangle():
    """
    Calculate and print the area and the circumference of a rectangle

    :return : no return
    """

    side1 = checkPos("Enter the length of the rectangle's side 1: ")
    side2 = checkPos("Enter the length of the rectangle's side 2: ")
        
    printCircumference((side1 + side2) * 2)
    printArea(side2 * side1)

def circle():
    """
    Calculate and print the area and the circumference of a circle

    :return : no return
    """
    radius = checkPos("Enter the circle's radius: ")
    printCircumference(2 * pi * radius)
    printArea(pi * radius * radius)

def menu():
    """
    This function prints a menu for user to select which
    geometric shape to use in calculations.
    """

    while True:
        answer = input("Enter the pattern's first letter, q stops this (s/r/q): ")
        if answer == "s":
            square()
            # replace this comment and "pass" above with your function calls
            # dealing with square.


        elif answer == "r":
            rectangle()
            # replace this comment and "pass" above with your function calls
            # dealing with rectangle.

        elif answer == "c":
            circle()

        elif answer == "q":
            return

        else:
            print("Incorrect entry, try again!")

        print()  # Empty row for the sake of readability


def main():
    menu()
    print("Goodbye!")


if __name__ == "__main__":
    main()
