from flask import Flask

app = Flask(__name__)

from endpoints import restaurant, client, menu, clientOrders