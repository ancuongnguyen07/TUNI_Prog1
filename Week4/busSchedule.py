"""
COMP.CS.100 Programming 1
Code template for "replacing grades" program
"""

def threeNextBuses(busSchedule, curTime):
    """
    Based on the current time, print the 3 next buses

    :param busSchedule: the bus time table
    :param curTime: the current time
    :return : no return, just print the results
    """
    totalTimes = len(busSchedule)
    start = 0
    for index in range(totalTimes - 1,-1,-1):
        if busSchedule[index] < curTime: 
            start = index + 1
            break
    print("The next buses leave:")
    for i in range(start, start + 3):
        print(f"{busSchedule[i % totalTimes]}")

def main():
    BUS_SCHEDULE = [630,1015,1415,1620,1720,2000]
    currentTime = int(input("Enter the time (as an integer): "))
    threeNextBuses(BUS_SCHEDULE, currentTime)

if __name__ == "__main__":
    main()