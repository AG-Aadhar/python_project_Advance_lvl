class Library():
    def __init__(self, file):
        self.bookName = file  # str form
        self.bookNameList = self.bookName.split()  # list form

    def listOfbooks(self):
        print("\t\tBooks available are:-")
        for i in range(len(self.bookNameList)):
            print(f"\t\t {i+1} "+self.bookNameList[i])

    def borrowingBook(self):
        print("\t\tWant to know more about these book ?")
        print("\t\tPress the no. to borrow the book assigned to each book")
        try:
            bookNumber = int(input("\t\t  -->Book no. please: "))
            if bookNumber < 1:
                print("Please enter the assigned no.")
        except:
            print("Invalid input") 
        if bookNumber > 0:           
            removingBookName = (self.bookNameList).pop(bookNumber-1)
            updatedBookList = "\n".join(self.bookNameList)
            with open("listOfBooks.txt", "w") as book:
                showBook = book.write(updatedBookList)
            return removingBookName


class Student():

    def borrowedBook(self, add):
        with open("borrowedBook.txt", "a") as book:
            borrowedBookName = book.write("\n"+add+"\n")

    def returnBook(self, checkName):
        with open("borrowedBook.txt", "r") as book:
            checking = book.read()
            borrowedBookList = checking.split()
            if borrowedBookList == []:
                a = 1
            b = len(borrowedBookList)
            for i in range(b or a):
                if b == 0 and a == 1:
                    print("The book is not belongs to this library \n"
                          + "You can donate this book from donation option in the main menu")
                    break
                elif borrowedBookList[i].lower().replace("\n", "") == checkName.lower().replace(" ", ""):
                    removedBookName = borrowedBookList.pop(i)
                    updatedBorrowedBookList = "\n".join(borrowedBookList)
                    with open("borrowedBook.txt", "w") as book:
                        updating = book.write(updatedBorrowedBookList)
                    with open("listOfBooks.txt", "a") as book:
                        returningBook = book.write("\n"+removedBookName)
                    mainFunc() # 2nd/3rd function call
                    break

    def donateBook(self, newBookName):
        with open("listOfBooks.txt", "a") as book:
            donate = book.write("\n"+newBookName+"\n")
        mainFunc() # 2nd/3rd function call

print("\t\t\t   ***Welcome to your library***")
def mainFunc():
    with open("listOfBooks.txt", "r") as mainBook:
        showingBook = mainBook.read()
    source = Library(showingBook)
    learner = Student()

    while(True):
        print("\t\tMain menu:- \n"
            + "\t\tPress numbers as assigned to each task:) \n"
            + "\t\t  1 for 'books available' \n"
            + "\t\t  2 for 'return the book' \n"
            + "\t\t  3 for 'donate the book' \n"
            + "\t\t  0 for 'exit'")
        try:
            userAction = int(input("\t\t  -->main menu "))
            if userAction > 3:
                print("Please enter the assigned no.")
        except:
            print("Invalid input")
        else:
            if userAction == 1:
                source.listOfbooks()
                value = source.borrowingBook()
                if value != None:
                    learner.borrowedBook(value)
            if userAction == 2:
                try:
                    returningBookName = input("Book name please: ")
                    value2 = learner.returnBook(returningBookName)
                except:
                    print("Invalid input")
            if userAction == 3:
                try:
                    donatingBookName = input("Book name please: ")
                    learner.donateBook(donatingBookName)
                except:
                    print("Invalid input")
            if userAction == 0:
                print("\t\t\t\tSee you soon budy, have an awesome day:)")
                break
mainFunc() # first function call