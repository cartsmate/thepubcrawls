function populate_pub(id) {
    console.log('populate_pub')
    //console.log('pub: ' + id)
    //console.log('filtered_data: ' + all_data.length)

    var filtered_data = all_data.filter(function(pub) {
        return pub.pub_identity == id
        });

    return filtered_data
}