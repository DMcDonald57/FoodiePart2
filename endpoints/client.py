from app import app
from flask import request, make_response, jsonify
from dbhelpers import run_statement
import json
import uuid

# endpoints for clients go here

@app.post('/api/clientsession')
def client_login():
    email = request.json.get('email')
    password = request.json.get('password')
    result = run_statement('CALL client_login (?,?)' , [email, password])
    if (type(result) == list):
        return json.dumps("clientId: {}".format (result, default=str))
    else:
        return make_response(jsonify(result), 500)

@app.delete('/api/clientsession')
def client_logout():
    id = request.json.get('id')
    result = run_statement('CALL client_logout (?)', [id])
    if result == None:
        return make_response(jsonify("Client Logged out"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)