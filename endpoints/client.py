from app import app
from flask import request, make_response, jsonify
from dbhelpers import run_statement
import json
import uuid

# endpoints for clients go here

@app.post('/api/foodiepart2')
def client_login():
    email = request.json.get('email')
    password = request.json.get('password')
    result = run_statement('CALL client_login (?,?)' , [email, password])
    # uuidOne = uuid.uuid1()
    if (type(result) == list):
        return json.dumps(result, default=str)
    else:
        return "There was an error"