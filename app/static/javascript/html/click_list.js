function click_list() {
    console.log("CLICK_LIST")
    document.getElementById('x_search').value = document.getElementById('search-input-navbar').value
    document.getElementById('search-output-navbar').value = document.getElementById('x_search').value
    page_layout('list')
    document.getElementById('auto_exec').value = 'on'
    update_list_station()

    console.log('x_search')
    var inputAddress = document.getElementById('x_search').value
    console.log(inputAddress)
    if (inputAddress != '') {
        code_address(inputAddress)
    } else {
        go_update(all_data)
    }

    var day = document.getElementById('x_day').value
    if (day != 'all') {
        var checkBox = document.getElementById("btn_" + day + "_2")
        checkBox.checked == true
        var imageBox = document.getElementById(day + "_img_2")
        imageBox.style.opacity = "1"
    }

    //alert(document.getElementById('search-input-navbar').value)
}

const groupBy = (arr, key) => arr.reduce((acc, item) => ((acc[item[key]] = [...(acc[item[key]] || []), item]), acc), {});

function code_address(address) {
    console.log('CODE_ADDRESS')
    //var address = document.getElementById('address').value;
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address}, function(results, status) {
        if (status == 'OK') {
            /*
            map.setCenter(results[0].geometry.location);
            var marker = new google.maps.Marker({
                map: map,
                position: results[0].geometry.location
            });
            */
            var loc_lat = results[0].geometry.location.lat()
            var loc_lng = results[0].geometry.location.lng()
            //filtered_data = all_data
            for(const element of all_data) {
                element['distance'] = (Math.abs(element.pub_latitude - loc_lat)) + (Math.abs(element.pub_longitude - loc_lng))
            }
            //filtered_data = all_data
            go_update(all_data)

        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}

function go_update(data) {
    filtered_data = populate_test(data)

    update_data(filtered_data)

    update_icons_list(filtered_data)
}

function get_coordinates(address, fn){
    var geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address}, function(results, status) {
        fn(results[0].geometry.location);
    });
}

function do_complete(loc_lat, loc_lng) {
    alert('loc_lat: out: ' + loc_lat)
    alert('loc_lng: out: ' + loc_lng)
    for(const element of filtered_data) {
        element['distance'] = (Math.abs(element.pub_latitude - loc_lat)) + (Math.abs(element.pub_longitude - loc_lng))
    }
    return filtered_data
}
