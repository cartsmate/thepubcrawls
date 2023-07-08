
function show_map(lat, lng, zoom, data) {
    console.log('show_map')
    var map = new google.maps.Map(document.getElementById('map'), {
            center: new google.maps.LatLng(lat, lng),
            zoom: zoom,
            mapTypeId: google.maps.MapTypeId.ROADMAP,
            mapTypeControl: false,
            streetViewControl: false
        });
    google.maps.event.addListener(map, 'bounds_changed', function() {
        //alert(map.getBounds());
        let bounds = map.getBounds();
        /*
        let ne = bounds.getNorthEast(); // Coords of the northeast corner
        let sw = bounds.getSouthWest(); // Coords of the southwest corner
            /*
            let nw = new google.maps.LatLng(ne.lat(), sw.lng()); // Coords of the NW corner
            let se = new google.maps.LatLng(sw.lat(), ne.lng()); // Coords of the SE corner
            console.log('ne: ' + ne.toString())
            console.log('sw: ' + sw.toString())
            console.log('nw: ' + nw.toString())
            console.log('se: ' + se.toString());
            console.log('n: ' + typeof ne);

        let north_east = ne.toString().replace(/[()]/g, "");
        var north_east_str = north_east.toString().split(',');
        let south_west = sw.toString().replace(/[()]/g, "");
        var south_west_str = south_west.toString().split(',');
        console.log('n: ' + north_east_str[0])
        console.log('e: ' + north_east_str[1])
        console.log('s: ' + south_west_str[0])
        console.log('w: ' + south_west_str[1])
            var bounds =  map.getBounds();
            var ne = bounds.getNorthEast();
            var sw = bounds.getSouthWest();
            console.log('ne: ' + ne)
            console.log('sw: ' + sw)
        */
        add_marker_bounds(map, data, bounds)
        //do whatever you want with those bounds
    });
    return map
}
