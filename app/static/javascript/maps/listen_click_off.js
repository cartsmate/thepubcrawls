function listen_click_off(map) {
    map.addListener('click', function (event) {
        // If the event is a POI
        if (event.placeId) {
            // console.log('listen_click_off')
            console.log(event)
            // Call event.stop() on the event to prevent the default info window from showing.
            event.stop();
    })
}
