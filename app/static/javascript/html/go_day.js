function go_day(day) {
    console.log("go_day")
    console.log('day')
    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub/day/"
    } else {
        var url = "http://" + base_url + ":5000/pub/day/"
    }
    const myUrlWithParams = new URL(url);
    myUrlWithParams.searchParams.append('day', day);
    window.location.replace(myUrlWithParams.href);
}
