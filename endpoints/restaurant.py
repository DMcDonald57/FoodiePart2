from app import app
from flask import request, make_response,jsonify
from dbhelpers import run_statement
import json
import uuid

# endpoints for restaurants go here

@app.post('/api/restaurantsession')
def restaurant_login():
    email = request.json.get('email')
    password = request.json.get('password')
    token = uuid.uuid4().hex
    result = run_statement("CALL verify_restaurant (?)", [email])
    restaurant_id=result[0][0]
    storedpassword=result[0][1]
    if storedpassword != password:
        return make_response(jsonify("Password does not match"), 401)
    result = run_statement('CALL Restaurant_login (?,?)' , [restaurant_id, token])
    if (type(result) == list):
        response = {
            "restaurantId" : result[0][0],
            "token" : result[0][1]
        }
        return make_response(jsonify(response),201)
    else:
        return make_response(jsonify(result), 500)

@app.delete('/api/restaurantsession')
def restaurant_logout():
    session_id = request.json.get('session_id')
    result = run_statement('CALL restaurant_logout (?)', [session_id])
    if result == None:
        return make_response(jsonify("Restaurant Logged out"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)