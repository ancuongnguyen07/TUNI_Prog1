"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
"""

def are_all_members_same(arr):
    """
    Check whether the arr includes all the same members

    :param arr: a list of values
    :return boolean
    """
    for i in range(1,len(arr)):
        if arr[0] != arr[i]: return False
    return True

