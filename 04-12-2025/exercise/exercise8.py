
students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95, "Eva": 88}


sorted_students = sorted(students.items(), key=lambda x: x[1], reverse=True)

print(sorted_students[:3])
