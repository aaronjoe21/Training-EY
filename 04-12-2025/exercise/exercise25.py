import csv

# Write CSV
employees = [["Name", "Dept"], ["Aisha", "HR"], ["Rahul", "IT"], ["Meera", "Finance"]]
with open("employees.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(employees)

# Read CSV
with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)

print(data)
