"""
This program asks user to enter a file name and
then prints the contents of that file on the screen.
Error message is printed if there are any problems
opening the file.
"""

def read_message():
    """
    Read user's inputs,then return a list of them
    :return : a list of a string
    """
    messList = []
    while True:
        mess = input()
        if mess == "": return messList
        messList.append(mess.rstrip())

def main():
    fileName = input("Enter the name of the file: ")
    try:
        fileToWrite = open(fileName,'w')
    except OSError:
        print(f"Writing the file {fileName} was not successful.")
        return
    print("Enter rows of text. Quit by entering an empty row.")
    
    messList = read_message()
    for i in range(len(messList)):
        print(f"{i + 1} {messList[i]}",file=fileToWrite)

    print(f"File {fileName} has been written.")
    fileToWrite.close()

if __name__ == "__main__":
    main()