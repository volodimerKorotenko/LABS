import csv
# Відкриваємо CSV-файл
with open('netflix_list.csv', 'r', encoding='utf-8') as file:
    # Використовуємо DictReader для читання рядків як словників
    Data = csv.DictReader(file)    
    # Перевірка, що стовпець 'rating' існує і фільтрація даних
    filteredData = [
        {key: row[key] for key in list(row.keys())[:5]}  # Зберігаємо перші 5 колонок
        for row in Data 
        if 'rating' in row and row['rating'] and float(row['rating']) > 7.5  # Фільтрування по 'rating'
    ]
for row in filteredData:
    print(row)
