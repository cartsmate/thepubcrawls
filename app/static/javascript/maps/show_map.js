function show_map(lat, lng) {
    console.log('show_map')
    var map = new google.maps.Map(document.getElementById('map'), {
            center: new google.maps.LatLng(lat, lng),
            //zoom: zoom,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            mapTypeControl: false,
            streetViewControl: false
        });
        /*
    google.maps.event.addListener(map, 'bounds_changed', function() {
        let bounds = map.getBounds();
        add_marker_bounds(map, data, bounds)
    });
    */

    return map
}
