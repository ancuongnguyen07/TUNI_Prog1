"""
This program asks user to enter a file name and
then prints the contents of that file on the screen.
Error message is printed if there are any problems
opening the file.
"""

def main():
    scoreDict = {}
    fileName = input("Enter the name of the score file: ")

    try:
        file = open(fileName,'r')
    except OSError:
        print("There was an error in reading the file.")
        return

    for line in file:
        try:
            name, score = line.split()
        except ValueError:
            print("There was an erroneous line in the file:")
            print(line)
            return

        try:
            score = int(score)
        except ValueError:
            print("There was an erroneous score in the file:")
            print(score)
            return

        if name not in scoreDict:
            scoreDict[name] = score
        else:
            scoreDict[name] += score

    print("Contestant score:")
    for name in sorted(scoreDict):
        print(f"{name} {scoreDict[name]}")


if __name__ == "__main__":
    main()