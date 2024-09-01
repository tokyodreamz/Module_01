grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Антон', 'Гриша', 'Паша', 'Маша', 'Стас'}
sorted_students = sorted(students)
average_grades = {student: sum(grades[i]) / len(grades[i]) for i, student in enumerate(sorted_students)}
print(average_grades)