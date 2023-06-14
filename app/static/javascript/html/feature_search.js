function featureSearch(features) {
    console.log("featureSearch")

    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub/search/"
    } else {
        var url = "http://" + base_url + ":5000/pub/search/"
    }

    const myUrlWithParams = new URL(url);
    for (var i = 0; i < features.length; i++) {
        myUrlWithParams.searchParams.append(features[i], document.getElementById(features[i]).checked);
    }
    window.location.replace(myUrlWithParams.href);
}
