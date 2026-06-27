print("Employee Management System")
class Employee:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position
class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def display_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Age: {employee.age}, Position: {employee.position}")
employee_system = EmployeeManagementSystem()
while True:    
    name = input("Enter employee name (or 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")
    new_employee = Employee(name, age, position)
    employee_system.add_employee(new_employee)
employee_system.display_employees()
print("Exiting Employee Management System")
