class Library:

    def __init__(self,list_of_books, name):
        self.list_of_books = list_of_books
        self.name = name
        self.lendDict = {}
    
    def displayBooks(self):
        print("We have the following books in our library", {self.name})
        for book in self.booksLists:
            print(book)

    def lendBook(self, user, book):
        if book not in self.booksList:
            print("Sorry, we dont have that book.")
        elif book in self.bookList:
            print(f"The book is already being used by", {self.lendDict[book]})
        else:
            self.lendDict[book] = user
            print(
                "Lender-Book database has been updated. You can take the book now."
            )
        
    def addBook(self,book):
        self.bookList.append(book)
        print(f"{book} has been added to the book list.")

    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned")
        else:
            print("That book wasn't borrowed from us.")
    

books = Library([
        'Python', 'Rich Dad and Son', 'Harry potter', 'C++ Basics',
        'Algorithms by CLRS'
    ], "Let's Upkill")
user_name = input("Welcome to our library! Please enter your name:")

while True:
    print(f"\nHello {user_name}, welcome to the {books.name} library. Please choose an option:")
    print("1. Display  Books\n2. lend a Book\n3. Add a Book\n4. Return a Book\n5. Quit")
    user_choice = input("Enter your choice to continue")
    
    if user_choice not in ['1', '2', '3', '4', '5']:
        print("Please enter a valid option:")
        continue

    if user_choice == '1':
        books.displayBooks()
    elif user_choice == '2':
        book = input("Enter the name of the book you want to lend:")
        books.lendBook(user_name, book)
    elif user_choice == '3':
        book = input("Enter the name of the book you want to add:")
        books.addBook(book)
    elif user_choice == '4':
        book = input("Enter the name of the book you want to return:")
        books.returnBook(book)
    elif user_choice == '5':
        print(f"Thank you for using this library, {user_name}. Goodbye and See you next time!")
        break

    print("q to quit and c to continue")
    user_choice2 = ""
    while(user_choice2!="c" and user_choice2!="q"):
        user_choice2=input()
        if user_choice2=="q":
            exit()
    
        elif user_choice2=="c":
            continue
    