from csv import DictReader

with open("student.csv", "r") as f:
    reader = DictReader(f)
    for row in reader:
        with open(f"Welcome{row["STUDENT"]}.txt", "w") as c:
            total=f'''
            WELCOME TO OUR COLLEGE 
            {row["STUDENT"]}
            AND WELCOME TO OUR 
            {row[" COURSE"]} DEPARTMENT
            '''
            c.write(total)