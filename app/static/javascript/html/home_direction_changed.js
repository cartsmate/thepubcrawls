function home_direction_changed() {
    console.log('direction dropdown change')
    var directionSelect = document.getElementById("direction");
    var selectedText = directionSelect.options[directionSelect.selectedIndex].text;
    value = document.getElementById("direction").value
    //console.log(value)
    //console.log(selectedText)
    document.getElementById("station").selectedIndex = 0;
    //stations_directions_list = {{ stations_directions_list | tojson }}
    var select = document.getElementById("station");
    removeOptions(document.getElementById('station'));
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

    var e = document.getElementById("direction");
    var value = e.value;
    var text = e.options[e.selectedIndex].text;
    //console.log(text)
    document.getElementById("x_direction").value = value
    document.getElementById("x_direction_name").value = text
}
