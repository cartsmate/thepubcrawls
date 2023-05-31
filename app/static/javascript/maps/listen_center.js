
function listen_center(map) {
    map.addListener('center_changed', function() {
        console.log('center_change')
        var newCenter = map.getCenter();
        console.log(newCenter.lat())
        console.log(newCenter.lng())
    })
}
