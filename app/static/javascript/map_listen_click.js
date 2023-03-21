function map_listen_click(map, stations, marker) {

    map.addListener('click', function (event) {
        // If the event is a POI
        if (event.placeId) {
            console.log('map_listen_click')
            if (document.getElementById("submit").disabled = true) {
                document.getElementById("submit").disabled = false
            }
            // Call event.stop() on the event to prevent the default info window from showing.
            event.stop();
            document.getElementById("place").value = event.placeId;

            lat_lng_json = JSON.stringify(event.latLng.toJSON());
            var lat_lng_obj = JSON.parse(lat_lng_json);
            document.getElementById("latitude").value = lat_lng_obj.lat;
            document.getElementById("longitude").value = lat_lng_obj.lng;
            records = []
            for (let i = 0; i < stations.length; i++) {
                lat_diff = Math.abs(stations[i]['latitude'] - lat_lng_obj.lat)
                lng_diff = Math.abs(stations[i]['longitude'] - lat_lng_obj.lng)
                tot_diff = lat_diff + lng_diff
                var record = { name: stations[i]['station'], id: stations[i]['station_identity'], distance: tot_diff}
                records.push(record);
            }
            records = records.sort((a, b) => {
                if (a.distance < b.distance) {
                    return -1;
                }
            });
            document.getElementById("station").value = records[0]['name']
            document.getElementById("station_identity").value = records[0]['id']

            map.setCenter(event.latLng)

            map = show_map(lat_lng_obj.lat, lat_lng_obj.lng, map.getZoom())
            if (document.getElementById('score').value > 0) {
                pinColor = "#FF0000"
            } else {
                pinColor = "#553D67"
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
            map_listen_click(map, stations, marker)

        }
    })
}