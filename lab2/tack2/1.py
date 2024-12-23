import csv

class CastIterator:
    def __init__(self, file_path):
        self.file_path = file_path  # Шлях до файлу
        self.file = open(file_path, 'r', encoding='utf-8')  # Відкриття файлу
        self.reader = csv.DictReader(self.file)  # Читання файлу як словник
        self.count = 0  # Личильник оброблених рядків
        self.max_records = 10  # Ліміт записей

    def __iter__(self):
        return self  # Повертає сам інтератор

    def __next__(self):
        if self.count >= self.max_records:  # Перевірка на обмеження записи
            self.file.close()  # Зачинити файл після закінчення
            raise StopIteration  # Завершення ітерації

        for row in self.reader:  # Прохід по рядкам
            if 'cast' in row and len(row['cast']) > 50:  # Перевірка на довжину поля 'cast'
                self.count += 1
                return row['cast']  # Повертання поля 'cast'

        # Якщо більше немає рядків
        self.file.close()
        raise StopIteration

file_path = 'netflix_list.csv'
cast_iterator = CastIterator(file_path)

for cast in cast_iterator:
    print(cast)
