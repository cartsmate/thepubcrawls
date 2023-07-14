function listen_bounds_changed(map, pubs_reviews) {
    console.log('listen_bounds_changed')
    google.maps.event.addListener(map, 'bounds_changed', function() {
        var bounds = map.getBounds();
        console.log(bounds)
        add_marker_bounds(map, bounds, pubs_reviews)
        });
//    return bounds
}

