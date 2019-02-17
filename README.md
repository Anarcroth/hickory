# Hickory

> More walking, less technology

## Description

Hickory is a web-based application that aims to provide a simple interface to hikers and mountaineers.

When registering to the app, the user specifies a couple of options for personalization.

## Features

- Recommendation

The recommendation system is based on vector matrixes. Each hiker is treated like a multi-dimensional vector, which is then compared to the set of all routes in the Database. The vectors are normalized and then sorted into a list of most-to-least similar routes. The routes are picked on the level of experience of the hiker, the desired hiking difficulty, fitness level, etc.

This module can be seen in the `controllers.py` file under the `Recommendation` class, where the vector algebra algorithm is working.

- Geo-location

The Geo-location is based on the `Google-API` for location services, that returns both desired and searched routes. The `Google-API` connection allows us to see in the UI what the desired route is.

In addition to this, we also calculate the distance between two points using the Haversine formula. This can be found under the `map.js` file.

- Working with the Bulgarian Mountaineer Union

Since during the seasons, routes change, we maintain the application database through the mountaineer union to give us current and up-to-date info on what conditions of the routes are. If a route is in a bad shape, it will be colored in red.

- Gamification

We also incentivize the hikers to go more in nature by awarding them with points on route completion. With these points and awards, hikers can earn discounts in huts and mountain shelters.
