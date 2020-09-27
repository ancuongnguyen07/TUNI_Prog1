"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""

# TODO: add the definition for convert_grades here
def convert_grades(gradesList):
    """
    Convert the grades to another scale

    :param a list of grades
    :return no return, just modified the values in the list
    """
    for i in range(len(gradesList)):
        if gradesList[i] > 0: gradesList[i] = 6

def main():
    # grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    grades = []
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == "__main__":
    main()
