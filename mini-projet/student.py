class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = []

def add_student():
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    s = Student(name, marks)
    students.append(s)
    print("Student added!")

def show_students():
    if not students:
        print("No students found")
    else:
        for s in students:
            print(s.name, s.marks)

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        show_students()
    elif choice == '3':
        break
    else:
        print("Invalid choice")
