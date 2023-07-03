function stationClick(station) {
    console.log("stationClick")
    console.log(icon_list)
    var base_url = window.location.hostname
    console.log('base_url')
    console.log(base_url)
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub/list/"
    } else {
        var url = "http://" + base_url + ":5000/pub/list/"
    }

    const myUrlWithParams = new URL(url);
    //myUrlWithParams.searchParams.append('area', document.getElementById('area').value)
    myUrlWithParams.searchParams.append('direction', 'all');
    myUrlWithParams.searchParams.append('station', station);
    for (var i = 0; i < icon_list.length; i++) {
        console.log(icon_list[i])
        console.log(document.getElementById(icon_list[i]).checked)
        myUrlWithParams.searchParams.append(icon_list[i], 'false');
    }
    window.location.replace(myUrlWithParams.href);
}
