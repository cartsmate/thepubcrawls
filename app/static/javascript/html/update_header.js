function update_header() {
    console.log('UPDATE_HEADER')

    direction = document.getElementById('x_direction').value
    direction_name = document.getElementById('x_direction_name').value

    station = document.getElementById('x_station').value
    station_name = document.getElementById('x_station_name').value

    day = document.getElementById('x_day').value

    search = document.getElementById('x_search').value
    header = "Pubs"

    if (search != '') {
        header = header + " nearest " + search
    } else if (station != 'all') {
        header = station_name + " " + header
    } else if (direction != 'all') {
        header = direction_name + " " + header
    }
    if (day != 'all') {
        header = header + " on " + day
    }
    console.log(header)
    return header
}
