print("Employee Management System")
employee = {}
while True:
    print("1. Add employee details")
    print("2. Delete employee details")
    print("3. Display employee details")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        n = int(input("Enter number of employee to add: "))
        for i in range(n):
            name = input("Enter employee name: ")
            age = input("Enter age: ")
            salary = int(input("Enter salary: "))
            id = input("Enter employee id: ")
            employee[name] = age, salary, id
        print("Detail added")
    elif choice == 2:
        name = input("Enter employee name to remove: ")
        if name in employee:
            del employee[name]
            print("Employee removed")
        else:
            print("Employee not found")
    elif choice == 3:
        if employee:
            for name in employee.items():
                print(f"{name}")
        else:
            print("Data is empty")
    elif choice == 4:
        print("Exiting")
        print("Thank you")
        break
    else:
        print("Invalid choice")