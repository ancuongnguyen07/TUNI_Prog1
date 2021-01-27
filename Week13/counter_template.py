"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id: 050358715
Name:       An Cuong Nguyen
Email:      cuong.nguyen@tuni.fi

Code template for counter program.
"""

from tkinter import *


class Counter:
    def __init__(self):
        # TODO: You have to creater one label and four buttons and store
        #       them in the following attributes:
        #
        #       self.__current_value    # Label displaying the current value of the counter.
        #       self.__reset_button     # Button which resets counter to zero.
        #       self.__increase_button  # Button which increases the value of the counter by one.
        #       self.__decrease_button  # Button which decreases the value of the counter by one.
        #       self.__quit_button      # Button which quits the program.
        #
        #       Make sure you name the components exactly as shown above,
        #       otherwise the automated tests will fail.
        self.__mainWindow = Tk()
        self.__counter = 0

        self.__current_value = Label(self.__mainWindow, text = '0', borderwidth = 5,
                                    relief = GROOVE)
        self.__current_value.grid(row = 0, column = 0, columnspan = 4, sticky = N+W+E)

        self.__increase_button = Button(self.__mainWindow, text = "Increase", relief = GROOVE,
                                    command = self.increase)
        self.__increase_button.grid(row = 1, column = 0, sticky = W+N)

        self.__decrease_button = Button(self.__mainWindow, text = "Decrease", relief = GROOVE,
                                    command = self.decrease)
        self.__decrease_button.grid(row = 1, column = 1, sticky = W+N)

        self.__reset_button  = Button(self.__mainWindow, text = "Reset", relief = GROOVE,
                                command = self.reset)
        self.__reset_button.grid(row = 1, column = 2, sticky = W+N)

        self.__quit_button = Button(self.__mainWindow, text = "Quit", relief = GROOVE,
                                command = self.quit)
        self.__quit_button.grid(row = 1, column = 3, sticky = W+N)

        self.__mainWindow.mainloop()

    # TODO: Implement the rest of the needed methods here.

    def increase(self):
        self.__counter += 1
        self.__current_value.configure(text = str(self.__counter))

    def decrease(self):
        #if self.__counter > 0:
        self.__counter -= 1
        self.__current_value.configure(text = str(self.__counter))

    def reset(self):
        self.__counter = 0 
        self.__current_value.configure(text = str(self.__counter))

    def quit(self):
        self.__mainWindow.destroy()


def main():
    # There is no need to modify the main function.
    # As a matter of fact, automated tests ignore main
    # once again.

    Counter()


if __name__ == "__main__":
    main()
