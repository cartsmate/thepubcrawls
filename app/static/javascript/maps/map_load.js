function mapLoad(google_key, form_type, station) {
    console.log('map_load')
    console.log('form_type: ' + form_type)
    console.log('station: ' + station)
    var js = document.createElement("script");
    js.type = "text/javascript";
    if (station != 'all' || form_type == 'home') {
        if ( window.navigator.onLine == true) {
            console.log('google map api')
            js.src = 'https://maps.googleapis.com/maps/api/js?key=' + google_key + '&libraries=places&callback=initMap'
            document.head.appendChild(js)
        } else {
            console.log('off line')
            var elem = document.createElement("img");
            elem.src = "/static/icons/no-wifi.png"
            elem.className = "fa-quora"
            elem.height = "100"
            document.getElementById('map').appendChild(elem);
        }
    } else {
        console.log('no map to be loaded')
        var elem = document.createElement("img");
        elem.src = "/static/icons/no-map.png"
        elem.className = "fa-quora"
        elem.height = "100"
        document.getElementById('map').appendChild(elem);
    }
}
