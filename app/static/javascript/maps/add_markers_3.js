function add_markers_2(data) {
    console.log('add_markers_3')
    console.log('data')
    console.log(data)
    /*
    if (typeof map.markers !== "undefined") {
        for(var i=0; i < map.markers.length; i++){
            this.markers[i].setMap(null);
        }
        markers = []
    }
    */
    for (let i = 0; i < markersArray.length; i++) {
        markersArray[i].setMap(null);
        }
    markersArray = []
    //console.log(markersArray.length)
    //console.log(data.length)
    //var pinSVGHole = "M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z";
    //var labelOriginHole = new google.maps.Point(12,15);
    var pinSVGFilled = "M 12,2 C 8.1340068,2 5,5.1340068 5,9 c 0,5.25 7,13 7,13 0,0 7,-7.75 7,-13 0,-3.8659932 -3.134007,-7 -7,-7 z";
    var labelOriginFilled =  new google.maps.Point(12,9);
    var infowindow = new google.maps.InfoWindow();
    var marker, i, j;
    var bounds = new google.maps.LatLngBounds();
    //console.log(data)
    for (var key in data) {
        //console.log('key')
        //console.log(key)
        //console.log('data')
        //console.log(data)
        //console.log('data[key].count')
        //console.log(data[key].count)
        //var pinColor = data[key].colour
        var pinColor = "#0275d8"
        //console.log('colour: ' + pinColor)
        //if (true == false) {
        var pin = pinSVGFilled

        var label = {
            text: data[key].count.toString(),
            color: "white",
            fontSize: "12px",
        };
        /*
        } else {
            var pinHole = pinSVGHole
            var label = {
                text: " ",
                color: "white",
                fontSize: "1px",
            };
        }
        */
        var markerImage = {  // https://developers.google.com/maps/documentation/javascript/reference/marker#MarkerLabel
            path: pin,
            anchor: new google.maps.Point(12,17),
            fillOpacity: 1,
            fillColor: pinColor,
            strokeWeight: 2,
            strokeColor: "white",
            scale: 2,
            labelOrigin: labelOriginFilled
        };
        /*
        if (typeof data[key].name != "undefined") {
            title_name = data[key].pub_name
        } else {
            title_name = data[key].area_name
        }
        */

        marker = new google.maps.Marker({
            position: new google.maps.LatLng(data[key].pub_latitude, data[key].pub_longitude),
            map: map,
            icon: markerImage,
            label: label
        })

        google.maps.event.addListener(marker, 'click', (function (marker, key) {
            return function () {
                console.log('listener click')
                document.getElementById('x_station').value = data[key].station_identity.toString()
                document.getElementById('x_station_name').value = data[key].station_name.toString()
                click_station()
                }
            })(marker, key))
        /*
        google.maps.event.addListener(marker, 'click', (function (marker, key) {
            return function () {
                set=data[key].direction_identity.trim().replace(/%20/g, " ");
                infowindow.x = set;
                infowindow.setContent("<p><b>" + set + "</b></p>" +
                    "<a href='#' onclick='pub_click()'>" + set + "</a>");
                infowindow.open(map, marker);
                }
            })(marker, key));
        */
        markersArray.push(marker);
        var myLatLng = new google.maps.LatLng(data[key].pub_latitude, data[key].pub_longitude)
        bounds.extend(myLatLng);
        /*
        if (clickable == true) {
            if (true == false) {
                google.maps.event.addListener(marker, 'click', (function (marker, key) {
                    return function () {
                        set=data[key].area.trim().replace(/%20/g, " ");
                        console.log(data[key].area_name)
                        console.log(set)
                        infowindow.x = set;
                        infowindow.setContent("<p><b>" + set + "</b></p>" +
                            "<a href='/pub/list/area/" + set + "'>list of local venues</a>");
                        infowindow.open(map, marker);
                    }
                })(marker, key));
            } else {
                google.maps.event.addListener(marker, 'click', (function (marker, key) {
                    return function () {
                        infowindow.x = data[key].pub_name;
                        infowindow.setContent("<p><b>" + data[key].pub_name + "</b></p>" +
                            "<p>address : " + data[key].address + "</p>" +
                            "<p>category : " + data[key].category + "</p>" +
                            "<p>rank : " + data[key].rank + "</p>" +
                            "<p>station : " + data[key].station_name + "</p>" +
                            "<p>area : " + data[key].area_name + "</p>" +
                            "<a href='/pub/" + data[key].pub_identity + "'>click for more details</a>");
                        infowindow.open(map, marker);
                    }
                })(marker, key));
            }
        }
        */
    }
    //var bounds = new google.maps.LatLngBounds();
    //var myLatLng = new google.maps.LatLng(data[key].pub_latitude, data[key].pub_longitude)
    //bounds.extend(myLatLng);
    map.fitBounds(bounds);
    //add_marker_bounds(map, bounds, data)
    console.log(markersArray.length)
    console.log(data.length)
}
