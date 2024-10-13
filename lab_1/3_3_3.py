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

# Підрахунок загальної кількості студентів
total_students = len(students)

subject_stats = {}

for subject in subjects:
    grades = [students_grades[name][subject] for name in students]
    average = sum(grades) / len(grades)  # Середня оцінка
    min_grade = min(grades)  # Мінімальна оцінка
    max_grade = max(grades)  # Максимальна оцінка
    subject_stats[subject] = {
        "average": average,
        "min": min_grade,
        "max": max_grade
    }


print(f"Загальна кількість студентів: {total_students}")
for subject, stats in subject_stats.items():
    print(f"Предмет: {subject}, Середня оцінка: {stats['average']:.2f}, Min оцінка: {stats['min']}, Max оцінка: {stats['max']}")
