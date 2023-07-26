function pubClick(pub) {
    console.log("pubClick")
    //station = document.getElementById('station_identity').value
    //console.log(station)
    //console.log(icon_list)

    var base_url = window.location.hostname
    //console.log('base_url')
    //console.log(base_url)
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub//"
    } else {
        var url = "http://" + base_url + ":5000/pub//"
    }

    const myUrlWithParams = new URL(url);
    //myUrlWithParams.searchParams.append('area', document.getElementById('area').value)
    myUrlWithParams.searchParams.append('pub_id', pub);

    window.location.replace(myUrlWithParams.href);
}
