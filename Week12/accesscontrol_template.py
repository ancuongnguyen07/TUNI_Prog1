"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student numbet: 050358715
Email: cuong.nguyen@tuni.fi 

Project: accesscontrol, program template
"""

DOORCODES = {'TC114': ['TIE'], 'TC203': ['TIE'], 'TC210': ['TIE', 'TST'],
             'TD201': ['TST'], 'TE111': [], 'TE113': [], 'TE115': [],
             'TE117': [], 'TE102': ['TIE'], 'TD203': ['TST'], 'TA666': ['X'],
             'TC103': ['TIE', 'OPET', 'SGN'], 'TC205': ['TIE', 'OPET', 'ELT'],
             'TB109': ['OPET', 'TST'], 'TB111': ['OPET', 'TST'],
             'TB103': ['OPET'], 'TB104': ['OPET'], 'TB205': ['G'],
             'SM111': [], 'SM112': [], 'SM113': [], 'SM114': [],
             'S1': ['OPET'], 'S2': ['OPET'], 'S3': ['OPET'], 'S4': ['OPET'],
             'K1705': ['OPET'], 'SB100': ['G'], 'SB202': ['G'],
             'SM220': ['ELT'], 'SM221': ['ELT'], 'SM222': ['ELT'],
             'secret_corridor_from_building_T_to_building_F': ['X', 'Y', 'Z'],
             'TA': ['G'], 'TB': ['G'], 'SA': ['G'], 'KA': ['G']}

INPUTFILENAME = "accessinfo.txt"

class Accesscard:
    """
    This class models an access card which can be used to check
    whether a card should open a particular door or not.
    """

    def __init__(self, id, name):
        """
        Constructor, creates a new object that has no access rights.

        :param id: str, card holders personal id
        :param name: str, card holders name

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME OR THE
        PARAMETERS!
        """

        # TODO: Implement the constructor
        self.__id = id
        self.__name = name
        self.__accessCodesList = []


    def info(self):
        """
        The method has no return value. It prints the information related to
        the access card in the format:
        id, name, access: a1,a2,...,aN
        for example:
        777, Thelma Teacher, access: OPET, TE113, TIE
        Note that the space characters after the commas and semicolon need to
        be as specified in the task description or the test fails.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE PRINTOUT FORMAT!
        """

        # TODO: Implement the method
        accessCodesStr = ', '.join(sorted(self.__accessCodesList))
        print(f"{self.__id}, {self.__name}, access: {accessCodesStr.rstrip()}")


    def get_name(self):
        """
        :return: Returns the name of the accesscard holder.
        """

        # TODO: Implement the method
        return self.__name

    def listDoorCodes(self):
        """
        Return a list which contains all door codes of this access card

        :return : list
        """
        doorCodesList = []
        for accessCode in self.__accessCodesList:
            if isDoorCode(accessCode):
                doorCodesList.append(accessCode)
        return doorCodesList

    def add_access(self, new_access_code):
        """
        The method adds a new accesscode into the accesscard according to the
        rules defined in the task description.

        :param new_access_code: str, the accesscode to be added in the card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # TODO: Implement the method
        
        # invalid code is checked outside
        # check duplicate
        if new_access_code in self.__accessCodesList:
            return

        if isDoorCode(new_access_code):
            # check if this door code is 'unnecessary'
            # by checking if there is any area code in this access card
            # has access to this door code
            for accessCode in self.__accessCodesList:
                if accessCode in DOORCODES[new_access_code]:
                    return     
        else : # is an area code
            doorCodesList = self.listDoorCodes()
            
            # remove 'unnecessary' door codes
            for doorCode in doorCodesList:
                if new_access_code in DOORCODES[doorCode]:
                    self.__accessCodesList.remove(doorCode)

        self.__accessCodesList.append(new_access_code)


    def check_access(self, door):
        """
        Checks if the accesscard allows access to a certain door.

        :param door: str, the doorcode of the door that is being accessed.
        :return: True: The door opens for this accesscard.
                 False: The door does not open for this accesscard.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # TODO: Implement the method
        # invalid code is checked outside
        for accessCode in self.__accessCodesList:
            if door == accessCode or accessCode in DOORCODES[door]:
                return True
        return False

    def merge(self, card):
        """
        Merges the accesscodes from another accesscard to this accesscard.

        :param card: Accesscard, the accesscard whose access rights are added to this card.

        THIS METHOD IS AUTOMATICALLY TESTED, DON'T CHANGE THE NAME, THE
        PARAMETERS, OR THE RETURN VALUE! DON'T PRINT ANYTHING IN THE METHOD!
        """

        # TODO: Implement the method
        for accessCode in card.__accessCodesList:
            self.add_access(accessCode)


# TODO: Implement helper functions here.
def isDoorCode(accessCode):
    """
    Check if 'accessCode' is a door code or not

    :return:    True if 'accessCode' is a door code
                False if 'accessCode' is not a door code
    """
    return accessCode in DOORCODES

def isAreaCode(accessCode):
    """
    Check if 'accessCode' is an area code or not

    :return:    True if 'accessCode' is an area code
                False if 'accessCode' is not an area code
    """
    for areaCodeList in DOORCODES.values():
        # DOORCODES.values() return a list of lists of area codes
        if accessCode in areaCodeList:
            return True
    return False

def isValidCode(accessCode):
    """
    Check if accessCode is valid or not

    :return:    True if 'accessCode' is valid
                False if 'accessCode' is invalid
    """
    return isDoorCode(accessCode) or isAreaCode(accessCode)

def isEmpty(str):
    """
    Check if a string is empty or not

    :return:    True if a string is empty
                False if a string is not empty
    """
    return str.strip() == "" 

def isIDExist(cardDict, id):
    """
    Check if an id is in an access card dict or not

    :return:    True if an access card dict stores id
                False if an access card dict doesn't store id
    """
    
    return id in cardDict


def main():
    # TODO: Implement the reading of the inputfile and
    # storing the information into a data structure.

    accessCardDict = {}
    try:
        file = open(file = INPUTFILENAME, mode = 'r')
        for line in file:
            id, name, accessCodeStr = line.split(';')
            # check if 'id' or 'name' is empty or not
            if isEmpty(id) or isEmpty(name) or id in accessCardDict:
                raise ValueError
            
            accessCardDict[id] = Accesscard(id, name)
            # check if there is any access codes or not
            if isEmpty(accessCodeStr):
                continue
            accessCodeList = accessCodeStr.split(',')       

            for accessCode in accessCodeList:
                # check if 'access code' is empty or not 
                if isEmpty(accessCode):
                    raise ValueError
                accessCardDict[id].add_access(accessCode.strip())
            
    except ValueError:
        print("Error: file cannot be read.")
        return
    except IOError:
        print("Error: file cannot be read.")
        return

    while True:
        line = input("command> ")

        if line == "":
            break

        strings = line.split()
        command = strings[0]

        if command == "list" and len(strings) == 1:
            # TODO: Excecute the command list here

            for card in sorted(accessCardDict):
                accessCardDict[card].info()

        elif command == "info" and len(strings) == 2:
            card_id = strings[1]
            # TODO: Excecute the command info here

            if isIDExist(accessCardDict,card_id):
                accessCardDict[card_id].info()
            else:
                print("Error: unknown id.")
                continue

        elif command == "access" and len(strings) == 3:
            card_id = strings[1]
            door_id = strings[2]
            # TODO: Excecute the command access here

            if not isIDExist(accessCardDict,card_id):
                print("Error: unknown id.")
                continue
            if not isDoorCode(door_id):
                print("Error: unknown doorcode.")
                continue

            card = accessCardDict[card_id]
            if card.check_access(door_id):
                print(f"Card {card_id} ( {card.get_name()} ) has access to door {door_id}")
            else:
                print(f"Card {card_id} ( {card.get_name()} ) has no access to door {door_id}")
            

        elif command == "add" and len(strings) == 3:
            card_id = strings[1]
            access_code = strings[2]
            # TODO: Excecute the command add here

            if not isIDExist(accessCardDict, card_id):
                print("Error: unknown id.")
                continue
            if not isValidCode(access_code):
                print("Error: unknown accesscode.")
                continue
            accessCardDict[card_id].add_access(access_code)

        elif command == "merge" and len(strings) == 3:
            card_id_to = strings[1]
            card_id_from = strings[2]
            # TODO: Excecute the command merge here

            if isIDExist(accessCardDict,card_id_to) and isIDExist(accessCardDict,card_id_from):
                accessCardDict[card_id_to].merge(accessCardDict[card_id_from])
            else:
                print("Error: unknown id.")
                continue

        elif command == "quit":
            print("Bye!")
            return
        else:
            print("Error: unknown command.")


if __name__ == "__main__":
    main()
