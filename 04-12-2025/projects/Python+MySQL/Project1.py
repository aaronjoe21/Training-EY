#Employee Management CLI App


import pymysql
import csv

conn = pymysql.connect(
    host="localhost",
    user="root",
    passwd="V@ishnav1",
    db="company_db",   # use your DB
    autocommit=True
)
cursor = conn.cursor()

# --- Setup (run once) ---
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100),
    email VARCHAR(100),
    salary INT,
    dept_id INT
)
""")

# --- CRUD examples ---
cursor.execute("INSERT INTO employees (emp_id, emp_name, email, salary, dept_id) VALUES (201, 'Aisha Khan', 'aisha@example.com', 60000, 10)")
cursor.execute("INSERT INTO employees (emp_id, emp_name, email, salary, dept_id) VALUES (202, 'Rahul Sharma', 'rahul@example.com', 75000, 20)")
cursor.execute("UPDATE employees SET salary=80000 WHERE emp_id=202")
cursor.execute("DELETE FROM employees WHERE emp_id=999")  # safe no-op if not present

# --- Search / Read ---
cursor.execute("SELECT * FROM employees WHERE emp_name LIKE %s", ("%Rahul%",))
rows = cursor.fetchall()
for r in rows:
    print(r)

# --- Export to CSV ---
cursor.execute("SELECT emp_id, emp_name, email, salary, dept_id FROM employees")
rows = cursor.fetchall()
with open("employees_export.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["emp_id", "emp_name", "email", "salary", "dept_id"])
    w.writerows(rows)

cursor.close()
conn.close()
