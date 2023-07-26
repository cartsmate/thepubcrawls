function map_listen_click(map, data) {
    console.log('map_listen_click')
    map.addListener('click', function (event) {
        // If the event is a POI
        if (event.placeId) {

            var request = {
                placeId: event.placeId,
                fields: ['name','formatted_address','rating','reviews','user_ratings_total','editorial_summary']
            };
            var service = new google.maps.places.PlacesService(map);
            service.getDetails(request, function(place, status) {
                if (status === google.maps.places.PlacesServiceStatus.OK) {
                    var reviews = place.reviews;
                    console.log(place.rating)
                    if (place.rating === undefined) {
                            console.log('undefined')
                            var ranking = 0
                        } else {
                            console.log(place.rating)
                            var ranking = place.rating
                        }
                    document.getElementById("rank").value = ranking
                    //console.log(place.editorial_summary)
                    document.getElementById("pub_name").value = place.name
                    document.getElementById("address").value = place.formatted_address
                    shadeStars('rank', ranking, 'map')
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

            //map = show_map(lat_lng_obj.lat, lat_lng_obj.lng)

            pinColor = "#0275d8"
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
            const center = new google.maps.LatLng(lat_lng_obj.lat, lat_lng_obj.lng);
            window.map.panTo(center);


        }
    })
}