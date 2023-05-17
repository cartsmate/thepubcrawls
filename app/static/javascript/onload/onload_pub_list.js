function onLoad() {
    console.log("onLoad in pub_list");
    filter = {{ filter | tojson }}
    var header_listing = String(filter['0']).toUpperCase() + String(filter).substring(1)
    document.getElementById("header_listing").innerHTML = "<h2>" + header_listing + "</h2>"
    var map_lat = {{ map_lat | tojson }}
    var map_lng = {{ map_lng | tojson }}
    var map_view = {{ map_view | tojson }}
    pubs_reviews = {{ pubs_reviews | tojson }};
    list_type = {{ list_type | tojson }}
    id_type = {{ id_type | tojson }}
    if (list_type == 'area') {
        console.log('area')
        Area()
    } else {
        console.log('NOT area')
        Category()
    }
}
