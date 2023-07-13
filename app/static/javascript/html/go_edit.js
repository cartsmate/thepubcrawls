function goEdit(selected_pub, zoom) {
    console.log("goEdit")
    console.log(selected_pub)

    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub/edit/"
    } else {
        var url = "http://" + base_url + ":5000/pub/edit/"
    }
    const myUrlWithParams = new URL(url);
    myUrlWithParams.searchParams.append('pub_id', selected_pub);
    myUrlWithParams.searchParams.append('zoom', zoom);
//    window.location.href = url + selected_pub
    window.location.replace(myUrlWithParams.href);
    /*

    myUrlWithParams.searchParams.append('direction', document.getElementById('direction').value);

    for (var i = 0; i < icon_list.length; i++) {
        console.log(icon_list[i])
        console.log(document.getElementById(icon_list[i]).checked)
        myUrlWithParams.searchParams.append(icon_list[i], document.getElementById(icon_list[i]).checked);
    }
    window.location.replace(myUrlWithParams.href);
    */
}
