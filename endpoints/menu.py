from app import app
from flask import request, make_response,jsonify
from dbhelpers import run_statement
import json
import uuid

# endpoints for menu go here

@app.get('/api/menu')
def get_menu():
    result = run_statement('CALL get_menu')
    keys = ["menu_id", "name", "discription", "price", "img_url", "restaurant_id"]
    response = []
    if (type(result) == list):
        for menu_id in result:
            response.append(dict(zip(keys,menu_id)))
        return make_response(jsonify(response), 200)
    else:
        return make_response(jsonify(result), 500)
    
@app.post('/api/menu')
def add_menu_item():
    email = request.json.get('email')
    password = request.json.get('password')
    token = uuid.uuid4().hex
    name = request.json.get('name')
    discription = request.json.get('discription')
    price = request.json.get('price')
    result = run_statement("CALL verify_restaurant (?)", [email])
    restaurant_id=result[0][0]
    storedpassword=result[0][1]
    if token != token:
        return make_response((jsonify("Error"),401))
    if storedpassword != password:
        return make_response(jsonify("Password does not match"), 401)
    result = run_statement('CALL add_menu_item (?,?,?,?)', [name, discription, price, restaurant_id])
    if result == None:
        return make_response(jsonify("Restaurant info updated"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)
    
@app.patch('/api/menu')
def update_menu_item():
    email = request.json.get('email')
    password = request.json.get('password')
    token = uuid.uuid4().hex
    menu_id = request.json.get('menu_id')
    name = request.json.get('name')
    discription = request.json.get('discription')
    price = request.json.get('price')
    img_url = request.json.get('img_url')
    result = run_statement("CALL verify_restaurant (?)", [email])
    restaurant_id=result[0][0]
    storedpassword=result[0][1]
    if token != token:
        return make_response((jsonify("Error"),401))
    if storedpassword != password:
        return make_response(jsonify("Password does not match"), 401)
    result = run_statement('CALL update_menu_item (?,?,?,?,?,?)', [menu_id, name, discription, price, img_url, restaurant_id])
    if result == None:
        return make_response(jsonify("Restaurant info updated"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)
    
@app.delete('/api/menu')
def delete_menu_item():
    email = request.json.get('email')
    password = request.json.get('password')
    token = uuid.uuid4().hex
    menu_id = request.json.get('menu_id')
    result = run_statement("CALL verify_restaurant (?)", [email])
    restaurant_id=result[0][0]
    storedpassword=result[0][1]
    if token != token:
        return make_response((jsonify("Error"),401))
    if storedpassword != password:
        return make_response(jsonify("Password does not match"), 401)
    result = run_statement('CALL delete_menu_item (?,?)', [menu_id, restaurant_id])
    if result == None:
        return make_response(jsonify("Menu Item has been deleted"), 200)
    else:
        return make_response(jsonify("Something went wrong"), 500)