import csv
def filter_netflix_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Перевірка умов
            if (
                row.get('language') == 'English' and
                row.get('type') in ('tvSeries', 'movie') and
                row.get('endYear') and int(row['endYear']) > 2015
            ):
                yield row  # Повертаємо рядок, який відповідає умовам
                
file_path = 'netflix_list.csv'
for filtered_row in filter_netflix_data(file_path):
    print(filtered_row)
