print("Salary Management System")
class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
class SalaryManagementSystem:
    def __init__(self):
        self.employees = []
    def add_employee(self, employee):
        self.employees.append(employee)
    def display_employees(self):
        for employee in self.employees:
            print(f"Name: {employee.name}, Position: {employee.position}, Salary: {employee.salary}")
employee = SalaryManagementSystem()
while True:
    name = input("Enter employee name (or 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    position = input("Enter employee position: ")
    salary = float(input("Enter employee salary: "))
    new_employee = Employee(name, position, salary)
    employee.add_employee(new_employee)
employee.display_employees()
print("Exiting Salary Management System")