from flask import Flask, request, jsonify
import pymysql

conn = pymysql.connect(
    host='localhost',
    user='root',
    password='Aaron@2003',
    database='employees_db'
)
cursor = conn.cursor()
app = Flask(__name__)
@app.route("/employee",methods=["GET"])
def get_employees():
    cursor.execute("select * from Employees")
    rows = cursor.fetchall()
    return jsonify(rows)

@app.route("/employee-add",methods=["POST"])
def insert_employees():
    data = request.get_json()
    emp_id = data.get("emp_id")
    emp_name = data.get("emp_name")
    email = data.get("email")
    salary = data.get("salary")
    dept_id = data.get("dept_id")

    sql = "INSERT INTO Employees (emp_id, emp_name, email, salary, dept_id) VALUES (%s, %s, %s, %s, %s)"
    cursor.execute(sql, (emp_id, emp_name,email,salary,dept_id))
    conn.commit()
    return "Employee added successfully"

@app.route("/employee-update/<int:emp_id>",methods=["PUT"])
def put_item(emp_id):
    data = request.get_json()
    emp_name = data.get("emp_name")
    email = data.get("email")
    salary = data.get("salary")
    dept_id = data.get("dept_id")

    sql = "UPDATE Employees SET emp_name=%s,email=%s, salary=%s, dept_id=%s WHERE emp_id=%s"
    cursor.execute(sql, (emp_name,email, salary, dept_id,emp_id))
    conn.commit()
    return "Employee updated successfully"
if __name__=="__main__":
    app.run(debug=True)