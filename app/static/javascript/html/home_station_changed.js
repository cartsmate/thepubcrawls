function home_station_changed() {
    console.log('HOME_STATION_CHANGED')
    console.log(stations_directions_list)
    var station_selection = document.getElementById('station').value
    //console.log(document.getElementById('station').value)
    //console.log(document.getElementById('station').text)
    var e = document.getElementById("station");
    var value = e.value;
    var text = e.options[e.selectedIndex].text;
    //console.log(text)

    document.getElementById("x_station").value = value
    document.getElementById("x_station_name").value = text

    new_direction_array = stations_directions_list.filter(item => item[0] == value)
    document.getElementById("x_direction").value = new_direction_array[0][2]
    document.getElementById("x_direction_name").value = new_direction_array[0][3]


    var desiredValue = new_direction_array[0][3]
    var el = document.getElementById("direction");
    for(var i=0; i<el.options.length; i++) {
      if ( el.options[i].text == desiredValue ) {
        el.selectedIndex = i;
        break;
      }
    }
}
