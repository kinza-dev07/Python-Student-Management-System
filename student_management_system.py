# Student Management System

students = {}


def add_student():
    roll_no = input("Enter Roll Number: ")

    if roll_no in students:
        print("Student already exists.")
        return

    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    students[roll_no] = {
        "Name": name,
        "Age": age,
        "Course": course
    }

    print("Student added successfully.")


def view_students():
    if not students:
        print("No student record found.")
        return

    print("\nStudent Records")

    for roll_no, details in students.items():
        print(f"\nRoll Number : {roll_no}")
        print(f"Name        : {details['Name']}")
        print(f"Age         : {details['Age']}")
        print(f"Course      : {details['Course']}")


def search_student():
    roll_no = input("Enter Roll Number to Search: ")

    if roll_no in students:
        print("\nStudent Found")
        print("Roll Number :", roll_no)
        print("Name        :", students[roll_no]["Name"])
        print("Age         :", students[roll_no]["Age"])
        print("Course      :", students[roll_no]["Course"])
    else:
        print("Student not found.")


def update_student():
    roll_no = input("Enter Roll Number to Update: ")

    if roll_no in students:
        students[roll_no]["Name"] = input("Enter New Name: ")
        students[roll_no]["Age"] = input("Enter New Age: ")
        students[roll_no]["Course"] = input("Enter New Course: ")

        print("Student record updated successfully.")
    else:
        print("Student not found.")


def delete_student():
    roll_no = input("Enter Roll Number to Delete: ")

    if roll_no in students:
        del students[roll_no]
        print("Student record deleted successfully.")
    else:
        print("Student not found.")


while True:

    print("\nStudent Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter Your Choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Program Closed.")
        break

    else:
        print("Invalid choice. Please try again.")