function add_listen_click(map) {
    var infowindow = new google.maps.InfoWindow();
    map.addListener('click', function (event) {
        // If the event is a POI
        if (event.placeId) {
            console.log('add_listen_click')
            console.log(event)
            // Call event.stop() on the event to prevent the default info window from showing.
            event.stop();
            infowindow.close();
            infowindow.setPosition(event.latLng);
            // do any other stuff you want to do
            console.log('You clicked on place:' + event.placeId + ', location: ' + event.latLng);
            // add pop up box with info and do you want to add this pub?
            infowindow.setContent(
                '<div>'
                + '<strong>Click the link to open the add pub page</strong>'
                + '<br>'
                + '<a href="/pub/add/' + event.latLng.lat() + '/' + event.latLng.lng() + '">Add Venue</a>'
                + '<br>'
                + '</div>');
            infowindow.open(map);
        }
    })
}
