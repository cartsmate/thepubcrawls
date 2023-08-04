function click_direction() {
    console.log("click_direction")
    id = document.getElementById('x_direction').value
    console.log(id)
    delete_table()

    filtered_data = populate_test(all_data)

    json_array = calculate_directions_count(filtered_data)

    json_array_stations = calculate_stations_count(filtered_data)

    update_features_icons(filtered_data)

    create_table(filtered_data, alias)

    visible, order = column_filter()

    filter_table(headers, visible, order)

    map_visible(filtered_data, json_array, json_array_stations);

    header = update_header() + " (" + filtered_data.length + ")"
    document.getElementById('search_header').innerHTML = header
    document.getElementById('list_header').style.display = 'block'
}