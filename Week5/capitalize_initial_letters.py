"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       An Cuong Nguyen
Email:      cuong.nguyen@tuni.fi
Student Id: 050358715

Reverse a string
"""


def capitalize_initial_letters(fullString):
    """
    Capitalize the first char of a phrase

    :param fullString: string
    :return string
    """
    if fullString == '': return ''
    phraseList = fullString.lower().split(' ')
    for i in range(len(phraseList)):
        phraseList[i] = phraseList[i][0].upper() + phraseList[i][1:]
    return ' '.join(phraseList).rstrip()

#print(capitalize_initial_letters("aTtAcK oN TItAN"))