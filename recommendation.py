import math


def get_users():
    pass


def get_list_routes():
    pass


def normalize(vector):
    length = math.sqrt(sum([math.pow(i, 2) for i in vector]))
    for item in vector:
        item = float(item) / length
    coefficients = [0.2, 0.2, 0.2, 0.4]
    for index in range(len(vector)):
        vector[index] *= coefficients[index]
    return vector


def check_prev_routes():
    pass


def search_nearest_route():
    user = [1000, 250, 10, 10]  # get_users()
    routes = [[100, 250, 8, 10], [1000, 100, 3, 2], [100000, 400, 9, 2]]
    #get_list_routes()

    user = normalize(user)
    for route in routes:
        route = normalize(route)

    nearest_routes = sort_by_nearest(routes, user)
    print(nearest_routes)


def sort_by_nearest(routes, comparator):
    closest_dist = []
    for route in routes:
        temp_dist = 0
        for index in range(len(route)):
            temp_dist += abs(comparator[index] - route[index])
            closest_dist.append(temp_dist)
    return closest_dist.sort()


search_nearest_route()
