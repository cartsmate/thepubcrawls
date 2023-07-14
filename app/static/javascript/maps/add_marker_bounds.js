function add_marker_bounds(map, bounds, data) {
    console.log('add_marker_bounds')
    //console.log(data)
    var labelOriginHole = new google.maps.Point(12,15);
    var pinSVGHole = "M12,11.5A2.5,2.5 0 0,1 9.5,9A2.5,2.5 0 0,1 12,6.5A2.5,2.5 0 0,1 14.5,9A2.5,2.5 0 0,1 12,11.5M12,2A7,7 0 0,0 5,9C5,14.25 12,22 12,22C12,22 19,14.25 19,9A7,7 0 0,0 12,2Z";
    //var pinSVGFilled = "M 12,2 C 8.1340068,2 5,5.1340068 5,9 c 0,5.25 7,13 7,13 0,0 7,-7.75 7,-13 0,-3.8659932 -3.134007,-7 -7,-7 z";
    var pinHole = pinSVGHole
    /*
    var label = {
        text: " ",
        color: "white",
        fontSize: "1px",
    };
    */
    let ne = bounds.getNorthEast(); // Coords of the northeast corner
    let sw = bounds.getSouthWest(); // Coords of the southwest corner
    let north_east = ne.toString().replace(/[()]/g, "");
    var north_east_str = north_east.toString().split(',');
    let south_west = sw.toString().replace(/[()]/g, "");
    var south_west_str = south_west.toString().split(',');
    var north = north_east_str[0]
    var south = south_west_str[0]
    var east = north_east_str[1]
    var west = south_west_str[1]
    for (var key in data) {

        //var pinColor = '#0275d8'
        var pinColor = data[key].colour
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
        /*
        if (data[key].pub_identity == '54ed8eb6-770a-4ed4-b269-a7c770447aed') {
            console.log('lat: ' + data[key].pub_latitude)
            console.log('north: ' + north_east_str[0])
            console.log('south: ' + south_west_str[0])
            console.log('lng: ' + data[key].pub_longitude)
            console.log('east: ' + north_east_str[1])
            console.log('west: ' + south_west_str[1])
        }
        */
        if (data[key].pub_latitude > south && data[key].pub_latitude < north && data[key].pub_longitude > west && data[key].pub_longitude < east) {
            console.log("inside if statement")
            marker = new google.maps.Marker({
                position: new google.maps.LatLng(data[key].pub_latitude, data[key].pub_longitude),
                map: map,
                icon: markerImage
            })
        }
    }
}
