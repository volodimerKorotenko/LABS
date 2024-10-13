import os

part = 'student_marks'

rez = sorted(os.listdir(part))
for n, item in enumerate(rez):
    print(n + 1, item)
