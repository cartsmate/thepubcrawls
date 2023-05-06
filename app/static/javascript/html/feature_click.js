function featureClick(check_item) {
    var checkBox = document.getElementById(check_item);
    var image = document.getElementById(check_item + "_img");
    var caption = document.getElementById(check_item + "_caption");
    if (check_item == 'search') {
        const myUrlWithParams = new URL("http://127.0.0.1:5000/pub/search/");
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
