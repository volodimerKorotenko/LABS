import csv
def countIsAdult(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get('isAdult') == '1':
                count += 1
    return count

def countNumVotes(file_path):
    count = 0
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row.get('numVotes'):
                try:
                    if float(row['numVotes']) > 1000.0:
                        count += 1
                except ValueError:
                    continue  # Игноруємо рядкі, де numVotes не є числом
    return count

file_path = 'netflix_list.csv'

adult_count = countIsAdult(file_path)
numvotes_count = countNumVotes(file_path)

print(f"Кількість рядків з isAdult = 1: {adult_count} /// Кількість рядків з numVotes > 1000.0: {numvotes_count}")
