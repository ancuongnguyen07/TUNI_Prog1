"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       An Cuong Nguyen
Email:      cuong.nguyen@tuni.fi
Student Id: 050358715

Reverse a string
"""

def reverse_name(name):
    """
    Split name by comma ',' then reverse the order of a list contains phrases of name
    FirstName + LastName

    :name : string, a string of unformatted name
    :return string with format: FirstName + LastName
    """
    phrase = name.split(',')
    n = len(phrase)
    phrase.reverse()
    formattedName = ''
    for ele in phrase:
        if ele != '':
            formattedName += ele.strip() + ' '
    return formattedName.rstrip()
