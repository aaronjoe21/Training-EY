'''
from flask import Flask
app=Flask(__name__)

@app.route("/get-item",methods=["GET"])
def get_item():
    return "GET EXECUTED"
@app.route("/create-item",methods=["POST"])
def create_item():
    return "POST EXECUTED"
@app.route("/update-item",methods=["PUT"])
def update_item():
    return "PUT EXECUTED"
@app.route("/delete-item",methods=["DELETE"])
def delete_item():
    return "DELETE EXECUTED"
if __name__ == "__main__":
    app.run()
'''
'''
from flask import Flask, request, jsonify
app=Flask(__name__)
items=["apple","banana","orange"]
@app.route("/item",methods=["GET"])
def get_items():
    return jsonify(items)

if __name__=="__main__":
    app.run(debug=True)
'''

from flask import Flask, request, jsonify
app=Flask(__name__)
items=["apple","banana","orange"]

@app.route("/items",methods=["GET"])
def get_items():
    return jsonify(items)

@app.route("/items",methods=["POST"])
def add_item():
    data=request.get_json()
    item=data.get("item")
    items.append(item)
    return "POST EXECUTED"

@app.route("/items/<int:index>",methods=["PUT"])
def update_item(index):
    data=request.get_json()
    new_value=data.get("item")
    items[index]=new_value
    return"PUT EXECUTED"

@app.route("/items/<int:index>",methods=["DELETE"])
def delete_item(index):
    items.pop(index)
    return "DELETE EXECUTED"

if __name__=="__main__":
    app.run(debug=True)