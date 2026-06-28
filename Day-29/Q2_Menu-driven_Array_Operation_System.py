print("Array Operation System")
array = []
while True:
    print("1. Insert Element")
    print("2. Delete Element")
    print("3. Display Array")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        n = int(input("Enter number of elements to insert: "))
        for i in range(n):
            element = int(input("Enter element to insert: "))
            array.append(element)
        print("Element inserted")
    elif choice == 2:
        if len(array) > 0:
            element = int(input("Enter element to delete: "))
            if element in array:
                array.remove(element)
                print("Element deleted")
            else:
                print("Element not found")
        else:
            print("Array is empty")
    elif choice == 3:
        if len(array) > 0:
            print("Array:", array)
        else:
            print("Array is empty")
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("Invalid choice")