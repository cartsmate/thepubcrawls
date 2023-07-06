function listen_center(map) {
    console.log('listen_center')
    map.addListener('center_changed', function() {
        var newCenter = map.getCenter();
        console.log(newCenter.lat())
        console.log(newCenter.lng())
    })
}
