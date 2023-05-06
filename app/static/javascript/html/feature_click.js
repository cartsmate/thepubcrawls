function featureClick(check_item) {
    var checkBox = document.getElementById(check_item);
    var image = document.getElementById(check_item + "_img");
    var caption = document.getElementById(check_item + "_caption");
    if (check_item == 'search') {
        var base_url = window.location.hostname
        var full_url = "http://" + base_url + ":5000/pub/search/"
        var full_url_prod = "http://" + base_url + "/pub/search/"
        const myUrlWithParams = new URL(full_url);
        //myUrlWithParams.searchParams.append("pet", pet.checked);

        myUrlWithParams.searchParams.append("tv", tv.checked);
        myUrlWithParams.searchParams.append("garden", garden.checked);
        myUrlWithParams.searchParams.append("music", music.checked);
        myUrlWithParams.searchParams.append("late", late.checked);
        myUrlWithParams.searchParams.append("meals", meals.checked);
        myUrlWithParams.searchParams.append("toilets", toilets.checked);
        myUrlWithParams.searchParams.append("cheap", cheap.checked);
        myUrlWithParams.searchParams.append("games", games.checked);

        console.log(myUrlWithParams.href);
        window.location.replace(myUrlWithParams.href);
    }
    if (checkBox.checked == true){
        //window.location.replace("/pub/list/" + check_item + "/True");
        image.style.opacity = "1.00"
        caption.style.opacity = "1.00"
    } else {
        image.style.opacity = "0.25"
        caption.style.opacity = "0.25"
    }
    //console.log(image)
}
