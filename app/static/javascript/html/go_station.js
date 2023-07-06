function goStation(direction, station) {
    console.log("goStation")
    console.log(direction)
    console.log(station)

    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub/add/"
    } else {
        var url = "http://" + base_url + ":5000/pub/add/"
    }

    const myUrlWithParams = new URL(url);
    myUrlWithParams.searchParams.append('direction', direction);
    myUrlWithParams.searchParams.append('station', station);
    /*
    for (var i = 0; i < icon_list.length; i++) {
        console.log(icon_list[i])
        console.log(document.getElementById(icon_list[i]).checked)
        myUrlWithParams.searchParams.append(icon_list[i], document.getElementById(icon_list[i]).checked);
    }
    */
    window.location.replace(myUrlWithParams.href);
}
