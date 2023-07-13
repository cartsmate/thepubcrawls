function mapLoad(google_key) {
    console.log('map_load')
    var js = document.createElement("script");
    js.type = "text/javascript";
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
