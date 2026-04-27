students = [
   {'ad': 'Ali', 'notlar': [85,90,78]},
   {'ad': 'Ayşe', 'notlar': [92,88,95]},
   {'ad': 'Mehmet', 'notlar': [70,75,80]}
]
for student in students:
    name = student['ad']
    grades = student['notlar']
    average = sum(grades) / len(grades)

    print(f"{name}:{average:.2f}")