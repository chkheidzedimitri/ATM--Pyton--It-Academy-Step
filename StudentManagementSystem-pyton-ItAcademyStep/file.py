class Student:
    def __init__(self, name, roll_number, grade):
        self.name = name
        self.roll_number = roll_number
        self.grade = grade

def add_student(students):
    print("\nAdding a new student:")
    name = input("Enter student's name: ")
    roll_number = int(input("Enter student's roll number: "))
    
    # Check if the roll number already exists
    for student in students:
        if student.roll_number == roll_number:
            print("A student with the same roll number already exists. Adding a student with the same roll number is not allowed.")
            return
    
    grade = int(input("Enter student's grade (1-10): "))
    while grade < 1 or grade > 10:
        grade = int(input("Invalid input. Please enter a valid grade (1-10): "))

    new_student = Student(name, roll_number, grade)
    students.append(new_student)
    print("\nStudent added successfully!")

def view_all_students(students):
    print("\nAll Students:")
    for student in students:
        print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")

def search_student(students):
    roll_number = int(input("\nEnter roll number to search: "))
    found = False
    for student in students:
        if student.roll_number == roll_number:
            print(f"Name: {student.name}, Roll Number: {student.roll_number}, Grade: {student.grade}")
            found = True
            break
    if not found:
        print("Student not found.")

def update_grade(students):
    roll_number = int(input("\nEnter roll number of the student whose grade you want to update: "))
    found = False
    for student in students:
        if student.roll_number == roll_number:
            new_grade = int(input("Enter new grade (1-10): "))
            while new_grade < 1 or new_grade > 10:
                new_grade = int(input("Invalid input. Please enter a valid grade (1-10): "))
            student.grade = new_grade
            print("\nGrade updated successfully!")
            found = True
            break
    if not found:
        print("Student not found.")

def delete_student(students):
    roll_number = int(input("\nEnter roll number of the student you want to delete: "))
    for student in students:
        if student.roll_number == roll_number:
            students.remove(student)
            print("Student deleted successfully!")
            return
    print("Student not found.")

def main():
    students = []

    while True:
        print("\nStudent Management System")
        print("1. Add a new student")
        print("2. View all students")
        print("3. Search for a student by roll number")
        print("4. Update a student's grade")
        print("5. Delete a student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_student(students)
        elif choice == '2':
            view_all_students(students)
        elif choice == '3':
            search_student(students)
        elif choice == '4':
            update_grade(students)
        elif choice == '5':
            delete_student(students)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
