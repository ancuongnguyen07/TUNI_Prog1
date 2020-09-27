"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
"""

def inputList(numOfPoints):
    """
    Ask user type the point and package these points into 
    a ascending-order list 

    :param numOfPoints: a number of points a list can contains
    :return :list of points
    """
    pointList = []
    for i in range(numOfPoints):
        pointList.append(float(input(f"Enter the time for performance {i + 1}: ")))
    return pointList

def removeMinMax(pointList):
    """
    Remove the best and the worst point of the list

    :param list of points
    :return removed-best-worst list of points
    """
    pointList.sort()
    pointList.pop(0)
    pointList.pop(len(pointList) - 1)
    return pointList

def avgPoint(pointList):
    """
    Calculate the average point of the list

    :param list of points
    :return avg_point
    """
    return sum(pointList)/len(pointList)

def main():
    myList = inputList(5)
    removeMinMax(myList)
    print(f"The official competition score is {avgPoint(myList):.2f} seconds.")

if __name__ == "__main__":
    main()