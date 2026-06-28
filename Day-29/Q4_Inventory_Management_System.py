print("Inventory Management System")
inventory = {}
while True:
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Display Inventory")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        n = int(input("Enter number of items to add: "))
        for i in range(n):
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory[item] = quantity
        print("Item added")
    elif choice == 2:
        item = input("Enter item name to remove: ")
        if item in inventory:
            del inventory[item]
            print("Item removed")
        else:
            print("Item not found")
    elif choice == 3:
        if inventory:
            for item, quantity in inventory.items():
                print(f"{item}: {quantity}")
        else:
            print("Inventory is empty")
    elif choice == 4:
        print("Exiting")
        break
    else:
        print("Invalid choice")