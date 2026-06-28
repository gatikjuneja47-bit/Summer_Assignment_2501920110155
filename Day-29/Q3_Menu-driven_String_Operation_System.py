print("String Operation System")
string = ""
while True:
    print("1. Insert String")
    print("2. Delete String")
    print("3. Display String")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        n = int(input("Enter number of strings to insert: "))
        for i in range(n):
            s = input("Enter string to insert: ")
            string += s + " "
        print("String inserted")
    elif choice == 2:
        if len(string) > 0:
            s = input("Enter string to delete: ")
            if s in string:
                string = string.replace(s, "", 1)
                print("String deleted")
            else:
                print("String not found")
        else:
            print("String is empty")
    elif choice == 3:
        if len(string) > 0:
            print("String:", string)
        else:
            print("String is empty")
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("Invalid choice")