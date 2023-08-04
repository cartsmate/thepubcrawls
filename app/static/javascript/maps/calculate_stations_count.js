function calculate_stations_count(filtered_data) {
    console.log('calculate_stations_count')
    group_by = groupBy(filtered_data, 'station_identity')
    //console.log(group_by)
    keys_list = Object.keys(group_by);

    var json_array = []
    for (i = 0; i < keys_list.length; i++) {
        var new_record = {}
        var key = Object.keys(group_by)[i];

        var stations = filtered_data.filter(function(pub) {
            return pub.station_identity == keys_list[i]
            });
        var station_lat = [], station_lng = []
        for (j = 0; j < stations.length; j++) {
            station_lat.push(stations[j]['pub_latitude'])
            station_lng.push(stations[j]['pub_longitude'])
            }
        var sum_lat = station_lat.reduce((a, b) => a + b, 0);
        var ave_lat = sum_lat / station_lat.length

        var sum_lng = station_lng.reduce((a, b) => a + b, 0);
        var ave_lng = sum_lng / station_lng.length
        new_record = {"station_identity": keys_list[i], "station_name" : stations[0].station_name, "pub_latitude" : ave_lat, "pub_longitude" : ave_lng, "count" : group_by[key].length}
        json_array.push(new_record)
        }
    //console.log(json_array)
    return json_array
}
