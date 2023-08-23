function update_data(filtered_data) {
    console.log('UPDATE_DATA')

    delete_table()

    create_table(filtered_data.slice(0, 50))
    const [new_visible, new_order, new_asc_desc] = column_filter()
    filter_table(new_visible, new_order, new_asc_desc)

    json_array = calculate_directions_count(filtered_data)
    json_array_stations = calculate_stations_count(filtered_data)
    map_visible(filtered_data, json_array, json_array_stations);

    header = update_header() + " (" + filtered_data.length + ")"
    document.getElementById('search_header').innerHTML = header
    document.getElementById('list_header').style.display = 'block'

}
