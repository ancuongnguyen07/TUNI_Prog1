"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Student number: 050358715
Full name: An Cuong Nguyen
"""

LOAN_TIME = 3
MAX_LOANS = 3


class Librarycard:
    def __init__(self, card_id, card_holder):
        self.__id = card_id
        self.__holder = card_holder
        # dictionary of loaned books with key is book id (string)
        # value is loan time (int)
        self.__loanedBooks = {} 

    def holder(self):
        return self.__holder

    def getId(self):
        return self.__id

    def info(self):
        prompt = "-"
        print("Card holder:", self.__holder)
        if self.countLoanedBook() == 0:
            print(prompt, "No loans")
        else:
            lbd = self.__loanedBooks # lbd stands for loaned book dictionary
            for book in sorted(lbd):
                print(prompt, f"Loan {book}, loan time left {lbd[book]} weeks")

    def addBook(self, bookId):
        self.__loanedBooks[bookId] = LOAN_TIME

    def removeBook(self, bookId):
        #Check 'bookId' is in loaned list of this card
        #is outside this function
        del self.__loanedBooks[bookId]

    def countLoanedBook(self):
        return len(self.__loanedBooks)

    def isBookLoaned(self, bookId):
        return bookId in self.__loanedBooks

    def updateLoanTime(self):
        """
        Reducing 1 week in loan time of all borrowed books
        """
        lbd = self.__loanedBooks # lbd stands for loaned book dictionary
        for id in lbd:
            if lbd[id] > 0:
                lbd[id] -= 1

def read_card_data(file_name):
    """
    Read text file containing info about library cards:
    Structure of a file:
    'card_id';'card_holder'

    :return : a dictionary with key is card id (string)
                value is 'Librarycard' object
    """
    card_data = {}

    try:
        file_object = open(file_name, mode="r")

        for line in file_object:
            line = line.strip()
            strings = line.split(";")

            card_id = int(strings[0])
            card_holder = strings[1]

            new_card = Librarycard(card_id, card_holder)

            card_data[card_id] = new_card

    except OSError:
        print("Error in reading the file")
        return None

    return card_data


def read_card_id(prompt, database):
    while True:
        try:
            id = int(input(prompt))

            while id not in database:
                print("Erroneous card id, existing id's are:")
                listing(database)
                id = int(input(prompt))

            return id

        except ValueError:
            print("Erroneous card id, existing id's are:")
            listing(database)


def listing(cards):
    for card in sorted(cards):
        print(card, ":", cards[card].holder())

def findCardById(cardData, id):
    """
    Find and return the 'Librarycard' object have an 'id'

    :parameter: 'cardData' (dictionary of cards) 
                'id' (int): id of a card which is needed to find
    :return  :  'Librarycard' object
    ---- Check the exist of id is outside this function
    """
    for i in cardData:
        if cardData[i].getId() == id:
            return cardData[i]
    return None

def bookTakenBy(cardData, bookId):
    """
    Find the 'Librarycard' object which loans the book

    :parameter: 'cardData' (dictionary of cards)
                'bookId' (string)
    :return :   'Librarycard' object 
                'None' if the book is not loaned by any 'Librarycard' objects
    """
    for id in cardData:
        card = cardData[id]
        if card.isBookLoaned(bookId):
            return card
    return None

def borrowBook(cardData):
    """
    Executing the 'B' command 
    """
    # read the id card and check if this id is valid
    id = read_card_id("Card code: ", cardData)
    card = findCardById(cardData,id)

    # read the book id and find the card borrows the book
    bookId = input("Book code: ")
    cardBorrowBook = bookTakenBy(cardData, bookId)

    # there is a card borrowing the book
    if cardBorrowBook != None:
        print(f"Customer {cardBorrowBook.getId()} {cardBorrowBook.holder()}", \
            f"has already borrowed book with id {bookId}")
        return
    
    # the card has already borrowed the maximum amount of books
    if card.countLoanedBook() == MAX_LOANS:
        print(f"Card {id} has already {MAX_LOANS} loans")
        print("Loan not successful")
    else:
        # add the book to dictionary of loaned books in 'Librarycard' object
        card.addBook(bookId)
        print(f"Loan successful, loan time {LOAN_TIME} weeks")

def returnBook(cardData):
    """
    Executing the 'R' command
    """
    # read the book id and find the card borrows the book
    bookId = input("Book code: ")
    cardBorrowBook = bookTakenBy(cardData, bookId)

    # no card borrow the book
    if cardBorrowBook == None:
        print("This book has not been borrowed by anyone")
    else:
        cardBorrowBook.removeBook(bookId)
        print("Book returned")

def oneWeekPass(cardData):
    """
    Executing the 'W' command
    """
    for id in cardData:
        cardData[id].updateLoanTime()
    print("Loan times updated!")

def main():
    library = read_card_data("library.txt")
    if library == None:
        return

    print("Welcome to Perähikiä library!")

    while True:
        command = input("Command: ")
        command = command.upper()

        if command == "I":
            card = read_card_id("Card code: ", library)
            library[card].info()

        elif command == "L":
            listing(library)

        elif command == "B":
            borrowBook(library)

        elif command == "R":
            returnBook(library)

        elif command == "W":
            oneWeekPass(library)

        elif command == "" or command == "Q":
            print("Thankyou and good bye!")
            return

        else:
            print("Erroneous command!")
            print("The commands are:")
            print("Info")
            print("List librarycards")
            print("Borrow")
            print("Return")
            print("new Week")


if __name__ == "__main__":
    main()
