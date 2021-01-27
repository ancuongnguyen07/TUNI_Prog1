"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Fractions code template
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        sign = ""
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        """else:
            sign = """""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        Simplify the fraction
        """
        gcd = greatest_common_divisor(self.__denominator,self.__numerator)
        """self.__denominator //= gcd
        self.__numerator //= gcd"""

        return Fraction(self.__numerator // gcd, self.__denominator // gcd)

    def complement(self):
        """
        Return a new fraction object which numerator = -self.__numerator
        :return : fraction object
        """
        return Fraction(-self.__numerator,self.__denominator)

    def reciprocal(self):
        """
        Return a new fraction object which numerator, denominator is swapped
        :return : fraction object
        """
        return Fraction(self.__denominator, self.__numerator)

    def multiply(self, frac2):
        """
        Multiply 2 fractions
        :return : fraction object
        """
        newNumerator = self.__numerator * frac2.__numerator
        newDenominator = self.__denominator * frac2.__denominator

        return Fraction(newNumerator, newDenominator)

    def divide(self,frac2):
        """
        Divide 2 fractions
        : return : fraction object
        """

        inverseFrac = frac2.reciprocal()
        return self.multiply(inverseFrac)

    def add(self,frac2):
        """
        Add 2 fractions
        :return : fraction object
        """
        newNumerator = self.__numerator * frac2.__denominator + frac2.__numerator * self.__denominator
        newDenominator = self.__denominator * frac2.__denominator 
        return Fraction(newNumerator, newDenominator)

    def deduct(self,frac2):
        """
        Substract 2 fractions
        :return : fraction object
        """
        newNumerator = self.__numerator * frac2.__denominator - frac2.__numerator * self.__denominator
        newDenominator = self.__denominator * frac2.__denominator 
        return Fraction(newNumerator, newDenominator)

    def __lt__(self, other):
        """
        Built-in method if 'self' is less than 'other'
        :return : boolean value
        """
        return self.__numerator * other.__denominator < other.__numerator * self.__denominator

    def __str__(self):
        """
        Built-in method return string of object
        :return : string
        """
        return self.return_string()



def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a

def main():
    """
    Get user's input (fraction) then store in a list 
    Print simplified format of each fraction
    """
    fracDict = {}

    while True:
        command = input("> ")

        if command == "add":
            fracText = input("Enter a fraction in the form integer/integer: ")
            name = input("Enter a name: ")

            numerator, denominator = fracText.split("/")
            fracDict[name] = Fraction(int(numerator), int(denominator))
        elif command == "print":
            name = input("Enter a name: ")
            if name not in fracDict:
                print(f"Name {name} was not found")
            else:
                print(f"{name} = {fracDict[name]}")
        elif command == "list":
            for fr in sorted(fracDict):
                print(f"{fr} = {fracDict[fr]}")
        elif command == "*":
            firstName = input("1st operand: ")
            if firstName not in fracDict:
                print(f"Name {firstName} was not found")
                continue

            secondName = input("2nd operand: ")
            if secondName not in fracDict:
                print(f"Name {secondName} was not found")
                continue
            multipliedFrac = fracDict[firstName].multiply(fracDict[secondName])
            print(f"{fracDict[firstName]} * {fracDict[secondName]} = {multipliedFrac}")
            print(f"simplified {multipliedFrac.simplify()}")
        elif command == "file":
            fileName = input("Enter the name of the file: ")
            try:
                file = open(fileName, mode='r')
                for row in file:
                    name, fracText = row.split("=")
                    numerator, denominator = fracText.split('/')

                    fracDict[name] = Fraction(int(numerator), int(denominator))
            except IOError:
                print("Error: the file cannot be read.")
                continue
            except ValueError:
                print("Error: the file cannot be read.")
                continue
            
            file.close()

        elif command == "quit":
            print("Bye bye!")
            break
        else:
            print("Unknown command!")

if __name__ == "__main__":
    main()

    

