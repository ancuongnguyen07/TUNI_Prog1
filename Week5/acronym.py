"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       An Cuong Nguyen
Email:      cuong.nguyen@tuni.fi
Student Id: 050358715

Reverse a string
"""

def create_an_acronym(fullName):
    """
    Create an acronym from the full name

    :param fullName: string
    :return string
    """
    acronym = []
    for ele in fullName.strip().split():
        acronym.append(ele[0].upper())
    return ''.join(acronym).strip()
