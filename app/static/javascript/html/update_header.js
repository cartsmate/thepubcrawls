function update_header() {
    console.log('update_header')

    direction = document.getElementById('x_direction').value
    direction_name = document.getElementById('x_direction_name').value
    console.log('direction')
    console.log(direction)
    station = document.getElementById('x_station').value
    station_name = document.getElementById('x_station_name').value
    console.log('station')
    console.log(station)
    day = document.getElementById('x_day').value
    header = "Pubs"
    console.log(header)
    if (station != 'all') {
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
