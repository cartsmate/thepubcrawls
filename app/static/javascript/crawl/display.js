function displayCrawl(stop_offs, locator) {
    /*for (let i=0; i<stop_offs.length; i++) {
        console.log(stop_offs[i])
    }*/
    stop_offs = stop_offs.sort((a, b) => {
        if (a.distance_from_first < b.distance_from_first) {
            return -1;
        }
    });
    /*
    for (let i=0; i<stop_offs.length; i++) {
        console.log(stop_offs[i])
    }*/
    var pinColor = '#0275D8'
    var pinSVGHole = "M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z";
    var labelOriginHole = new google.maps.Point(12,15);
    var pinSVGFilled = "M 12,2 C 8.1340068,2 5,5.1340068 5,9 c 0,5.25 7,13 7,13 0,0 7,-7.75 7,-13 0,-3.8659932 -3.134007,-7 -7,-7 z";
    var labelOriginFilled =  new google.maps.Point(12,9);
    var pinHole = pinSVGHole
    var markerImage = {  // https://developers.google.com/maps/documentation/javascript/reference/marker#MarkerLabel
            path: pinHole,
            anchor: new google.maps.Point(12,17),
            fillOpacity: 1,
            fillColor: pinColor,
            strokeWeight: 2,
            strokeColor: "white",
            scale: 2,
            labelOrigin: labelOriginHole
        };
    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer({ suppressMarkers: false, markerOptions: {icon: markerImage}, polylineOptions: { strokeColor: '#0275D8' } });

    var map = new google.maps.Map(document.getElementById(locator), {
        zoom:7,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: false,
        streetViewControl: false,
        zoomControl: false
    });
    map.addListener("click", (event) => {
        console.log('you clicked on the map')
        event.stop();
        window.location.href = "/pub/crawl"
    });
    directionsRenderer.setMap(map);
    var request = {
        origin: {placeId: stop_offs[0].place},
        destination: {placeId: stop_offs[stop_offs.length-1].place},
        optimizeWaypoints: true,
        travelMode: google.maps.DirectionsTravelMode.WALKING
    };
    ways = []

    if (stop_offs.length > 2) {
        for (let i=1; i<stop_offs.length-1; i++) {
            ways.push({stopover: true, location: { placeId: stop_offs[i].place }})
        }
        request["waypoints"] = ways
    }
    directionsService.route(request, function(response, status) {
        var no_of_legs = response.routes[0].legs.length
        if (status == google.maps.DirectionsStatus.OK) {

            var optimised_route = response.geocoded_waypoints
            optimised_route[0]['duration'] = 0
            for (let i = 0; i < response.routes[0].legs.length; i++) {
                var duration = response.routes[0].legs[i].duration.value
                optimised_route[i+1]['duration'] = duration
            }
            let merged = stop_offs.map((item, i) => Object.assign({}, item, optimised_route[i]));

            populate_table(merged)
            directionsRenderer.setDirections(response);
        }
    });
}
