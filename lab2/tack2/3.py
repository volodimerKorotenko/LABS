import csv
def filter_shows(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                if row.get('episodes') and row.get('numVotes'):
                    if int(row['episodes']) > 10 and float(row['numVotes']) > 1000.0:
                        yield row['title']
            except ValueError:
                continue

file_path = 'netflix_list.csv'

# Використовуємо генератор для фільтрації і створення список з допомогою list comprehensions
filtered_titles = [title for title in filter_shows(file_path)]

print("Заголовки шоу з більше чим 10 эпізодами і рейтингом вижче середнього:")
for title in filtered_titles:
    print(title)
