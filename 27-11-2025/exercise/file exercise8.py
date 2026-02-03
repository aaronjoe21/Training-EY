import csv
students = [
    {"name": "Alice", "marks": 85},
    {"name": "Bob", "marks": 90},
    {"name": "Charlie", "marks": 78}
]

f=open("exercise8.csv", "w+")
writer=csv.writer(f)
writer.writerows(students)

reader=csv.reader(f)
print(reader)