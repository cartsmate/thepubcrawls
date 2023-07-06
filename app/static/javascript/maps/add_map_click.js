function add_map_click(map) {
    console.log('add_map_click')
    map.addListener('click', function (event) {
        if (isIconMouseEvent(event)) {
            console.log('you clicked on the map')
            // Call event.stop() on the event to prevent the default info window from showing.
            event.stop();
            window.location.href = "/pub/map/all"
        }
    })
}
