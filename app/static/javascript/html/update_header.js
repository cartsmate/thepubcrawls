function update_header() {
    console.log('update_header')

    direction = document.getElementById('x_direction_name').value
    station = document.getElementById('x_station_name').value
    day = document.getElementById('x_day').value
    header = "Pubs"
    console.log(header)
    if (station != 'all') {
        header = station + " " + header
    } else if (direction != 'all') {
        header = direction + " " + header
    }
    if (day != 'all') {
        header = header + " on " + day
    }
    console.log(header)
    return header
}
