"""
COMP.CS.100 Programming 1
Code Template
"""

def main():
    rowList = read_message()
    maxChar = int(input("Enter the number of characters per line: "))
    print(f"{splitByLine(maxChar,rowList)}")

def read_message():
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """
    rowList = []
    print("Enter text rows. Quit by entering an empty row.")
    while True:
        mess = input()
        if mess == '': return rowList
        i = 0
        while i < (len(mess) - 1):
            if mess[i] == mess[i+1] and mess[i] == ' ': mess = mess[:i] + mess[i + 1]
            i += 1
        rowList.append(mess)

def splitByLine(maxChar, rowList):
    """
    Split a message by line of max characters
    The user enters the number of characters 
    that will be printed in one line. The text 
    justification algoritm will divide the text 
    into segments that are shorter than this and
    then fill in the line to the desired character 
    length by adding space characters inbetween the
    words. The space characters are placed so that
    in the beginning of the line each word spacings
    contain one space character more than in the end of the line.

    The last line of the text won't be filled with extra spaces. 
    It can be shorter than the other lines.

    :param maxChar: int, maximum chars of a line
    return formatted string: string
    """
    formattedRowList = []
    msg = ' '.join(rowList).rstrip()
    i = 0
    n = len(msg)
    while i + maxChar < n:
        nextLastIndex = i + maxChar
        # max length contains enough words
        x = msg[nextLastIndex - 2:nextLastIndex + 1]
        if nextLastIndex < n and  msg[nextLastIndex] == ' ': 
            formattedRowList.append(msg[i: nextLastIndex])
            i += maxChar + 1 # eliminate the space begin in the next line
        # max length doesn't contain enough words, nextLast is not space
        else: # msg[nextLastIndex] != ' '
            lastIndex = nextLastIndex - 1
            cursor =  lastIndex
            while cursor >= i and msg[cursor] != ' ' : cursor -= 1
            numOfSpaces = lastIndex - cursor + 1

            wordsInRow = msg[i: cursor].split(' ')
            numOfWords = len(wordsInRow)
            if numOfWords == 1:
                divisor = remainder = 0
            else:
                divisor = numOfSpaces // (numOfWords - 1)
                remainder = numOfSpaces % (numOfWords - 1)

            for k in range(len(wordsInRow) - 1):
                wordsInRow[k] += divisor * ' '
                if remainder > 0:
                    wordsInRow[k] += ' '
                    remainder -= 1
            formattedRowList.append(' '.join(wordsInRow).rstrip())
            i = cursor + 1

    formattedRowList.append(msg[i:])
    return '\n'.join(formattedRowList).rstrip()
            

if __name__ == "__main__":
    main()