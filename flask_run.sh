#!/bin/bash
export POSTGRES_URL="172.16.191.230:5432"
export POSTGRES_PORT="5432"
export POSTGRES_USER="postgres"
export POSTGRES_PW="dbpw"
export POSTGRES_DB="test"
FLASK_APP=hickory.py flask run
