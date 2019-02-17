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

@app.route("/recommendations/<int:uid>")
def recommendations(uid: int):
    recs = controllers.get_recommendations(uid)
    recs = [r.to_json() for r in recs]
    return json.dumps(recs)


@app.route("/route/<int:id>")
def get_route(id: int):
    route = controllers.Route.get(id)
    #return render_template('route.html', {'route': route})
    return json.dumps(route)


@app.route("/user/<int:id>")
def user(id: int):
    user = controllers.User.get(id)
    #return render_template('user.html', {'user': user})
    return json.dumps(user)

@app.route("/user_page")
def user_page():
    return render_template('user.html')
	
@app.route("/route_page")
def route():
    return render_template('route.html')

if __name__ == '__main__':
    app.run(debug=True)
    #controllers.get_connection()

