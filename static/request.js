function getUser(uid) {
    return fetch('http://localhost:5000/user/1', {
        method : 'GET',
        headers: {
            "Content-Type": 'application/json',
        }
    }).then(
        response => response.text()
    );
}

function getRoute(routeId) {
    return fetch('http://localhost:5000/route/6', {
        method : 'GET',
        headers: {
            "Content-Type": 'application/json',
        }
    }).then(
        response => response.text()
    );
}
