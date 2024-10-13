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

# Знаходження студента з найвищою оцінкою з кожного предмета
top_students = {}

for subject in subjects:
    max_grade = -1  # Ініціалізуємо максимальну оцінку
    top_student = ""  # Ініціалізуємо ім'я студента

    for name in students:
        grade = students_grades[name][subject]
        if grade > max_grade:  # Якщо оцінка вища за поточну максимальну
            max_grade = grade  # Оновлюємо максимальну оцінку
            top_student = name  # Обновляем имя студента

    top_students[subject] = (top_student, max_grade)

for subject, (student, grade) in top_students.items():
    print(f"Предмет: {subject}, Студент: {student}, Оцінка: {grade}")
