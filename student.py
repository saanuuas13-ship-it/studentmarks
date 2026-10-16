
def calculate_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


def display_result(name, marks):
    grade = calculate_grade(marks)

    print("Student Name:", name)
    print("Marks:", marks)
    print("Grade:", grade)


# Fixed test data for Jenkins
name = "Sanika"
marks = 89

display_result(name, marks)
