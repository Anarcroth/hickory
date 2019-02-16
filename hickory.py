#!/bin/env python

from flask import Flask
from flask import render_template
from flask import request

import json

import controllers

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/recommendations", methods=["POST"])
def recommendations():
    recs = controllers.get_recommendations()
    return json.dumps(recs)


@app.route("/route/<int:id>")
def get_route(id: int):
    route = controllers.Route.get(id)
    #return render_template('route.html', {'route': route})


@app.route("/user/<int:id>")
def user(id: int):
    user = controllers.User.get(id)
    #return render_template('user.html', {'user': user})


if __name__ == '__main__':
    app.run(debug=True)
    #controllers.get_connection()