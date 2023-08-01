function populate_pub(filtered_data, id) {
    console.log('populate_pub')
    console.log('pub: ' + id)
    console.log('filtered_data: ' + filtered_data.length)

    var filtered_data = filtered_data.filter(function(pub) {
        return pub.pub_identity == id
        });

    return filtered_data
}