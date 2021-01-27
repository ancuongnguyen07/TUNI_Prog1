"""
COMP.CS.100 Programming 1
ROT13 program code template
"""

def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars   = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]

    # TODO: implement encryption here
    if not text.isalpha(): return text
    index = regular_chars.index(text.lower())
    if text.isupper(): return encrypted_chars[index].upper()
    return encrypted_chars[index]


def row_encryption(fullString):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    encryptedString = []
    for char in fullString:
        encryptedString.append(encrypt(char))
    return ''.join(encryptedString)


#print(row_encryption("Happy, happy, joy, joy!"))