const meanRadius = 6378137; // Earth’s mean radius in meter

let toLat = 42.264444;
let toLong = 23.606944;
let fromLat = 42.179722;
let fromLong = 23.586667;
let mapTo;
let mapFrom;
let routeComplexity = "green";

// Google API defined
let directionsService;
let directionsDisplay;

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

function initMap() {
    directionsService = new google.maps.DirectionsService();
    directionsDisplay = new google.maps.DirectionsRenderer({
	polylineOptions: {
	    strokeColor: routeComplexity
	}
    });

    mapTo = new google.maps.LatLng(toLat, toLong);
    mapFrom = new google.maps.LatLng(fromLat, fromLong);
    let mapOptions = {
	zoom: 14,
	center: mapFrom
    };

    let map = new google.maps.Map(document.getElementById('map'), mapOptions);
    directionsDisplay.setMap(map);
    calcRoute();
}

function calcRoute() {
    let request = {
	origin: mapFrom,
	destination: mapTo,
	travelMode: google.maps.TravelMode['WALKING']
    };
    directionsService.route(request, function(response, status) {
	if (status === 'OK') {
	    directionsDisplay.setDirections(response);
	}
    });
}

calcRoute();
