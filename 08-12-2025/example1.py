from flask import Flask, request, jsonify
app=Flask(__name__)
Employees=["Aaron","Sam","Vaishnavi"]

@app.route("/Employees",methods=["GET"])
def get_items():
    return jsonify(Employees)

@app.route("/Employees",methods=["POST"])
def add_item():
    data=request.get_json()
    item=data.get("Employee")
    items.append(item)
    return "POST EXECUTED"

@app.route("/Employees/<int:index>",methods=["PUT"])
def update_item(index):
    data=request.get_json()
    new_value=data.get("Employee")
    Employees[index]=new_value
    return"PUT EXECUTED"

@app.route("/Employees/<int:index>",methods=["DELETE"])
def delete_item(index):
    Employees.pop(index)
    return "DELETE EXECUTED"

if __name__=="__main__":
    app.run(debug=True)