print("Student Record System Using Array and String")
array = []
string = ""
while True:
    print("1. Add Student Record")
    print("2. Delete Student Record")
    print("3. Display Student Records")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        n = int(input("Enter the number of students to add: "))
        for _ in range(n):
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            grade = input("Enter student grade: ")
            record = f"{name}, {age}, {grade}"
            array.append(record)
            string += record + "\n"
        print(f"{n} student records have been added")
    elif choice == '2':
        name = input("Enter the name of the student to delete: ")
        record_to_delete = None
        for record in array:
            if name in record:
                record_to_delete = record
                break
        if record_to_delete:
            array.remove(record_to_delete)
            string = ""
            for record in array:
                string += record + "\n"
            print(f"Student record for {name} has been deleted")
        else:
            print(f"No student found with the name {name}")
    elif choice == '3':
        print("Student Records:")
        for record in array:
            print(record)
    elif choice == '4':
        print("Exiting the system")
        print("Thank you")
        break
    else:
        print("Invalid choice")