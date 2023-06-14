function featureClick(check_item, auto_exec, features) {
    console.log("featureClick")
    console.log(check_item)
    console.log(auto_exec)
    var checkBox = document.getElementById(check_item);
    var image = document.getElementById(check_item + "_img");
    var caption = document.getElementById(check_item + "_caption");
    var checkCol = document.getElementById(check_item + "_col");
    if (checkBox.checked == true){
        //window.location.replace("/pub/list/" + check_item + "/True");
        image.style.opacity = "1.00"
        caption.style.opacity = "1.00"
        caption.style.color = "white"
        checkCol.style.background = "#0275D8"
    } else {
        image.style.opacity = "1.0"
        caption.style.opacity = "1.0"
        caption.style.color = "black"
        checkCol.style.background = "#CDCDCD"
    }
    if (auto_exec == 'on') {
        featureSearch(features)
    }
    /*
    if (auto_exec == 'on') {
        var base_url = window.location.hostname
        console.log(base_url)
        if (config2['env'] == 'prod') {
            var url = "http://" + base_url + "/pub/search/"
        } else {
            var url = "http://" + base_url + ":5000/pub/search/"
        }
        console.log(url)
        const myUrlWithParams = new URL(url);
        myUrlWithParams.searchParams.append("pet", pet.checked);
        myUrlWithParams.searchParams.append("tv", tv.checked);
        myUrlWithParams.searchParams.append("garden", garden.checked);
        myUrlWithParams.searchParams.append("music", music.checked);
        myUrlWithParams.searchParams.append("late", late.checked);
        myUrlWithParams.searchParams.append("meals", meals.checked);
        myUrlWithParams.searchParams.append("toilets", toilets.checked);
        myUrlWithParams.searchParams.append("cheap", cheap.checked);
        myUrlWithParams.searchParams.append("games", games.checked);
        myUrlWithParams.searchParams.append("quiz", quiz.checked);
        myUrlWithParams.searchParams.append("pool", pool.checked);
        myUrlWithParams.searchParams.append("lively", pool.checked);

        console.log(myUrlWithParams.href);
        window.location.replace(myUrlWithParams.href);
    }

    //console.log(image)
    */
}
