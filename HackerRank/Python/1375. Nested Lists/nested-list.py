students = []

for _ in range(int(input())):
    name = input()
    score = float(input())
    students.append([name, score])

scores = []

for student in students:
    if student[1] not in scores:
        scores.append(student[1])

scores.sort()

second_lowest = scores[1]

names = []

for student in students:
    if student[1] == second_lowest:
        names.append(student[0])

names.sort()

for name in names:
    print(name)
