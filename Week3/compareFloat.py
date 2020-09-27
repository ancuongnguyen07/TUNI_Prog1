
"""
COMP.CS.100 Programming 1
An Cuong Nguyen, cuong.nguyen@tuni.fi
Week3 - compareFloat
"""


def compare_floats(a,b,epsilon):
    """
    The function compare two float numbers with the absolute
    difference epsilon
    Return True if |a-b|<epsilon and false for rest of cases

    :param a: float, first number
    :param b: float, second number
    :return : boolean
    """
    if abs(a-b) < epsilon: return True
    return False
