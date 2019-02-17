from sqlalchemy import create_engine
#import recommendation
import psycopg2
import re
import os
import math

from db_connection import get_env_variable
from constants import COEFFICIENTS, MAX_COEFFICIENTS


def get_connection():
    POSTGRES_URL = get_env_variable("POSTGRES_URL")
    POSTGRES_USER = get_env_variable("POSTGRES_USER")
    POSTGRES_PW = get_env_variable("POSTGRES_PW")
    POSTGRES_DB = get_env_variable("POSTGRES_DB")

    DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
    engine = create_engine(DB_URL)
    conn = engine.connect()
    return conn

CONNECTION = get_connection()


# recommendation system

def get_recommendation(user_id : int):
    user_settings = UserSetting.get_by_foreign_key(user_id=user_id)
    routes = Route.get_all()
    return Recommendation.search_nearest_route(user_settings, routes)


class Recommendation(object):
    """Provides recommendation system."""

    @staticmethod
    def normalize(vector : list) -> list:
        """Normalize a vector of values."""
        normalize_values = [u / m for u, m in zip(vector, MAX_COEFFICIENTS)]
        length = math.sqrt(sum([math.pow(i, 2) for i in normalize_values]))
        for i, item in enumerate(normalize_values):
            vector[i] = float(item) / length
        return vector

    @staticmethod
    def weight(vector : list) -> list:
        for i, item in enumerate(vector):
            vector[i] = COEFFICIENTS[i] * item
        return vector

    @staticmethod
    def sort_by_nearest(user : list, routes : list) -> list:
        for route in routes:
            for i, index in enumerate(route.profile_vector):
                route.approximation += abs(user[i] - route.profile_vector[i])
            #print(temp_dist)
        return sorted(routes, key=lambda r: r.approximation)


    @staticmethod
    def search_nearest_route(user : list = None, routes : list = None) -> list:
        hard_code = [[1000, 100, 3, 2], [100000, 400, 9, 2], [100, 250, 8, 10], [155, 4, 54, 7], [300, 50, 40, 55]]
        if not user:
            user = [1000, 250, 10, 10]  # get_users()
        for route, profile in zip(routes, hard_code):
            if not route.profile_vector:
                route.profile_vector = profile
        #get_list_routes()

        user = Recommendation.normalize(user)
        for i, route in enumerate(routes):
            routes[i].profile_vector = Recommendation.normalize(route.profile_vector)
            routes[i].profile_vector = Recommendation.weight(route.profile_vector)

        nearest_routes = Recommendation.sort_by_nearest(user, routes)
        return nearest_routes




# connection to the database
class User(object):
    @staticmethod
    def get(id : int):
        sql = "Select user from users where user_id = %s;"
        data = (id)
        result = CONNECTION.execute(sql, data)
        r = result.fetchone()
        user_dict = {
            "id": r[0],
            "name": r[1],
            "age": r[2]
        }
        return user_dict


class Route(object):
    def __init__(self, id : int = None, name : str = None, from_dest : str = None, to_dest : str = None, description : str = None, difficulty : str = None, profile_vector : list = None):
        self.id = id
        self.route = id
        self.name = name
        self.from_dest = from_dest
        self.to_dest = to_dest
        self.description = description
        self.difficulty = difficulty
        self.approximation = 0.0
        self.profile_vector = profile_vector

    @staticmethod
    def get( id : int):
        sql = "Select * from routes where route_id =%s;"
        data = (id)
        result = CONNECTION.execute(sql, data)
        r = result.fetchone()
        route = Route(r[0],[1],r[2],r[3],[4],r[5])
        route_dict = Route.to_json(route)
        return route_dict

    @staticmethod
    def get_all() -> list:
        sql_query = "Select * from routes"
        results = CONNECTION.execute(sql_query)
        results = results.fetchall()
        routes = [Route(r[0],[1],r[2],r[3],[4],r[5]) for r in results]
        return routes


    @staticmethod
    def to_json(route ) -> dict:
        json_route = {
            'name' : route.name,
            'route' : route.id,
            'from_dest' : route.from_dest,
            'to_dest' : route.to_dest,
            'description' : route.description,
            'difficulty' : route.difficulty,
        }
        return json_route

class UserSetting(object):
    @staticmethod
    def get_by_foreign_key(**kvargs):
        return None
