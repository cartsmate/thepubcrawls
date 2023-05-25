function add_markers(map, zoom, data, clickable) {
    console.log('add_markers')
    console.log(zoom)
    var pinSVGHole = "M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z";
    var labelOriginHole = new google.maps.Point(12,15);
    var pinSVGFilled = "M 12,2 C 8.1340068,2 5,5.1340068 5,9 c 0,5.25 7,13 7,13 0,0 7,-7.75 7,-13 0,-3.8659932 -3.134007,-7 -7,-7 z";
    var labelOriginFilled =  new google.maps.Point(12,9);
    var infowindow = new google.maps.InfoWindow();
    var marker, i, j;
    for (var key in data) {
        //console.log(data[key])
        //var pinColor = data[key].colour
        var pinColor = data[key].colour
        //console.log(data[key])
        if (zoom < 15) {
            var pinHole = pinSVGFilled
            var label = {
                text: data[key].count,
                color: "white",
                fontSize: "12px",
            };
        } else {
            var pinHole = pinSVGHole
            var label = {
                text: " ",
                color: "white",
                fontSize: "1px",
            };
        }
        console.log(label)
        //console.log('label: ' + JSON.stringify(label))
        var markerImage = {  // https://developers.google.com/maps/documentation/javascript/reference/marker#MarkerLabel
            path: pinHole,
            anchor: new google.maps.Point(12,17),
            fillOpacity: 1,
            fillColor: pinColor,
            strokeWeight: 2,
            strokeColor: "white",
            scale: 2,
            labelOrigin: labelOriginFilled
        };
        if (typeof data[key].name != "undefined") {
            title_name = data[key].name
        } else {
            title_name = data[key].area
        }
        if (data[key].colour == '#d9534f' ) {
            var indie = 2
        } else {
            var indie = 1
        }
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(data[key].latitude, data[key].longitude),
            map: map,
            label: label,
            icon: markerImage,
            title: title_name,
            zIndex: indie
        })
        if (clickable == true) {
            if (zoom < 15) {
                google.maps.event.addListener(marker, 'click', (function (marker, key) {
                    return function () {
                        set=data[key].area.trim().replace(/%20/g, " ");
                        console.log(data[key].area)
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
                        infowindow.x = data[key].name;
                        infowindow.setContent("<p><b>" + data[key].name + "</b></p>" +
                            "<p>address : " + data[key].address + "</p>" +
                            "<p>category : " + data[key].category + "</p>" +
                            "<p>rank : " + data[key].rank + "</p>" +
                            "<p>best for : " + data[key].star + "</p>" +
                            "<p>station : " + data[key].station + "</p>" +
                            "<p>area : " + data[key].area + "</p>" +
                            "<a href='/pub/" + data[key].pub_identity + "'>click for more details</a>");
                        infowindow.open(map, marker);
                    }
                })(marker, key));
            }
        }
    }
    return marker
}
