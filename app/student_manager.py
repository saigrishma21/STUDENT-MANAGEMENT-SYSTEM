from app.student import Student


class StudentManager:

    def __init__(self, file_handler):
        self.file_handler = file_handler
        self.students = []

        self.load_data()

    def load_data(self):
        data = self.file_handler.load_students()

        self.students = [
            Student.from_dict(student)
            for student in data
        ]

    def save_data(self):
        data = [
            student.to_dict()
            for student in self.students
        ]

        self.file_handler.save_students(data)

    def add_student(self, student):
        if self.find_student(student.student_id):
            raise ValueError("Student ID already exists.")

        self.students.append(student)
        self.save_data()

    def find_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student

        return None

    def display_all_students(self):
        if not self.students:
            print("\nNo student records found.")
            return

        for student in self.students:
            student.display_student()

    def update_student(self, student_id, name, age, course):
        student = self.find_student(student_id)

        if not student:
            raise ValueError("Student not found.")

        student.name = name
        student.age = age
        student.course = course

        self.save_data()

    def delete_student(self, student_id):
        student = self.find_student(student_id)

        if not student:
            raise ValueError("Student not found.")

        self.students.remove(student)
        self.save_data()

    def search_student(self, student_id):
        student = self.find_student(student_id)

        if student:
            student.display_student()
        else:
            print("\nStudent not found.")