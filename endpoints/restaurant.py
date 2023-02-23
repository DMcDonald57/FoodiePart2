from app import app
from flask import request, make_response,jsonify
from dbhelpers import run_statement
import json

# endpoints for restaurants go here

@app.post('/api/restaurantsession')
def restaurant_login():
    email = request.json.get('email')
    password = request.json.get('password')
    result = run_statement('CALL Restaurant_login (?,?)' , [email, password])
    if (type(result) == list):
        return json.dumps("restaurantId: {}".format (result, default=str))
    else:
        return make_response(jsonify(result), 500)

@app.delete('/api/restaurantsession')
def restaurant_logout():
    id = request.json.get('id')
    result = run_statement('CALL restaurant_logout (?)', [id])
    if result == None:
        return make_response(jsonify("Restaurant Logged out"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)