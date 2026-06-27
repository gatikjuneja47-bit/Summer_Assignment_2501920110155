print("Marksheet Generation System")
class Student:
    def __init__(self, name, roll_number, marks, percentage):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        self.percentage = percentage
class MarksheetGenerationSystem:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def display_marksheets(self):
        for student in self.students:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Marks: {student.marks}, Percentage: {student.percentage}")
marksheet_system = MarksheetGenerationSystem()
while True:
    name = input("Enter student name (or 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    roll_number = input("Enter student roll number: ")
    marks = float(input("Enter student marks: "))
    percentage = float(input("Enter student percentage: "))
    new_student = Student(name, roll_number, marks, percentage)
    marksheet_system.add_student(new_student)
marksheet_system.display_marksheets()
print("Exiting Marksheet Generation System")