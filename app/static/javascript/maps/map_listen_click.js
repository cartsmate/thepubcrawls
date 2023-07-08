function map_listen_click(map, data) {
    console.log('map_listen_click')
    map.addListener('click', function (event) {
        // If the event is a POI
        if (event.placeId) {

            var request = {
                placeId: event.placeId,
                fields: ['rating', 'reviews', 'user_ratings_total']
            };
            var service = new google.maps.places.PlacesService(map);
            service.getDetails(request, function(place, status) {
                if (status === google.maps.places.PlacesServiceStatus.OK) {
                    var reviews = place.reviews;
                    // console.log(place.rating + ' ' + place.user_ratings_total)
                    document.getElementById("rank").value = place.rating
                    shadeStars('rank', place.rating, 'map')
                    // Process and display the reviews on your web page as desired
                }
            });

            if (document.getElementById("submit").disabled = true) {
                document.getElementById("submit").disabled = false
                document.getElementById("submit_message").style.display = "none"
            }
            // Call event.stop() on the event to prevent the default info window from showing.
            event.stop();
            document.getElementById("place").value = event.placeId;
            console.log('event: ' + JSON.stringify(event))

            lat_lng_json = JSON.stringify(event.latLng.toJSON());
            var lat_lng_obj = JSON.parse(lat_lng_json);
            document.getElementById("pub_latitude").value = lat_lng_obj.lat;
            document.getElementById("pub_longitude").value = lat_lng_obj.lng;

            nearestStation(place, lat_lng_obj)
            /*
            records = []
            for (let i = 0; i < stations.length; i++) {
                lat_diff = Math.abs(stations[i]['station_latitude'] - lat_lng_obj.lat)
                lng_diff = Math.abs(stations[i]['station_longitude'] - lat_lng_obj.lng)
                tot_diff = lat_diff + lng_diff
                var record = { name: stations[i]['station_name'], id: stations[i]['station_identity'], distance: tot_diff}
                records.push(record);
            }
            records = records.sort((a, b) => {
                if (a.distance < b.distance) {
                    return -1;
                }
            });
            document.getElementById("station_name").value = records[0]['name']
            document.getElementById("station_identity").value = records[0]['id']

            records2 = []
            for (let i = 0; i < areas.length; i++) {
                lat_diff = Math.abs(areas[i]['area_latitude'] - lat_lng_obj.lat)
                lng_diff = Math.abs(areas[i]['area_longitude'] - lat_lng_obj.lng)
                tot_diff = lat_diff + lng_diff
                var record2 = { name: areas[i]['area_name'], id: areas[i]['area_identity'], distance: tot_diff}
                records2.push(record2);

            }
            records2 = records2.sort((a, b) => {
                if (a.distance < b.distance) {
                    return -1;
                }
            });
            document.getElementById("area_name").value = records2[0]['name']
            document.getElementById("area_identity").value = records2[0]['id']

            */

            map = show_map(lat_lng_obj.lat, lat_lng_obj.lng, map.getZoom())
            if (document.getElementById('rank').value > 0) {
                pinColor = "#d9534f"
            } else {
                pinColor = "#0275d8"
            }
            var labelOriginHole = new google.maps.Point(12,15);
            var pinSVGHole = "M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z";
            var markerImage2 = {  // https://developers.google.com/maps/documentation/javascript/reference/marker#MarkerLabel
                    path: pinSVGHole,
                    anchor: new google.maps.Point(12,17),
                    fillOpacity: 1,
                    fillColor: pinColor,
                    strokeWeight: 2,
                    strokeColor: "white",
                    scale: 2,
                    labelOrigin: labelOriginHole
                };
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(lat_lng_obj.lat, lat_lng_obj.lng),
                map: map,
                icon: markerImage2,
            })

            var class_event_handler = new ClickEventHandler(map, origin, key, stations, areas);
            const input = document.getElementById("search-input-navbar");
            const searchBox = new google.maps.places.SearchBox(input);
            map_listen_click(map, stations, areas)
            listen_search(map, searchBox);
            map_listen_bounds(map, searchBox, stations, areas);
            function isIconMouseEvent(e) {
                console.log("place icon clicked")
                return "placeId" in e;
            }
        }
    })
}