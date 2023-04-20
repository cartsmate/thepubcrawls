function displayCrawl(stop_offs) {
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
    var directionsService = new google.maps.DirectionsService();
    var directionsRenderer = new google.maps.DirectionsRenderer();

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom:7,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: false,
        streetViewControl: false
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
