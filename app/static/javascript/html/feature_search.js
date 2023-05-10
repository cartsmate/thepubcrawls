function featureSearch() {
    console.log("featureSearch")
    var base_url = window.location.hostname
    console.log(base_url)
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub/search/"
    } else {
        var url = "http://" + base_url + ":5000/pub/search/"
    }
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

    window.location.replace(myUrlWithParams.href);
}
