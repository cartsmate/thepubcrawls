//function listen_zoom(map, pubs_reviews) {
//
//    map.addListener('zoom_changed', function() {
//        var newZoom = map.getZoom();
//        console.log('listen_zone')
//        document.getElementById('panel').innerHTML  = "<p>" + newZoom + "</p>";
//    });
//}

function listen_zoom(map, summary, full) {
    map.addListener('center_changed', function() {
        console.log('center_change')
    })
    map.addListener('zoom_changed', function() {
        var newZoom = map.getZoom();
        showMap(summary, full, map.getZoom(), map.getCenter().lat(), map.getCenter().lng())
    });
}
