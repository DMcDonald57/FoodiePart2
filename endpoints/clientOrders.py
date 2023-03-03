from app import app
from flask import request, make_response,jsonify
from dbhelpers import run_statement
import json
import uuid

# endpoints for orders by clients go here

@app.post('/api/orders')
def client_orders():
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
    if (type(result) == list):
        response = {
            "logged in"
        }
        return make_response(jsonify(response), 201)
    # result = run_statement('CALL client_orders (?)' , [client_id])
    # if (type(result) == list):
    #     response = {
    #         "restaurantId" : 
    #         "items" : 
    #     }
    #     return make_response(jsonify(response), 201)
    # else:
    #     return make_response(jsonify(result), 500)
