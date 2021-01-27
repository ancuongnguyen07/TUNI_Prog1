"""
This program asks user to enter a file name and
then prints the contents of that file on the screen.
Error message is printed if there are any problems
opening the file.
"""

def main():
    filename = input("Enter the filename: ")

    # The code lines which might cause an error
    # are placed inside try.
    try:
        # Let's try to open the file for reading and if successfull
        # open returns a stream (a value representing the file)
        # which we can use to manipulate the file later in the program.

        file = open(filename, mode="r")

    # If there was an error in the preceeding try block, we can
    # handle if with an except block.  OSError is the error
    # type which is caused by a failed request to the operating
    # system.  For example if the file can not be opened → OSError.

    except OSError:
        print(f"Error: opening the file '{filename}' failed!")

        # When we use return statement in the main function,
        # it will end our program.  Can you say why?
        return

    # If we want to process the file one line at the time,
    # for-loop is the easiest way to achieve it.
    # On every repetition of the loop the variable file_line
    # will automatically contain the next line from the file.
    # The loop will end when all the lines in the file
    # have been processed.

    for file_line in file:

        # When a line is read from a file the string
        # contianing the text of the line will also have the
        # newline character at the end.  Since print-function
        # also adds a newline automatically after whatever it
        # prints, this would result empty lines in the
        # output unless we somehow get rid of the extra
        # newline: rstrip does that.

        file_line = file_line.rstrip()

        print(file_line)

    # When the file has been processed, we should close it.
    file.close()


if __name__ == "__main__":
    main()
