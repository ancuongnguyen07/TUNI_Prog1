"""
This program asks user to enter a file name and
then prints the contents of that file on the screen.
Error message is printed if there are any problems
opening the file.
"""

def main():
    fileName = input("Enter the name of the file: ")

    try:
        file = open(fileName,'r')

    except OSError:
        print(f"Failed to open file: {fileName}")
        return
    
    line = 0
    for fileLine in file:
        contentLine = fileLine.rstrip()
        #if contentLine == "": return
        line +=1 
        print(f"{line} {contentLine}")
    file.close()

if __name__=="__main__":
    main()