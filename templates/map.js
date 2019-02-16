const meanRadius = 6378137; // Earth’s mean radius in meter

let rad = function(x) {
    return x * Math.PI / 180;
};

let getDistance = function(p1Lat, p1Long, p2Lat, p2Long) {
    let dLat = rad(p2Lat - p1Lat);
    let dLong = rad(p2Long - p1Long);

    // Haversine formula
    let a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
	Math.cos(rad(p1Lat)) * Math.cos(rad(p2Lat)) *
	Math.sin(dLong / 2) * Math.sin(dLong / 2);
    let c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));

    let distanceMeters = meanRadius * c;

    return distanceMeters / 1000;
};

getDistance(41.7677, 23.4008, 42.1797, 23.5866);
