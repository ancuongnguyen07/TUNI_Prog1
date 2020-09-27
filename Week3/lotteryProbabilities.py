
"""
COMP.CS.100 Programming 1
An Cuong Nguyen, cuong.nguyen@tuni.fi
Week3
"""

def factorial(n):
    """
    The fuction calculate n!

    :param n: integer
    :return n!: integer
    """
    result = 1
    for i in range(1,n + 1): result *= i
    return result

def lotteryLines(lotteryBall, drawnBall):
    """
    The function calculate total lottery lines as the formula
    lotteryBall!/((lotteryBall - drawnBall)! * drawnBall!)

    :param lotteryBall, drawnBall: integer
    :return lotter lines: integer
    """ 
    return int(factorial(lotteryBall)/(factorial(lotteryBall - drawnBall) * factorial(drawnBall)))

def main():
    # lottery ball: lBall, drawn ball: dBall
    lBall = int(input("Enter the total number of lottery balls: "))
    dBall = int(input("Enter the number of the drawn balls: "))
    
    if lBall <= 0 or dBall <= 0:
        print("The number of balls must be a positive number.")
        return
    if lBall < dBall:
        print("At most the total number of balls can be drawn.")
        return
    print(f"The probability of guessing all {dBall} balls correctly is 1/{lotteryLines(lBall,dBall)}")


if __name__=="__main__":
    main()