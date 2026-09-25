from app.student import Student


def test_student_average():

    marks = {
        "Python": 80,
        "Database": 70,
        "Web Development": 90
    }

    student = Student(
        "S101",
        "Rahul",
        21,
        "Computer Science",
        marks
    )

    assert student.calculate_average() == 80


def test_student_grade():

    marks = {
        "Python": 90,
        "Database": 90,
        "Web Development": 90
    }

    student = Student(
        "S102",
        "Anil",
        22,
        "Computer Science",
        marks
    )

    assert student.calculate_grade() == "A+"