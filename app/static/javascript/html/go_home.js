function go_home() {
    console.log("go_home")

    //document.getElementById('header_number').innerHTML = 'The Pub Crawls'
    /*
    document.getElementById('home_page').style.display = 'block'
    document.getElementById('list_header').style.display = 'none'
    document.getElementById('list_page1').style.display = 'none'
    document.getElementById('list_page2').style.display = 'none'
    document.getElementById('pub_read').style.display = 'none'
    */
    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/home/"
    } else {
        var url = "http://" + base_url + ":5000/home/"
    }
    const myUrlWithParams = new URL(url);

    window.location.replace(myUrlWithParams.href);
}
