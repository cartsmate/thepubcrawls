function populate_direction(filtered_data, direction) {
    console.log('populate_direction')
    var filtered_data = filtered_data.filter(function(pub) {
        return pub.direction_identity == direction
        });

    return filtered_data
}