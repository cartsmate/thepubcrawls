function update_list_station() {
    console.log('UPDATE_LIST_STATION')

    var select = document.getElementById("direction_2");
    removeOptions(document.getElementById('direction_2'));
    var option = document.createElement("option");
    option.value = 'all'
    option.text = "Area"
    select.add(option);
    for(var i = 0; i < directions_list.length; i++) {
        var opt = directions_list[i][3];
        var el = document.createElement("option");
        el.textContent = directions_list[i][1];
        el.value = directions_list[i][0];
        select.appendChild(el);
    }
    var desired_direction = document.getElementById("x_direction_name").value;
    console.log('desired_direction')
    console.log(desired_direction)
    if (desired_direction == 'all') {
        document.getElementById("direction_2").selectedIndex = 0;
    } else {
        var el = document.getElementById("direction_2");
        for(var i=0; i<el.options.length; i++) {
            if ( el.options[i].text == desired_direction ) {
                el.selectedIndex = i;
                break;
            }
        }
    }

    var select = document.getElementById("station_2");
    removeOptions(document.getElementById('station_2'));
    var option = document.createElement("option");
    option.value = 'all'
    option.text = "Tube/Train Station"
    select.add(option);
    for(var i = 0; i < stations_directions_list.length; i++) {
        var opt = stations_directions_list[i][1];
        var el = document.createElement("option");
        el.textContent = stations_directions_list[i][1];
        el.value = stations_directions_list[i][0];
        select.appendChild(el);
    }
    var desired_station = document.getElementById("x_station_name").value;
    console.log('desired_station')
    console.log(desired_station)
    if (desired_station == 'all') {
        document.getElementById("station_2").selectedIndex = 0;
    } else {
        var el = document.getElementById("station_2");
        for(var i=0; i<el.options.length; i++) {
            if ( el.options[i].text == desired_station ) {
                el.selectedIndex = i;
                break;
            }
        }
    }

}
