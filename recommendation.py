import math

max_coefficients = [1000000, 2500, 10000, 100]


def get_users():
    pass


def get_list_routes():
    pass


def normalize(vector):
    normalize_values = [u / m for u, m in zip(vector, max_coefficients)]
    length = math.sqrt(sum([math.pow(i, 2) for i in normalize_values]))
    for i, item in enumerate(normalize_values):
        vector[i] = float(item) / length
    return vector


def weight(vector):
    coefficients = [0.2, 0.2, 0.2, 0.4]
    for i, item in enumerate(vector):
        vector[i] = coefficients[i] * item
    return vector


def check_prev_routes():
    pass


def search_nearest_route():
    user = [1000, 250, 10, 10]  # get_users()
    routes = [[1000, 100, 3, 2], [100000, 400, 9, 2], [100, 250, 8, 10]]
    #get_list_routes()

    user = normalize(user)
    for i, route in enumerate(routes):
        routes[i] = normalize(route)
        routes[i] = weight(route)

    nearest_routes = sort_by_nearest(routes, user)
    print(nearest_routes)


def sort_by_nearest(routes, user):
    closest_dist = []
    for route in routes:
        temp_dist = 0
        for i, index in enumerate(route):
            temp_dist += abs(user[i] - route[i])
        closest_dist.append(temp_dist)
        print(temp_dist)

    return sorted(closest_dist)


search_nearest_route()
