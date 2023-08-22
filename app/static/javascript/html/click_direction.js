function click_direction() {
    console.log("CLICK_DIRECTION")
    id = document.getElementById('x_direction').value
    /*
    delete_table()

    filtered_data = populate_test(all_data)

    json_array = calculate_directions_count(filtered_data)

    json_array_stations = calculate_stations_count(filtered_data)

    update_icons_list(filtered_data)

    create_table(filtered_data, alias)

    const new_visible, new_order = column_filter()

    filter_table(headers, new_visible, new_order)

    map_visible(filtered_data, json_array, json_array_stations);

    header = update_header() + " (" + filtered_data.length + ")"
    document.getElementById('search_header').innerHTML = header
    document.getElementById('list_header').style.display = 'block'
    */
    filtered_data = populate_test(all_data)

    update_data(filtered_data)

    update_icons_list(filtered_data)
}
