"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
"""

def input_to_list(maxNum):
    """
    Input nums from user typing

    :param maxNum: the number of nums user want
    :return arr: a list of numbers user typed
    """
    print(f"Enter {maxNum} numbers:")
    arr = []
    for _ in range(maxNum):
        arr += [int(input())]
    return arr

def count(numArr, num):
    """
    Count how many times the 'num' variable appears
    in 'numArr'

    :param numArr: list of number
    :param num: abritatry number
    :return appear-times
    """
    count = 0
    for ele in numArr:
        if ele == num: count += 1
    return count

def main():
    maxNum = int(input("How many numbers do you want to process: "))
    myArr = input_to_list(maxNum)
    searchedNum = int(input("Enter the number to be searched: "))
    times = count(myArr,searchedNum)
    if times == 0:
        print(f"{searchedNum} is not among the numbers you have entered.")
    else:
        print(f"{searchedNum} shows up {times} times among the numbers you have entered.")


if __name__ == "__main__":
    main()
