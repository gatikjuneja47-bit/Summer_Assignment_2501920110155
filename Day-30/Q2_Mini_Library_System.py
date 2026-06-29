print("Library Management System")
book = {}
while True:
    print("1. Add Books Details")
    print("2. Delete Books")
    print("3. Display Books Info")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        n = int(input("Enter number of books to add: "))
        for i in range(n):
            item = input("Enter book name: ")
            author = input("Enter author name: ")
            quantity = int(input("Enter quantity: "))
            book[item] = quantity
        print("Item added")
    elif choice == 2:
        item = input("Enter book name to remove: ")
        if item in book:
            del  book[item]
            print("Book removed")
        else:
            print("Book not found")
    elif choice == 3:
        if book:
            for item in book.items():
                print(f"{item}{author}")
        else:
            print("Data is empty")
    elif choice == 4:
        print("Exiting")
        print("Thank you")
        break
    else:
        print("Invalid choice")