"""
COMP.CS.100 Ohjelmointi 1 / Programming 1

Body Mass Index template
"""

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()

        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow)

        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        #       the default colour.
        self.__calculate_button = Button(self.__mainwindow, text = 'Calculate BMI',
                command = self.calculate_BMI, background = 'red', foreground = 'white')

        # TODO: Create a Label that will show the decimal value of the BMI
        #      after it has been calculated.
        self.__result_text = Label(self.__mainwindow)

        # TODO: Create a Label that will show a verbal description of the BMI
        #       after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow)

        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow, text = 'Quit', command = self.stop)

        # Title labels
        weightLabel = Label(self.__mainwindow, text = 'Weight (kg)')
        heightLabel = Label(self.__mainwindow, text = 'Height (cm)')
        BMILabel = Label(self.__mainwindow, text = 'BMI: ')
        messageLabel = Label(self.__mainwindow, text = 'Message: ')

        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        weightLabel.grid()
        self.__weight_value.grid()
        heightLabel.grid()
        self.__height_value.grid()
        self.__calculate_button.grid()
        self.__stop_button.grid()
        BMILabel.grid()
        self.__result_text.grid()
        messageLabel.grid()
        self.__explanation_text.grid()

    # TODO: Implement this method.
    def calculate_BMI(self):
        """
        Part b) This method calculates the BMI of the user and
        displays it. First the method will get the values of
        height and weight from the GUI components
        self.__height_value and self.__weight_value.  Then the
        method will calculate the value of the BMI and show it in
        the element self.__result_text.

        Part e) Last, the method will display a verbal
        description of the BMI in the element
        self.__explanation_text.
        """

        invalid = False
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get())

            if weight <= 0 or height <= 0:
                message = "Error: height and weight must be positive."
                self.reset_fields()
                invalid = True

        except ValueError:
            message = "Error: height and weight must be numbers."
            self.reset_fields()
            invalid = True

        if not invalid:
            BMI = weight / (height/100)**2
            if BMI < 18.5:
                message = "You are underweight."
            elif BMI <= 25:
                message = "Your weight is normal."
            else:
                message = "You are overweight."
            
            self.__result_text['text'] = f"{BMI:.2f}"
        self.__explanation_text['text'] = message


    # TODO: Implement this method.
    def reset_fields(self):
        """
        In error situations this method will zeroize the elements
        self.__result_text, self.__height_value, and self.__weight_value.
        """

        self.__result_text.configure(text = "")
        self.__height_value.delete(0, END)
        self.__height_value.insert(0, 0)
        self.__weight_value.delete(0, END)
        self.__weight_value.insert(0, 0)

    def stop(self):
        """
        Ends the execution of the program.
        """

        self.__mainwindow.destroy()

    def start(self):
        """
        Starts the mainloop.
        """
        self.__mainwindow.mainloop()


def main():
    # Notice how the user interface can be created and
    # started separately.  Don't change this arrangement,
    # or automatic tests will fail.
    ui = Userinterface()
    ui.start()


if __name__ == "__main__":
    main()
