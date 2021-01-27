"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Code template for Mölkky.
"""


# TODO:
# a) Implement the class Player here.
class Player:
    def __init__(self, name):
        self.__name = name
        self.__point = 0
        self.__sum = 0
        self.__round = 0
        self.__greaterThan0 = 0

    def get_name(self):
        return self.__name

    def get_points(self):
        return self.__point

    def add_points(self, pt):
        if self.__point + pt <= 50:
            self.__point += pt
        else:
            self.__point = 25
            self.printPenalty()
        self.__sum += pt
        self.__round += 1
        if pt >= 1:
            self.__greaterThan0 += 1

    def has_won(self):
        if self.__point == 50:
            return True
        return False

    def printWarning(self):
        sumPt = self.__sum
        if sumPt >= 40 and sumPt <=49:
            print(f"{self.get_name()} needs only {50 - self.get_points()} points. It's better to avoid knocking down the pins with higher points.")

    def printCheers(self, pt):
        if self.__round > 0 and pt > self.avgPt():
            print(f"Cheers {self.__name}!")

    def avgPt(self):
        if self.__round == 0:
            return 0
        return self.__sum / self.__round

    def getSucPercentage(self):
        if self.__round == 0:
            return 0
        return self.__greaterThan0 / self.__round * 100

    def printPenalty(self):
        print(f"{self.get_name()} gets penalty points!")

def main():
    # Here we define two variables which are the objects initiated from the
    # class Player. This is how the constructor of the class Player
    # (the method that is named __init__) is called!

    player1 = Player("Matti")
    player2 = Player("Teppo")

    throw = 1
    while True:

        # if throw is an even number
        if throw % 2 == 0:
            in_turn = player1

        # else throw is an odd number
        else:
            in_turn = player2

        pts = int(input("Enter the score of player " + in_turn.get_name() +
                        " of throw " + str(throw) + ": "))

        in_turn.add_points(pts)

        # TODO:
        # c) Add a supporting feedback printout "Cheers NAME!" here.
        #in_turn.printPenalty()
        in_turn.printWarning()
        in_turn.printCheers(pts)
        

        if in_turn.has_won():
            print("Game over! The winner is " + in_turn.get_name() + "!")
            return

        print("")
        print("Scoreboard after throw " + str(throw) + ":")
        print(player1.get_name() + ":", player1.get_points(), "p" + f", hit percentage {player1.getSucPercentage():.1f}")
        print(player2.get_name() + ":", player2.get_points(), "p" + f", hit percentage {player2.getSucPercentage():.1f}")
        print("")

        throw += 1


if __name__ == "__main__":
    main()
