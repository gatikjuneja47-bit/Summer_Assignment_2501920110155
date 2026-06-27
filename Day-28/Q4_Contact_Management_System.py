print("Contact Management System")
class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email
class ContactManager:
    def __init__(self):
        self.contacts = []
    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added to the system.")
    def display_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        print("Contacts:")
        for contact in self.contacts:
            print(f"Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
contact_manager = ContactManager()
while True:    
    print("\nMenu:")
    print("1. Add a contact")
    print("2. Display all contacts")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")
    if choice == '1':
        n = int(input("How many contacts do you want to add? "))
        for _ in range(n):
            name = input("Enter the contact name: ")
            phone_number = input("Enter the contact phone number: ")
            email = input("Enter the contact email: ")
            contact = Contact(name, phone_number, email)
            contact_manager.add_contact(contact)
    elif choice == '2':
        contact_manager.display_contacts()
    elif choice == '3':
        print("Exiting the Contact Management System. Thank you")
        break
    else:
        print("Invalid choice. Please try again.")