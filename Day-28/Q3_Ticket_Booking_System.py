class Ticket:
    def __init__(self, event_name, ticket_price, quantity):
        self.event_name = event_name
        self.ticket_price = ticket_price
        self.quantity = quantity
class TicketBookingSystem:
    def __init__(self):
        self.tickets = []
    def add_ticket(self, ticket):
        self.tickets.append(ticket)
        print(f"Ticket for '{ticket.event_name}' added to the system.")
    def display_tickets(self):
        if not self.tickets:
            print("No tickets available.")
            return
        print("Available tickets:")
        for ticket in self.tickets:
            print(f"Event: {ticket.event_name}, Price: ${ticket.ticket_price}, Quantity: {ticket.quantity}")

print("Welcome to the Ticket Booking System!")
booking_system = TicketBookingSystem()

while True:
    print("\nMenu:")
    print("1. Add a ticket")
    print("2. Display all tickets")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        n = int(input("How many tickets do you want to add? "))
        for _ in range(n):
            event_name = input("Enter the event name: ")
            ticket_price = float(input("Enter the ticket price: "))
            quantity = int(input("Enter the quantity: "))
            ticket = Ticket(event_name, ticket_price, quantity)
            booking_system.add_ticket(ticket)
    elif choice == '2':
        booking_system.display_tickets()
    elif choice == '3':
        print("Exiting the Ticket Booking System. Thank you")
        break
    else:
        print("Invalid choice. Please try again.")