students = [ {"name": "Nooh", "Grades": [90, 80, 99]},
             {"name": "Maram", "Grades": [95, 89, 85]},
             {"name": "Nada", "Grades": [65, 72, 98]},]

for student in students:
    average = sum(student["Grades"]) / len(student["Grades"])

    print(student["name"])
    print(average)