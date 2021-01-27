from tkinter import *

class GUI:
    def __init__(self, title):
        # main window
        self.__main_window = Tk()

        """# text field
        self.__textField = Label(self.__mainWindow, text = title)
        self.__textField.configure(background = "blue", foreground = "white", padx = 30, 
                                    pady = 50, borderwidth = 5, relief = RAISED)
        self.__textField.pack(side = TOP, fill =BOTH, expand = True)

        # Button
        self.__quitButton = Button(self.__mainWindow, text = "Quit",
                                    command = self.quit)
        self.__quitButton.pack(side = BOTTOM)

        self.__mainWindow.mainloop()"""

        # example test
        self.__labelA = Label(self.__main_window, text="A", borderwidth=2, relief=GROOVE)
        self.__labelA.grid(row=1, column=1)

        self.__labelB = Label(self.__main_window, text="B", borderwidth=2, relief=GROOVE)
        self.__labelB.grid(row=1, column=2, sticky=E)

        self.__high_label = Label(self.__main_window, text="high", borderwidth=2, relief=GROOVE)
        self.__high_label.grid(row=0, column=0, rowspan=3, sticky = N+S) 

        self.__wide_label = Label(self.__main_window, text="wide", borderwidth=2, relief=GROOVE)
        self.__wide_label.grid(row=0, column=1, columnspan=2, sticky = E+W)

        self.__quit_button = Button(self.__main_window, text="Quit", command=self.quit)
        self.__quit_button.grid(row=2, column=2)

        self.__main_window.mainloop()

    def quit(self):
        self.__main_window.destroy()

def main():
    myGUI = GUI("Hello World!")

if __name__ == "__main__":
    main()