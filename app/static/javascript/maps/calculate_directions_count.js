function calculate_directions_count(filtered_data) {
    console.log('calculate_directions_count')
    group_by = groupBy(filtered_data, 'direction_identity')
    console.log(group_by)
    keys_list = Object.keys(group_by);

    var json_array = []
    for (i = 0; i < keys_list.length; i++) {
        var new_record = {}
        var key = Object.keys(group_by)[i];

        var directions = filtered_data.filter(function(pub) {
            return pub.direction_identity == keys_list[i]
            });
        var direction_lat = [], direction_lng = []
        for (j = 0; j < directions.length; j++) {
            direction_lat.push(directions[j]['pub_latitude'])
            direction_lng.push(directions[j]['pub_longitude'])
            }
        var sum_lat = direction_lat.reduce((a, b) => a + b, 0);
        var ave_lat = sum_lat / direction_lat.length

        var sum_lng = direction_lng.reduce((a, b) => a + b, 0);
        var ave_lng = sum_lng / direction_lng.length
        new_record = {"direction_identity": keys_list[i], "direction_name" : directions[0].direction_name, "pub_latitude" : ave_lat, "pub_longitude" : ave_lng, "count" : group_by[key].length}
        json_array.push(new_record)
        }
    //console.log(json_array)
    return json_array
}
