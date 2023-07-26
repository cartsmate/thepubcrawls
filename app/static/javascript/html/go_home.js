function go_home() {
    console.log("go_home")
    /*
    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/home/"
    } else {
        var url = "http://" + base_url + ":5000/home/"
    }

    const myUrlWithParams = new URL(url);

    window.location.replace(myUrlWithParams.href);
    */
    document.getElementById('home_page').style.display = 'block'
    document.getElementById('header_page').style.display = 'none'
    document.getElementById('list_page1').style.display = 'none'
    document.getElementById('list_page2').style.display = 'none'
}
