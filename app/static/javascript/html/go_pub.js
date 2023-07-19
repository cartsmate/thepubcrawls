function goPub() {
    console.log("goPub")
    selected_pub = document.getElementById('tags').value
    requested_postcode = document.getElementById('tags_postcode').value
    if (requested_postcode == "") {
        alert("none")
        var base_url = window.location.hostname
        if (config2['env'] == 'prod') {
            var url = "http://" + base_url + "/pub/"
        } else {
            var url = "http://" + base_url + ":5000/pub/"
        }
        const myUrlWithParams = new URL(url + selected_pub);
        myUrlWithParams.searchParams.append('pub_id', selected_pub);
        myUrlWithParams.searchParams.append('zoom', zoom);
        window.location.replace(myUrlWithParams.href);
    } else {
        codeAddress(requested_postcode)

    }

}
