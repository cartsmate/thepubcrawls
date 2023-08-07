function map_visible(filtered_data, json_array, json_array_stations) {
    console.log('map_visible')

    if (window.navigator.onLine == true) {
        document.getElementById('no_wifi').style.display = "none";
        document.getElementById('no_map').style.display = "none";
        document.getElementById('map_areas').style.display = "none";
        document.getElementById('map').style.display = "block";
        if (filtered_data.length > 0 && filtered_data.length < 50) {
            add_markers(filtered_data)
        } else if (document.getElementById('x_direction').value == 'all') {
            console.log('all directions')
            add_markers_2(json_array)
        } else {
            console.log('one directions')
            add_markers_3(json_array_stations)
        }
    } else {
        document.getElementById('no_wifi').style.display = "block";
        document.getElementById('map').style.display = "none";
        document.getElementById('map_areas').style.display = "none";
        document.getElementById('no_map').style.display = "none";
        /*
        console.log('no map - too many pubs')
        var elem = document.createElement("img");
        elem.src = "/static/icons/no-map.png"
        elem.setAttribute("id", "map_img");
        elem.className = "fa-quora"
        elem.height = "100"
        document.getElementById('map').appendChild(elem);
        */
    }
}

function clearOverlays() {
  for (var i = 0; i < markersArray.length; i++ ) {
    markersArray[i].setMap(null);
  }
  markersArray.length = 0;
}
