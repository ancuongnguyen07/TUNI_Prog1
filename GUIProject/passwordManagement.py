from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import os

WIDTH = 400
HEIGHT = 200
MAIN_WINDOW_SIZE = f"{WIDTH}x{HEIGHT}"
BACK_BUTTON_IMAGE_PATH = "back_arrow.png"
ADD_BUTTON_IMAGE_PATH = "add_icon.png"
DELETE_BUTTON_IMAGE_PATH = "delete_icon.png"
MINIMUM_CHARACTERS = 8 # min number of letters for 'password'
# the path which the script file is operated
BASE_PATH = os.path.dirname(os.path.realpath(__file__)) 
USER_FOLDER = "users"

class Account:
    """
    Account object contains 3 attributes: username, password, title
    Is used to manage accounts
    """
    def __init__(self, username, password, title):
        self.__username = username
        self.__password = password
        self.__title = title

    def setUsername(self, newUsername):
        self.__username = newUsername

    def setPassword(self, newPassword):
        self.__password = newPassword

    def setTitle(self, newTitle):
        self.__title = newTitle

    def getTitle(self):
        return self.__title

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

class User:
    """
    User object contains 3 attributes: username, password, accountList
    Which 'accountList' is a list of account objects
    """
    def __init__(self, username, password, accountList=[]):
        self.__accountList = accountList
        self.__username = username
        self.__password = password

    def getUsername(self):
        return self.__username

    def getPassword(self):
        return self.__password

    def getAccountList(self):
        return self.__accountList

    def addAccount(self, newAccount):
        self.__accountList.append(newAccount)

class GUI:
    """
    GUI object is the main object which operate the GUI program
    """
    # missing a list of users
    def __init__(self):
        # load user data from files
        self.__userList = self.readData()
        # configure main window
        
        self.__mainWindow = Tk()
        self.__mainWindow.title("Password Manager")
        self.__mainWindow.geometry(MAIN_WINDOW_SIZE)
        self.__mainWindow.resizable(False,False)

        # set up buttons
        self.__backButtonImage = PhotoImage(file=BACK_BUTTON_IMAGE_PATH)
        self.__addButtonImage = PhotoImage(file=ADD_BUTTON_IMAGE_PATH)
        self.__deleteButtonImage = PhotoImage(file=DELETE_BUTTON_IMAGE_PATH)

        # set up frames
        self.__frontPageFrame = Frame(self.__mainWindow)
        self.__listAccountsFrame = Frame(self.__mainWindow)
        self.__signupFrame = Frame(self.__mainWindow)
        self.__updateAccountFrame = Frame(self.__mainWindow) 
        self.__addAccountFrame = Frame(self.__mainWindow)

        # initialize the front page frame
        self.frontPageFrame()

        self.__mainWindow.mainloop()

    def frontPageFrame(self):
        """
        Initialize the front page frame
        containing function buttons: login, sign up
        """
        root = self.__frontPageFrame
        self.showFrame(root)

        # initialize components
        labels, entries = self.u_pInitialize(root, mode=1, secret=1,users=self.__userList)
        signUpButton = Button(root, command=self.signUp, text='Sign up')
        loginButton = Button(root, command=self.login, text='Log in')

        # put components on grid
        # element 0 for 'username', element 1 for 'password'
        lastRow = self.arrangeLabelsEntries(labels, entries)
        signUpButton.grid(row=lastRow + 1, column=2)
        loginButton.grid(row=lastRow + 1, column=3)

        # active components means that current components which are displayed
        self.setActiveEntries(entries)
        self.setActiveFrame(self.__frontPageFrame)

    def findUser(self,username):
        """
        Find a User object by parameter: username

        parameter: username-string
        return: User object which matches the 'username'
        """
        for u in self.__userList:
            if u.getUsername() == username:
                return u

    def createUserNameList(self, userList):
        """
        Create username list from a list of users
        """
        usernameList = []
    
        for u in userList:
            usernameList.append(u.getUsername())
        return usernameList

    def u_pInitialize(self, frame, mode=0, secret=1,users = []):
        """
        method which initializes 'username', 'password' label, entry
        which is used often in the program

        mode = 1: create 'username' entry with combobox
        mode = 0: create 'username' normal entry

        secret = 1: create 'password' entry filled with '*'
        secret = 0: create 'password' entry filled with normal characters
        """

        userNameLabel = Label(frame, text='username')
        passwordLabel = Label(frame, text='password')
        userNameList = self.createUserNameList(users)

        if mode == 1:
            userNameEntry = ttk.Combobox(frame, values = userNameList, state='readonly')
        else:
            userNameEntry = Entry(frame)

        if secret == 1:
            passwordEntry = Entry(frame, show='*')
        else:
            passwordEntry = Entry(frame)

        return [userNameLabel, passwordLabel], [userNameEntry, passwordEntry]

    def arrangeLabelsEntries(self, labels, entries, col=2, colNext=3):
        """
        put labels and entries on grid for multiple frames
        len(labels) = len(entries) always

        return: the row of the last label-entry pair
        """
        i = 0
        while i < len(labels):
            labels[i].grid(row=i+2, column=col)
            entries[i].grid(row=i+2, column=colNext)
            i += 1
        return i+2

    def listAccountsFrame(self):
        """
        Initilize frame
        A page displays a list of accounts of the user
        containing function buttons: select, log out
        """
        root = self.__listAccountsFrame
        self.setActiveFrame(root)
        #root.config(width=WIDTH, height=HEIGHT)
        self.showFrame(root)

        # initialize components
        scroller = Scrollbar(root, orient='vertical')
        addButton = Button(root, image=self.__addButtonImage, command=self.addAccountFrame)
        accountList = self.__activeUser.getAccountList()
        helloLabel = Label(root, text=f"Hello {self.__activeUser.getUsername()}!")

        listAccountBox = self.initAccountListBox(accountList, root)
        self.__activeListAccountBox = listAccountBox
        listAccountBox.config(yscrollcommand=scroller.set)
        scroller.config(command = listAccountBox.yview)
        selectButton = Button(root, text='Select', command=self.updateAccountFrame)
        logoutButton = Button(root, text='Logout', command=self.logout)

        # put components on grid
        helloLabel.pack(side=TOP)     
        addButton.pack(side=TOP) 
        scroller.pack(side=RIGHT, fill=Y)
        listAccountBox.pack()
        selectButton.pack()
        logoutButton.pack()

    def initAccountListBox(self, accountList, frame):
        """
        initialize listbox containing accounts of the active user
        """
        listBox = Listbox(frame, height=5)
        for i in range(len(accountList)):
            listBox.insert(i, accountList[i].getTitle())
        return listBox

    def logout(self):
        """
        This method is operated when user press 'log out' button
        """
        self.saveDataUser(self.__activeUser)
        self.returnFrontPage()

    def addAccountFrame(self):
        """
        Initialize the frame which has a function: add account
        """
        self.clearFrame(self.__activeFrame)
        root = self.__addAccountFrame
        self.setActiveFrame(root)
        self.showFrame(root)

        # set up components
        labels, entries = self.u_pInitialize(root,secret=0)
        labels.append(Label(root, text='Title'))
        entries.append(Entry(root))
        doneButton = Button(root, text='Done', command=lambda : self.addAccount(entries))
        backButton = Button(root, image=self.__backButtonImage, \
                        command=self.returnListAccountsFrame)

        # put components on grid
        lastRow = self.arrangeLabelsEntries(labels, entries)
        doneButton.grid(row=lastRow+1, column=3)
        backButton.grid(row=lastRow+1, column=2)

    def textListEntry(self, entries):
        """
        return a list of text (values of entry) from a list of entries
        """
        textList = []
        for en in entries:
            textList.append(en.get())
        return textList

    def addAccount(self, entries):
        """
        This method operates the 'add account' function when
        user press the '+' button
        """
        username, password, title = self.textListEntry(entries) 
        # when one of 3 entries is emptied
        if self.isEmpty(username) or self.isEmpty(password) or self.isEmpty(title):
            self.showError("All textbox must be filled")
            return
        newAccount = Account(username, password, title)
        self.__activeUser.addAccount(newAccount)
        self.showInfo("Added account successfully")
        # return to the frame containing a list of accounts
        self.returnListAccountsFrame()

    def isEmpty(self, mess):
        return mess == ""

    def updateAccountFrame(self):
        """
        initialize the frame which has a function: update/edit account's info
        """
        # get selected account
        activeIndexTuple = self.__activeListAccountBox.curselection()
        
        if len(activeIndexTuple) == 0:
            # no one is selected
            self.showError("No account is selected")
            return
        
        activeIndex = activeIndexTuple[0] # index of the selected account
        self.clearFrame(self.__activeFrame)
        root = self.__updateAccountFrame
        self.showFrame(root)
        self.setActiveFrame(root)
        self.setActiveAccount(self.__activeUser.getAccountList()[activeIndex])
        
        # set up components
        labels, entries = self.u_pInitialize(root, secret=0)
        entries[0].insert(0,self.__activeAccount.getUsername())
        entries[1].insert(0,self.__activeAccount.getPassword())
        doneButton = Button(root, text='Done', \
            command=lambda : self.updateAccount(entries))
        deleteButton = Button(root, image=self.__deleteButtonImage,\
                    command=lambda : self.deleteAccount(activeIndex))

        # put components on grid
        lastRow = self.arrangeLabelsEntries(labels,entries)
        doneButton.grid(row=lastRow + 1, column=2)
        deleteButton.grid(row=lastRow + 1, column=3)

    def setActiveUser(self, user):
        self.__activeUser = user

    def setActiveFrame(self, frame):
        self.__activeFrame = frame

    def setActiveEntries(self, entries):
        self.__activeEntries = entries

    def setActiveAccount(self, account):
        self.__activeAccount = account

    def updateAccount(self, entries):
        """
        This method check if account's info is changed
        and then saves all changes
        """
        newUsername, newPassword = self.textListEntry(entries)
        activeAccount = self.__activeAccount
        if newUsername != activeAccount.getUsername():
            activeAccount.setUsername(newUsername)
        if newPassword != activeAccount.getPassword():
            activeAccount.setPassword(newPassword)
        # return to the frame containing a list of accounts
        self.returnListAccountsFrame()

    def deleteAccount(self, index):
        # ask again to make sure that an user don't press the button by mistake
        res = self.showYesNoQuestion("Delete account", \
            "Do you really want to delete this account")
        if res == 'yes':
            accounts = self.__activeUser.getAccountList()
            del accounts[index]
            self.returnListAccountsFrame()

    def returnFrontPage(self):
        """
        return to the front frame (begining frame)
        """
        self.clearFrame(self.__activeFrame)
        self.__activeFrame = self.__frontPageFrame
        self.frontPageFrame()

    def returnListAccountsFrame(self):
        """
        return to the frame containing a list of accounts
        """
        self.clearFrame(self.__activeFrame)
        self.__activeFrame = self.__listAccountsFrame
        self.listAccountsFrame()

    def showFrame(self, frame):
        frame.pack(expand = True, fill=BOTH)

    def clearFrame(self, frame): 
        # destroy all widgets of the frame      
        for widget in frame.winfo_children():
            widget.destroy()
        # hide the frame
        frame.pack_forget()

    def signUp(self):
        """
        Clear the UI and move to sign-up page
        Initialize sign-up frame
        """
        self.clearFrame(self.__frontPageFrame)
        root = self.__signupFrame
        self.showFrame(root)
        self.setActiveFrame(self.__signupFrame) 

        # initialize components
        labels, entries = self.u_pInitialize(root)
        labels.append(Label(root, text="Confirm password"))
        entries.append(Entry(root, show='*'))

        # missing command for 'doneButton'
        doneButton = Button(root, text='Done', command=self.processSignup)
        backButton = Button(root, image=self.__backButtonImage, command=self.returnFrontPage)

        # put components on grid
        lastRow = self.arrangeLabelsEntries(labels, entries)
        doneButton.grid(row=lastRow + 1, column=3)
        backButton.grid(row=0,column=0, sticky=N+W)

        self.setActiveEntries(entries)
        self.__activeEntries[0].bind("<FocusOut>", self.cUE_Event)
        self.__activeEntries[1].bind("<FocusOut>", self.cPL_Event)
        self.__activeEntries[2].bind("<FocusOut>", self.cMCP_Event)

    def login(self):
        """
        Clear the UI and move to account manager page
        Initialize account manager frame
        """
        username = self.__activeEntries[0].get()
        password = self.__activeEntries[1].get()
        
        if self.isPasswordValid(username, password):
            self.clearFrame(self.__frontPageFrame)

            self.setActiveUser(self.findUser(username)) 
            self.listAccountsFrame()
        else:
            self.showError("The password is not correct")


    def showError(self, mess):
        messagebox.showerror(title='Error', message=mess)

    def showYesNoQuestion(self, title, mess):
        response = messagebox.askquestion(title, mess)
        return response

    def checkUsernameEntry(self):
        """
        Check 'username' entry's value, in sign-up page, is exist or not
        and if the entry is empty or not
        """
        # self.__activeEntries has 3 elements at the moment
        username = self.__activeEntries[0].get()
        if len(username) == 0:
            self.showError("The username must not be empty")
            return False
        if self.isUsernameExist(username):
            self.showError("The username is already exist")
            return False
        return True

    def cUE_Event(self, event):
        """
        Check 'username' entry in sign-up page is exist or not 
        with 'event'
        """
        self.checkUsernameEntry()

    def checkPasswordLength(self):
        """
        Check if 'password' (password for program's account) entry contains 
        at least a minimum number of characters in sign-up page
        """
        if len(self.__activeEntries[1].get()) < MINIMUM_CHARACTERS:
            self.showError("The password must contains at least "
                            f"{MINIMUM_CHARACTERS} characters")
            return False
        return True

    def cPL_Event(self, event):
        """
        Check if 'password' (password for program's account) entry contains 
        at least a minimum number of characters in sign-up page
        with 'event'
        """
        self.checkPasswordLength()

    def checkMatchedConfirmPass(self):
        """
        Check if 'confirm password' matches with 'password'
        in sign-up page
        """
        password = self.__activeEntries[1].get()
        confirmPassword = self.__activeEntries[2].get()
        if password != confirmPassword:
            self.showError("CONFIRM PASSWORD and PASSWORD doesn't match")
            return False
        return True

    def cMCP_Event(self, event):
        """
        Check if 'confirm password' matches with 'password'
        in sign-up page with 'event'
        """
        self.checkMatchedConfirmPass()

    def processSignup(self):
        """
        Check all restrictions of entries which used in sign-up frame
        then save a new user to the user list
        """
        if not self.checkUsernameEntry():
            return
        if not self.checkPasswordLength():
            return
        if not self.checkMatchedConfirmPass():
            return
        # sign-up successfully
        username = self.__activeEntries[0].get()
        password = self.__activeEntries[1].get()
        newUser = User(username, password)
        self.saveUser(newUser)
        self.setActiveUser(newUser)
        self.showInfo("Sign-up successfully")

        # return to the frame containing the list of accounts
        self.returnListAccountsFrame()
    

    def isUsernameExist(self, username):
        return self.findUser(username) != None

    def isPasswordValid(self, username, password):
        user = self.findUser(username)
        if self.isUsernameExist(username):
            return password == user.getPassword()

    def saveUser(self, user):
        self.__userList.append(user)

    def showInfo(self, mess):
        messagebox.showinfo(title="Notice", message=mess)

    def readData(self):
        """
        read a file of a particular user then convert its information
        into data structures
        """
        try:
            os.chdir(BASE_PATH + '\\' + USER_FOLDER)
            userList = []
            haveFiles = False # flag to check if there is any user files
            for fileName in os.listdir():
                haveFiles = True
                userFile = open(fileName, 'r')
                username = userFile.readline().strip()
                password = userFile.readline().strip()
                accountList = []
                numOfAccs = int(userFile.readline().strip())
                for i in range(numOfAccs):
                    u, p, t = userFile.readline().split(',')
                    accountList.append(Account(u,p,t))
                userList.append(User(username,password,accountList))
            if haveFiles:
                userFile.close()
            os.chdir(BASE_PATH)
        except IOError:
            self.showError("Cannot read file!!!")
            return
        return userList

    def saveDataUser(self,user):
        """
        save user's data and his/her accounts information into a file
        """
        try:
            os.chdir(BASE_PATH + '\\' + USER_FOLDER)
            fileName = user.getUsername()+'.txt'
            userFile = open(fileName, 'w')
            print(user.getUsername(), file=userFile)
            print(user.getPassword(), file=userFile)
            accountList = user.getAccountList()
            print(str(len(accountList)), file=userFile)
            for acc in accountList:
                print(acc.getUsername().strip()+','+acc.getPassword().strip()+','+acc.getTitle().strip(), file=userFile)
            userFile.close()
            os.chdir(BASE_PATH)
        except IOError:
            self.showError("Cannot write data!!!")
            return


"""
-----------------------------FILE STRUCTURE
USERNAME
PASSWORD
NUMBER OF ACCOUNT
[ACCOUNT LIST]
-----------------e------------ACCOUNT LIST LINE STRUCTURE
USERNAME,PASSWORD,TITLE
"""



def main():
    container = GUI()
    

if __name__ == "__main__":
    main()