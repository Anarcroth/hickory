#!/bin/env python

import psycopg2
import re
import os
import recommendation

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    get_connection()


def get_connection():
    conn = psycopg2.connect(databasename=POSTGRES_DB,
                           user=POSTGRES_USER,
                           password=POSTGRES_PW,
                           host=POSTGRES_URL,
                           port=POSTGRES_PORT)
    return conn


def get_recommendation():
    pass
