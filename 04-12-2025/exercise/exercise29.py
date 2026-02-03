import csv, json

with open("employees.csv", "r") as f:
    reader = csv.DictReader(f)
    data = list(reader)

with open("employees.json", "w") as f:
    json.dump(data, f, indent=2)
