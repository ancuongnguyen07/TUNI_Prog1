"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       An Cuong Nguyen
Email:      cuong.nguyen@tuni.fi
Student Id: 050358715


A template of a program to output a logarithmic histogram
of energy consumption measurements.
"""

def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()

    """
    # Test values for the input data, so they don't have to be manually
    # entered every single time you want to test your program.  Before
    # submitting your program to Plussa these must be replaced by values
    # read from the user, otherwise the tests will fail.
    input_data = [
        22, 3, 4444, 333, 1000000000, 4, 33, 1, 55,
        5555, 2, 555, 44, 55555, 444, 999999999, 5,
    ]
    """
    
    prompt= "Enter energy consumption (kWh): "
    inputData, maxData = userInput(prompt)
    
    # maxData = -1 means that list of user's input is empty 
    if maxData == -1: print("Nothing to print. Done.")
    else:
        print_histogram(inputData,maxData)
    

def print_single_histogram_line(class_number, count, largest_class_number):
    """
    This function is probably the most challenging one in this assignment.
    It will print one correctly indented histogram line as described
    in the assignment instructions. Your job is to call it with
    correct parameters.

    :param class_number: int,
        Expresses which consumption class (1, 2, 3, ...)
        should the histogram line be printed for. The <class_number> is used
        to decide which value range (0-9, 10-99, 100-999, ...) should be
        printed in front of the histogram markers ("*").

    :param count: int,
        How many of the values entered by the user belong to <class_number>.

    :param largest_class_number: int,
        What is the largest class out of all input values
        the user entered. This is needed when deciding the indentations
        for all other histogram lines.  For example, if the largest
        number the user entered was 91827364 (8 digits) the value
        of this paramter should be 8.
    """

    # <range_string> represents the range of the values the line's
    # histogram will represent in the printout.  For example "1000-9999".
    # Uses the functions class_minimum_value and class_maximum_value which
    # have to be defined elsewhere.

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"


    # How many characters will the largest class' range need when printed.
    # For example if the <largest_class_number> is 7, it would print
    # "1000000-9999999" in the beginning of the line and requires 15 characters.
    # This value defines the print width for all the other <range_string>'s.

    largest_width = 2 * largest_class_number + 1


    # Now all the preparations have been done and we can print the
    # histogram line with the correct number of whitespaces in the
    # beginning of the line followed by the correct number of '*'
    # characters. ">" character in the following f-string places
    # <range_string>'s value to the right edge of the output field
    # (filler white spaces will be printed in the beginning).

    print(f"{range_string:>{largest_width}}: {'*' * count}")


def class_minimum_value(classNumber):
    """
    Return the minimum value of a class
    Using formula: min = 10 ** classNumber // 100 * 10

    :param classNumber: int, class number which you want to find the min_value
    :return : int, min_value of the class
    """
    return 10 ** classNumber // 100 * 10

def class_maximum_value(classNumber):
    """
    Return the maximum value of a class
    Using formula: max = 10 ** classNumber - 1

    :param classNumber: int, class number which you want to find the max_value
    :return : int, max_value of the class
    """
    return 10 ** classNumber - 1

def getClass(value):
    """
    Return the class which the value belongs

    :param value: int, non-negative int 
    :return the class of the value: int
    """
    classNumber = 0
    while True:
        if (class_minimum_value(classNumber) <= value
            and value <= class_maximum_value(classNumber)):
            return classNumber
        classNumber += 1

def userInput(prompt):
    """
    This function get inputs of an user, then check if they are non-negative

    :param prompt: string, a sentence to ask user to what is need to type in
    :return : a list of input values
    :return : the greatest value which an user typed in
    (I don't want to use max function to find the max value of a list
    because I want to save time and memory to spend on another loop n
    in case I use the built-in max function) 
    """
    userData = []
    maxVal = -1
    while True:
        val = input(prompt)
        #if a user type 'Enter' (empty line), the program stop collecting user's input
        if val == "": return userData, maxVal

        intVal = int(val)
        if intVal >= 0: 
            userData.append(intVal)
            # (user's input) > oldMax,so newMax = (user's input)
            if intVal > maxVal: maxVal = intVal
        else: 
            print(f"You entered: {intVal}. Enter non-negative numbers only!")

def print_histogram(inputValues, largestValue): 
    """
    Print histogram of values which user typed in

    :param inputValues: a list of input values (each element is a non-negative int)
    :param largestValue: the greatest value of the list 
    
    """
    # initial list of class 
    largestClass = getClass(largestValue)
    classList = [0] * largestClass

    # count the number of values in each class
    for val in inputValues:
        classNum = getClass(val)
        classList[classNum - 1] += 1

    # print final histogram
    for i in range(largestClass):
        print_single_histogram_line(i + 1,classList[i],largestClass)

if __name__ == "__main__":
    main()
