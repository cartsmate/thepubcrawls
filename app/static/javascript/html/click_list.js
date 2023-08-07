function click_list(stations_directions_list) {

    console.log("click_list")

    document.getElementById('home_page').style.display = "none"

    document.getElementById('list_header').style.display = "block"
    document.getElementById('list_page1').style.display = "block"
    document.getElementById('list_page2').style.display = "block"
    document.getElementById('home_button').style.display = "block"

    document.getElementById('form_type').value = 'list'
    document.getElementById('auto_exec').value = 'on'

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
        option.text = "the nearest station"
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
    filtered_data = populate_test(all_data)
    update_data(filtered_data);

}


const groupBy = (arr, key) => arr.reduce((acc, item) => ((acc[item[key]] = [...(acc[item[key]] || []), item]), acc), {});
