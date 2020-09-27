"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
"""

def is_the_list_in_order(arr):
    """
    Check whether the list is in ascending order

    :param arr: a list of values
    :return boolean
    """

    for i in range(0,len(arr)-1):
        if arr[i] > arr[i+1]: return False
    return True