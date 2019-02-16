import psycopg2
import re
import os

#import recommendation


def get_connection():
    conn = psycopg2.connect(databasename=POSTGRES_DB,
                           user=POSTGRES_USER,
                           password=POSTGRES_PW,
                           host=POSTGRES_URL,
                           port=POSTGRES_PORT)
    return conn


def get_recommendation():
    pass


class User(object):
    def get(self, id : int):
        pass


class Recommendation(object):
    def get(self, id : int):
        pass


