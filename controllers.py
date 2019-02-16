import psycopg2
import re
import os
import math

from constants import MAX_COEFFICIENTS



def get_connection():
    conn = psycopg2.connect(databasename=POSTGRES_DB,
                           user=POSTGRES_USER,
                           password=POSTGRES_PW,
                           host=POSTGRES_URL,
                           port=POSTGRES_PORT)
    return conn


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
        coefficients = [0.2, 0.2, 0.2, 0.4]
        for i, item in enumerate(vector):
            vector[i] = coefficients[i] * item
        return vector

    @staticmethod
    def sort_by_nearest(user : list, routes : list) -> list:
        closest_dist = []
        for route in routes:
            temp_dist = 0
            for i, index in enumerate(route):
                temp_dist += abs(user[i] - route[i])
            closest_dist.append(temp_dist)
            #print(temp_dist)
        return sorted(closest_dist)

    @staticmethod
    def search_nearest_route(user : list = None, routes : list = None) -> list:
        if not user:
            user = [1000, 250, 10, 10]  # get_users()
        if not routes:
            routes = [[1000, 100, 3, 2], [100000, 400, 9, 2], [100, 250, 8, 10]]
        #get_list_routes()

        user = Recommendation.normalize(user)
        for i, route in enumerate(routes):
            routes[i] = Recommendation.normalize(route)
            routes[i] = Recommendation.weight(route)

        nearest_routes = Recommendation.sort_by_nearest(user, routes)
        return nearest_routes




# connection to the database
class User(object):
    def get(self, id : int):
        pass


class Route(object):
    def get(self, id : int):
        pass

    @staticmethod
    def get_all():
        return []


class UserSetting(object):
    @staticmethod
    def get_by_foreign_key(**kvargs):
        return None
