function map_load(google_key) {
    console.log('MAP_LOAD')
    //console.log(google_key)
    var js = document.createElement("script");
    js.type = "text/javascript";
    console.log('window.navigator.onLine')
    console.log(window.navigator.onLine)
    var on_line = 'false'
    if (window.navigator.onLine == true) {
        console.log('on-line')
        js.setAttribute("defer", "defer");
        var google_string = 'https://maps.googleapis.com/maps/api/js?key=' + google_key + '&libraries=places&callback=initMap'
        console.log('google_string')
        console.log(google_string)
        js.src = google_string
        document.head.appendChild(js)
        //document.getElementById('search_map').style.display = 'block'
        //add_markers(all_data)
        on_line = 'true'
        console.log(on_line)
    } else {
        console.log('off-line')
        var elem = document.createElement("img");
        elem.src = "/static/icons/no-wifi.png"
        elem.setAttribute("id", ",map_img");
        elem.className = "fa-quora"
        elem.height = "100"
        //document.getElementById('search_map').style.display = 'none'
        //document.getElementById('map').appendChild(elem);
    }
    return on_line
}
