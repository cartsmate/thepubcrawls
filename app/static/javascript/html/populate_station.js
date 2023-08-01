function populate_station(filtered_data, station) {
    console.log('populate_station')
    var filtered_data = filtered_data.filter(function(pub) {
        return pub.station_identity == station
        });

    return filtered_data
}