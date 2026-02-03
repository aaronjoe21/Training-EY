import pymysql

conn=pymysql.connect(
    host='localhost',
    user='root',
    password='Aaron@2003',
    database="company_db"
)

cursor = conn.cursor()
cursor.execute("insert into employees(emp_id, emp_name, email, salary, dept_id) VALUES (107, 'John Doe', 'aaron@2003gmail', 45000,70);")
cursor.execute("update employees set salary=50000 where emp_id=107")
cursor.execute("delete from employees where emp_id=107")
cursor.execute("select * from employees")

rows=cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()
