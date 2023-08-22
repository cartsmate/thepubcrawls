function show_map(lat, lng) {
    console.log('SHOW_MAP')
    var map = new google.maps.Map(document.getElementById('map'), {
        center: new google.maps.LatLng(lat, lng),
        //zoom: zoom,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: false,
        streetViewControl: false
    });
    return map
}
