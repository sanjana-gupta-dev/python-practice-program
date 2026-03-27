import json

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# Load data
try:
    with open("students.json", "r") as f:
        students = json.load(f)
except:
    students = []

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter name: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "marks": marks})
        print("Student added!")

    elif choice == "2":
        for s in students:
            print(s["name"], s["marks"])

    elif choice == "3":
        name = input("Enter name to search: ")
        for s in students:
            if s["name"] == name:
                print("Found:", s["name"], s["marks"])

    elif choice == "4":
        name = input("Enter name to delete: ")
        for s in students:
            if s["name"] == name:
                students.remove(s)
                print("Deleted!")
                break

    elif choice == "5":
        name = input("Enter name to update: ")
        for s in students:
            if s["name"] == name:
                s["marks"] = int(input("Enter new marks: "))
                print("Updated!")
                break

    elif choice == "6":
        with open("students.json", "w") as f:
            json.dump(students, f)
        break

    else:
        print("Invalid choice")
