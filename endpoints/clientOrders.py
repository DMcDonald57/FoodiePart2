from app import app
from flask import request, make_response,jsonify
from dbhelpers import run_statement
import json
import uuid

# endpoints for orders by clients go here

@app.post('/api/orders')
def create_order():
    email = request.json.get('email')
    password = request.json.get('password')
    token = uuid.uuid4().hex
    result = run_statement("CALL verify_client (?)", [email])
    storedpassword=result[0][1]
    if storedpassword != password:
        return make_response(jsonify("Password does not match"),401)
    if token != token:
        return make_response((jsonify("Error"),401))
    client_id=result[0][0]
    result = run_statement('CALL client_login (?,?)', [client_id, token])
    if result == None:
        return make_response(jsonify("Order Placed"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)