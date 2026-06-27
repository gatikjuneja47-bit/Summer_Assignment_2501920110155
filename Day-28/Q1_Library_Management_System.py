class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")
    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print(f"Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}")
print("Welcome to the Library Management System!")
library = Library()
while True:
    print("\nMenu:")
    print("1. Add a book")
    print("2. Display all books")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        n = int(input("How many books do you want to add? "))
        for _ in range(n):
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            isbn = input("Enter the book ISBN: ")
            book = Book(title, author, isbn)
            library.add_book(book)
    elif choice == '2':
        library.display_books()
    elif choice == '3':
        print("Exiting the Library Management System. Thank you")
        break
    else:
        print("Invalid choice. Please try again.")