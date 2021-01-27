"""
COMP.CS.100 Programming 1
Code Template
"""

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    msg = read_message()

    print("The same, shouting:")
    print('\n'.join(msg).upper().strip())

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
