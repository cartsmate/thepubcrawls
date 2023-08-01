function map_load(google_key) {
    console.log('map_load')
    //console.log(google_key)
    var js = document.createElement("script");
    js.type = "text/javascript";
    if (window.navigator.onLine == true) {
        console.log('google map api')
        js.setAttribute("defer", "defer");
        js.src = 'https://maps.googleapis.com/maps/api/js?key=' + google_key + '&libraries=places&callback=initMap'
        //js.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyCbb6tdoROEQuBKLZXybG5cNIB4UTc6A20&libraries=places&callback=initMap'
        document.head.appendChild(js)
    } else {
        console.log('off line')
        var elem = document.createElement("img");
        elem.src = "/static/icons/no-wifi.png"
        elem.setAttribute("id", ",map_img");
        elem.className = "fa-quora"
        elem.height = "100"
        document.getElementById('map').appendChild(elem);
    }
}
