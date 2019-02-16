#!/bin/bash
export POSTGRES_URL="127.0.0.1:5432"
export POSTGRES_USER="postgres"
export POSTGRES_PW="dbpw"
export POSTGRES_DB="test"
FLASK_APP=hickory.py flask run
