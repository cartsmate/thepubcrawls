
function codeAddress(address) {
    console.log("code_address")
    geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address}, function(results, status) {
        if (status == 'OK') {
            var lat = results[0].geometry.location.lat()
            var lng = results[0].geometry.location.lng()
            var base_url = window.location.hostname
            if (config2['env'] == 'prod') {
                var url = "http://" + base_url + "/pub/list/"
            } else {
                var url = "http://" + base_url + ":5000/pub/list/"
            }
            const myUrlWithParams = new URL(url + selected_pub);
            myUrlWithParams.searchParams.append('direction', 'all');
            myUrlWithParams.searchParams.append('station', 'all');
            myUrlWithParams.searchParams.append('day', 'all');
            myUrlWithParams.searchParams.append('lat', lat);
            myUrlWithParams.searchParams.append('lng', lng);
            window.location.replace(myUrlWithParams.href);
        } else {
            alert('Geocode was not successful for the following reason: ' + status);
        }
    });
}
