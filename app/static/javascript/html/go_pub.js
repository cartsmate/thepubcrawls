function goPub() {
    console.log("goPub")
    selected_pub = document.getElementById('tags').value
    requested_postcode = document.getElementById('tags_postcode').value
    if (requested_postcode == "") {
        var base_url = window.location.hostname
        if (config2['env'] == 'prod') {
            var url = "http://" + base_url + "/pub/"
        } else {
            var url = "http://" + base_url + ":5000/pub/"
        }
        const myUrlWithParams = new URL(url);
        myUrlWithParams.searchParams.append('pub_id', selected_pub);
        myUrlWithParams.searchParams.append('direction', 'all');
        myUrlWithParams.searchParams.append('station', 'all');
        myUrlWithParams.searchParams.append('day', 'all');
        window.location.replace(myUrlWithParams.href);
    } else {
        codeAddress(requested_postcode)
    }
}
