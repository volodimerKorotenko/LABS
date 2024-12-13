# Відкриваємо файл для читання
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    # Читаем все строки
    lines = file.readlines()

data = []

# Обробляємо кожен рядок
for line in lines:
    # Видаляємо зайві прогалини та символи перекладу рядка
    cleaned_line = line.strip()
    # Розділяємо рядок по комах
    split_line = cleaned_line.split(',')
    # Додаємо отриманий список до загального списку
    data.append(split_line)
