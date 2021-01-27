"""
Check if a file is exist or not
Author: xxx
"""

def main():
    fileName = input("Enter the name of the file: ")

    try:
        file = open(fileName,'r')
        file.close()
    except OSError:
        print("There was an error in reading the file.")

    #file.write()

if __name__=="__main__":
    main()