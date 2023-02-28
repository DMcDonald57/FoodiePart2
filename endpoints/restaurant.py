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
    id = request.json.get('id')
    result = run_statement('CALL restaurant_logout (?)', [id])
    if result == None:
        return make_response(jsonify("Restaurant Logged out"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)
    
@app.get('/api/restaurantprofile')
def get_restaurant():
    result = run_statement('CALL get_restaurant')
    keys = ["id", "name", "bio", "address", "city", "email", "phone_num", 
        "profile_url", "banner_url"]
    response = []
    if (type(result) == list):
        for id in result:
            response.append(dict(zip(keys,id)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(result), 500)
    
@app.post('/api/restaurantprofile')
def add_restaurant():
    name = request.json.get('name')
    bio = request.json.get('bio')
    address = request.json.get('address')
    city = request.json.get('city')
    email = request.json.get('email')
    phone_num = request.json.get('phone_num')
    profile_url = request.json.get('picture_url')
    banner_url = request.json.get('banner_url')
    password = request.json.get('password')
    token = uuid.uuid4().hex
    result = run_statement('CALL add_restaurant (?,?,?,?,?,?,?,?,?)', [name, bio, address,
    city, email, phone_num, profile_url, banner_url, password])
    restaurant_id=result[0][0]
    result = run_statement('CALL restaurant_login (?,?)', [restaurant_id, token])
    if (type(result) == list):
        response = {
            "restaurantId" : result[0][0],
            "token" : [token]
        }
        return make_response(jsonify(response), 201)
    else:
        return make_response(jsonify(result), 500)