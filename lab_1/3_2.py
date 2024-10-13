def convert_value(value):
    try:
        return int(value)  # Пробуємо перетворити на ціле число
    except ValueError:
        return value.strip()  # Якщо не вийшло, повертаємо рядок без пробілів
def read_file(parts):# функція для читання однієї рядки у файлі та наступний запис у зміну
    with open(parts, 'r') as nf:
        res = [convert_value(line) for line in nf.readlines()]
    return res
students = read_file('student_marks/student_names.txt')
math_grades = read_file('student_marks/math.txt')
physics_grades = read_file('student_marks/physics.txt')
statistics = read_file('student_marks/statistics.txt')
students_grades = {}
subjects = ["Математика", "Физика", "Статистика"]

for i, name in enumerate(students):
    # Створюємо словник оцінок для кожного студента
    students_grades[name] = {
        subjects[0]: math_grades[i],
        subjects[1]: physics_grades[i],
        subjects[2]: statistics[i]
    }

for student, grades in students_grades.items():
    print(f"{student}: {grades}")
