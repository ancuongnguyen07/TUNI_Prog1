"""
COMP.CS.100 Programming 1 code template
Fill in all TODOs in this file
"""

from math import sqrt


def menu():
    """
    This is a text-based menu. You should ONLY TOUCH TODOs inside the menu.
    TODOs in the menu call functions that you have implemented and take care
    of the return values of the function calls.
    """

    tank_size = read_number("How much does the vehicle's gas tank hold? ")
    gas = tank_size  # Tank is full when we start
    gas_consumption = read_number("How many liters of gas does the car " +
                                  "consume per hundred kilometers? ")
    x = 0.0  # Current X coordinate of the car
    y = 0.0  # Current Y coordinate of the car

    while True:
        print("Coordinates x={:.1f}, y={:.1f}, "
              "the tank contains {:.1f} liters of gas.".format(x, y, gas))

        choice = input("1) Fill 2) Drive 3) Quit\n-> ")

        if choice == "1":
            to_fill = read_number("How many liters of gas to fill up? ")
            gas = fill(tank_size,to_fill,gas)

        elif choice == "2":
            new_x = read_number("x: ")
            new_y = read_number("y: ")
            gas, x, y = drive(x,y,new_x,new_y,gas,gas_consumption)

        elif choice == "3":
            break

    print("Thank you and bye!")


def fill(tankSize, requiredGas, currentGas):
    """
    This function has three parameters which are all FLOATs:
      (1) the size of the tank
      (2) the amount of gas that is requested to be filled in
      (3) the amount of gas in the tank currently

    The parameters have to be in this order.
    The function returns one FLOAT that is the amount of gas in the
    tank AFTER the filling up.

    The function does not print anything and does not ask for any
    input.
    """
    theoricalCurrentGas = currentGas + requiredGas
    if theoricalCurrentGas > tankSize: currentGas = tankSize
    else: currentGas = theoricalCurrentGas
    return currentGas


def drive(curX, curY, desX, desY, curGas, avgConsGas):
    """
    This function has six parameters. They are all floats.
      (1) The current x coordinate
      (2) The current y coordinate
      (3) The destination x coordinate
      (4) The destination y coordinate
      (5) The amount of gas in the tank currently
      (6) The consumption of gas per 100 km of the car

    The parameters have to be in this order.
    The function returns three floats:
      (1) The amount of gas in the tank AFTER the driving
      (2) The reached (new) x coordinate
      (3) The reached (new) y coordinate

    The return values have to be in this order.
    The function does not print anything and does not ask for any
    input.
    """
    theoricalLenght = displacement(curX, curY, desX, desY)
    plannedGasCons = gasConsumption(avgConsGas,theoricalLenght)


    # if the gas is running out during the trip
    if plannedGasCons > curGas:
        possibleLength = maxTripByGas(avgConsGas,curGas)
        newX, newY = posByLenght(curX, curY,possibleLength, theoricalLenght, desX, desY)
        return 0, newX, newY
    # else
    return float(curGas - plannedGasCons), desX, desY

    # It might be usefull to make one or two assisting functions
    # to help the implementation of this function.


def displacement(curX, curY, newX, newY):
    """
    Calculate the length of displacement which the car move

    :return length: float, using Pytago in a triangle
    """
    deltaX = abs(newX - curX)
    deltaY = abs(newY - curY)
    return float(sqrt(deltaX ** 2 + deltaY ** 2))

def gasConsumption(avgConsGas, lenghtOfDisplacement):
    """
    Calculate the gas consumption when the car move a trip (s)
    avgConsGas per 100km
    gasConsumption = (lenghtOfDisplacement * avgConsGas) / 100

    :return gasConsumption: float
    """
    return float((avgConsGas * lenghtOfDisplacement) / 100)

def maxTripByGas(avgConsGas, curGas):
    """
    Calculate the maximum possible lenght of trip the car can
    move with the current gas in tank

    :return lengthOfTrip: float, maximum value 
    """
    return float(curGas * 100 / avgConsGas)

def posByLenght(curX, curY, posLength, theLength, theX, theY):
    """
    Calculate possible x,y-coordinate based on the legnth of possible trip
    lenght of theorical trip, theorical x,y-coordinate
    deltaX/(theX-curX)=deltaY/(theY-curY)=posLength/theLength

    :return posX,posy: float
    """
    deltaX = (theX - curX) * posLength / theLength
    deltaY = (theY - curY) * posLength / theLength

    return curX + deltaX, curY + deltaY

# Implement your own functions here. You are required to
# implement at least two functions that take at least
# one parameter and return at least one value.  The
# functions have to be used somewhere in the program.


def read_number(prompt, error_message="Incorrect input!"):
    """
    DO NOT TOUCH THIS FUNCTION.
    This function reads input from the user.
    Also, don't worry if you don't understand it.
    """

    try:
        return float(input(prompt))

    except ValueError:
        print(error_message)
        return read_number(prompt, error_message)


def main():
    menu()


if __name__ == "__main__":
    main()
