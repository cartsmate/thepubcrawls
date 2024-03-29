
function update_data(filtered_data) {
    console.log('UPDATE_DATA')

    delete_table()

    create_table(filtered_data)
    const [new_visible, new_order, new_asc_desc] = column_filter()
    filter_table(new_visible, new_order, new_asc_desc)

    if (window.navigator.onLine == true) {
        console.log('on-line')
        document.getElementById('no_wifi').style.display = "none";
        document.getElementById('no_map').style.display = "none";
        document.getElementById('map_areas').style.display = "none";
        document.getElementById('mapTEST').style.display = "block";
        filtered_data = limiting_data(filtered_data)
        console.log('filtered_data.length')
        console.log(filtered_data.length)
        if (filtered_data.length > 0 && filtered_data.length <= 50) {
            console.log('<= 50 pubs to show')
            add_markers(map, filtered_data)
        } else if (document.getElementById('x_direction').value == 'all') {
            console.log('all directions')
            json_array = calculate_directions_count(filtered_data)
            add_markers_2(map, json_array)
        } else {
            console.log('one direction')
            json_array_stations = calculate_stations_count(filtered_data)
            add_markers_3(map, json_array_stations)
        }
    } else {
        console.log('off-line')
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

    //map_visible(map, filtered_data, json_array, json_array_stations);

    header = update_header() + " (" + filtered_data.length + ")"
    document.getElementById('search_header').innerHTML = header
    document.getElementById('list_header').style.display = 'block'

}
