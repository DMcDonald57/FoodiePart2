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
    token = uuid.uuid4().hex
    result = run_statement("CALL verify_client (?)", [email])
    client_id=result[0][0]
    storedpassword=result[0][1]
    if storedpassword != password:
        return make_response(jsonify("Password does not match"),401)
    result = run_statement('CALL client_login (?,?)', [client_id, token])
    if (type(result) == list):
        response = {
            "clientId" : result[0][0],
            "token" : result[0][1]
        }
        return make_response(jsonify(response), 201)
    else:
        return make_response(jsonify(result), 500)

@app.delete('/api/clientsession')
def client_logout():
    session_id = request.json.get('session_id')
    result = run_statement('CALL client_logout (?)', [session_id])
    if result == None:
        return make_response(jsonify("Client Logged out"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)

@app.get('/api/clientprofile')
def get_clients():
    id = request.json.get('id')
    token = uuid.uuid4().hex
    if token != token:
        return make_response((jsonify("Error"),401))
    result = run_statement('CALL get_clients (?)', [id])
    keys = ["id", "username", "first_name", "last_name", "email", "picture_url", "created_at"]
    response = []
    if (type(result) == list):
        for id in result:
            response.append(dict(zip(keys,id)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(result), 500)

@app.post('/api/clientprofile')
def add_client():
    username = request.json.get('username')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    email = request.json.get('email')
    password = request.json.get('password')
    picture_url = request.json.get('picture_url')
    result = run_statement('CALL add_client (?,?,?,?,?,?)', [username, first_name, 
    last_name, email, password, picture_url])
    if (type(result) == list):
        return json.dumps("ClientId: {}".format (result))
    else:
        return make_response(jsonify(result), 500)

@app.patch('/api/clientprofile')
def update_client():
    id = request.json.get('id')
    username = request.json.get('username')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    password = request.json.get('password')
    picture_url = request.json.get('picture_url')
    result = run_statement('CALL update_client (?,?,?,?,?,?)', [id, username, first_name, 
    last_name, password, picture_url])
    if result == None:
        return make_response(jsonify("Client info updated"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)


@app.delete('/api/clientprofile')
def delete_client():
    id = request.json.get('id')
    result = run_statement('CALL delete_client (?)', [id])
    if result == None:
        return make_response(jsonify("Client Profile has been deleted"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)
