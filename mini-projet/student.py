class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        s = Student(name, marks)
        students.append(s)
        print("Student added!")

    elif choice == "2":
        for s in students:
            print(s.name, s.marks)

    elif choice == "3":
        break

    else:
        print("Invalid choice")
