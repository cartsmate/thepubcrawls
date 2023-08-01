function map_visible(filtered_data) {
    console.log('map_visible')

    if (window.navigator.onLine == true && filtered_data.length > 0 && filtered_data.length < 50) {
        document.getElementById('no_map').style.display = "none";
        document.getElementById('map').style.display = "block";
        //console.log(filtered_data.length)

        add_markers(map, filtered_data)
    } else {
        document.getElementById('map').style.display = "none";
        document.getElementById('no_map').style.display = "block";
        /*
        var elem = document.createElement("img");
        elem.src = "/static/icons/no-map.png"
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
