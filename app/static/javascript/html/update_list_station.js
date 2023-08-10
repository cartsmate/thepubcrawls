function update_list_station() {
    console.log('update_list_station')
    document.getElementById("direction_2").value = document.getElementById("x_direction").value;
    if (document.getElementById("direction_2").value == 'all') {
        document.getElementById("station_2").value = document.getElementById("x_station").value;
    } else {
        console.log('direction_changed_2')
        var directionSelect = document.getElementById("direction_2");
        var selectedText = directionSelect.options[directionSelect.selectedIndex].text;
        value = document.getElementById("direction_2").value

        document.getElementById("station_2").selectedIndex = 0;

        var select = document.getElementById("station_2");
        removeOptions(document.getElementById('station_2'));
        var option = document.createElement("option");
        option.value = 'all'
        option.text = "Tube/Train Station"
        select.add(option);
        if (value == 'all') {
            for(var i = 0; i < stations_directions_list.length; i++) {
                var opt = stations_directions_list[i][1];
                var el = document.createElement("option");
                el.textContent = stations_directions_list[i][1];
                el.value = stations_directions_list[i][0];
                select.appendChild(el);
            }
        } else {
            filteredArray = stations_directions_list.filter(item => item[2] == value);
            for(var i = 0; i < filteredArray.length; i++) {
                var opt = filteredArray[i][1];
                var el = document.createElement("option");
                el.textContent = filteredArray[i][1];
                el.value = filteredArray[i][0];
                select.appendChild(el);
            }
        }
        var e = document.getElementById("direction_2");
        var value = e.value;
        var text = e.options[e.selectedIndex].text;
        document.getElementById("x_direction").value = value
        document.getElementById("x_direction_name").value = text
    }

}
