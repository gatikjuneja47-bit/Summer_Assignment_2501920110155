print("Student Record Management System")
class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
class StudentRecordManagementSystem:
    def __init__(self):
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def display_students(self):
        for student in self.students:
            print(f"Name: {student.name}, Age: {student.age}, Grade: {student.grade}")
student = StudentRecordManagementSystem()
while True:
    name = input("Enter student name (or 'exit' to stop): ")
    if name.lower() == 'exit':
        break
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    new_student = Student(name, age, grade)
    student.add_student(new_student)
student.display_students()
print("Exiting Student Record Management System")