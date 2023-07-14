function mapLoad(google_key, station) {
    console.log('map_load')
    //console.log(station)
    var js = document.createElement("script");
    js.type = "text/javascript";
    if (station == 'all') {
        var elem = document.createElement("img");
        elem.src = "/static/icons/no-map.png"
        elem.className = "fa-quora"
        elem.height = "100"
        document.getElementById('map').appendChild(elem);
    } else {
        if ( window.navigator.onLine == true) {
            js.src = 'https://maps.googleapis.com/maps/api/js?key=' + google_key + '&libraries=places&callback=initMap'
            document.head.appendChild(js)
        } else {
            var elem = document.createElement("img");
            elem.src = "/static/icons/no-wifi.png"
            elem.className = "fa-quora"
            elem.height = "100"
            document.getElementById('map').appendChild(elem);
        }
    }
}
