#!/bin/env python

import psycopg2
import re
import os

from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


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
