from app.student import Student
from app.student_manager import StudentManager
from app.file_handler import FileHandler


DATA_FILE = "data/students.json"


def get_student_details():
    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        raise ValueError("Student ID cannot be empty.")

    name = input("Enter Student Name: ").strip()

    if not name:
        raise ValueError("Student name cannot be empty.")

    age = int(input("Enter Age: "))

    if age <= 0:
        raise ValueError("Age must be greater than zero.")

    course = input("Enter Course: ").strip()

    if not course:
        raise ValueError("Course cannot be empty.")

    marks = {}

    subjects = ["Python", "Database", "Web Development"]

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))

        if mark < 0 or mark > 100:
            raise ValueError("Marks must be between 0 and 100.")

        marks[subject] = mark

    return Student(
        student_id,
        name,
        age,
        course,
        marks
    )


def add_student(manager):
    try:
        student = get_student_details()

        manager.add_student(student)

        print("\nStudent added successfully.")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


def search_student(manager):
    try:
        student_id = input("Enter Student ID to search: ").strip()

        if not student_id:
            raise ValueError("Student ID cannot be empty.")

        manager.search_student(student_id)

    except ValueError as error:
        print(f"\nError: {error}")


def update_student(manager):
    try:
        student_id = input("Enter Student ID to update: ").strip()

        if not manager.find_student(student_id):
            raise ValueError("Student not found.")

        name = input("Enter new name: ").strip()

        if not name:
            raise ValueError("Name cannot be empty.")

        age = int(input("Enter new age: "))

        if age <= 0:
            raise ValueError("Age must be greater than zero.")

        course = input("Enter new course: ").strip()

        if not course:
            raise ValueError("Course cannot be empty.")

        manager.update_student(
            student_id,
            name,
            age,
            course
        )

        print("\nStudent updated successfully.")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


def delete_student(manager):
    try:
        student_id = input("Enter Student ID to delete: ").strip()

        manager.delete_student(student_id)

        print("\nStudent deleted successfully.")

    except ValueError as error:
        print(f"\nError: {error}")

    except Exception as error:
        print(f"\nUnexpected error: {error}")


def show_menu():
    print("\n================================")
    print("     STUDENT MANAGEMENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. View All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
    print("================================")


def main():

    file_handler = FileHandler(DATA_FILE)

    manager = StudentManager(file_handler)

    while True:

        show_menu()

        try:
            choice = input("Enter your choice: ").strip()

            if choice == "1":
                add_student(manager)

            elif choice == "2":
                manager.display_all_students()

            elif choice == "3":
                search_student(manager)

            elif choice == "4":
                update_student(manager)

            elif choice == "5":
                delete_student(manager)

            elif choice == "6":
                print("\nThank you for using Student Management System.")
                break

            else:
                print("\nInvalid choice. Please select 1-6.")

        except KeyboardInterrupt:
            print("\n\nApplication stopped by user.")
            break

        except Exception as error:
            print(f"\nUnexpected error: {error}")


if __name__ == "__main__":
    main()