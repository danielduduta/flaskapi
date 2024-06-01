from flask import Flask, Response, request
import json

from data import cache, employees, EMP_KEYS


app = Flask(__name__)

cache.init_app(app=app, config={"CACHE_TYPE": "FileSystemCache","CACHE_DIR": "/tmp"})


@app.route("/api/v1/employees")
def list_employees():
    data = {"status": "success", "message":"Successfully! All records has been fetched."}
    data["data"] = [x for x in employees.values()]
    response = json.dumps(data)
    return Response(response=response, status=200, mimetype="application/json")


@app.route("/api/v1/employee/<emp_id>")
def get_employee(emp_id):
    data = {}
    employee = employees.get(int(emp_id), None)
    if not employee:
        data["status"] = "error"
        data["message"] = "No employee found"
        status = 404
    else:
        data["status"] = "success"
        data["message"] = "Successfully! Record has been fetched."
        data["data"] = employee
        status = 200
    return Response(response=json.dumps(data), status=status, mimetype="application/json")


@app.route("/api/v1/delete/<emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    data = {}
    emp_id = int(emp_id)
    employee = employees.get(int(emp_id), None)
    if not employee:
        data["status"] = "error"
        data["message"] = "No employee found"
        status = 404
    else:

        data["status"] = "success"
        data["message"] = "Successfully! Record has been deleted."
        del employees[emp_id]
        status = 200
    return Response(response=json.dumps(data), status=status, mimetype="application/json")


@app.route("/api/v1/create", methods=["POST"])
def create_employee():
    data = {}
    status_code = 200
    status = "success"
    message = "Successfully! Record has been added."
    emp_data = {}
    attribs = ["name", "age", "salary"]
    body = request.json
    errors = False
    
    for k in attribs:
        if k not in body.keys():
            status_code = 400
            message = "missing mandatory key '{}'".format(k)
            status = "failure"
            errors = True
            break

    if not errors:
        next_id = max(employees.keys()) + 1
        emp_data = {"id": next_id, "name": body["name"], "age": body["age"], "salary": body["salary"]}
        employees[next_id] = emp_data

    data["status"] = status
    data["message"] = message
    data["data"] = emp_data

    return Response(response=json.dumps(data), status=status_code, mimetype="application/json")


@app.route("/api/v1/update/<emp_id>", methods=["PUT"])
def update_employee(emp_id):
    data = {}
    status = "success"
    message = "Successfully! Record has been updated."
    status_code = 200
    employee = {}
    
    body = request.json
    emp_id = int(emp_id)
    employee = employees.get(int(emp_id), None)
    if not employee:
        status = "error"
        message = "No employee found"
        status_code = 404
    else:
        for k in EMP_KEYS:
            if body.get(k):
                employee[k] = body[k]
    
    data["status"] = status
    data["message"] = message
    data["data"] = employee
    
    return Response(response=json.dumps(data), status=status_code, mimetype="application/json")