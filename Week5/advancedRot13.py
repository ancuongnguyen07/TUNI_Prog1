"""
COMP.CS.100 Programming 1
ROT13 program code template
"""

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("ROT13:")
    for row in msg:
        print(row_encryption(row))

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

def read_message():
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    rowList = []
    #print("Enter the text rows of the message. End by entering an empty row.")
    while True:
        mess = input()
        if mess == '': return rowList
        rowList.append(mess)

if __name__ == "__main__":
    main()