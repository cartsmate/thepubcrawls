function show_map(lat, lng, mapLoc) {
    const LONDON_BOUNDS = {
        north: 51.68,
        south: 51.40,
        west: -0.549,
        east: 0.3,
    };
    console.log('SHOW_MAP')
    var map = new google.maps.Map(mapLoc, {
        center: new google.maps.LatLng(lat, lng),
//        zoom: 12,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: false,
        streetViewControl: false,
        restriction: {
            latLngBounds: LONDON_BOUNDS,
            strictBounds: false,
        }
    });
    console.log('map - in show_map')
    console.log(map)
    return map
}
