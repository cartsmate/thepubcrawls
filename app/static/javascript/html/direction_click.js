function direction_click(direction) {
    console.log("direction_click")
    /*
    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/home/"
    } else {
        var url = "http://" + base_url + ":5000/home/"
    }
    */
    delete_table()
    filtered_data = populate_direction(all_data, direction)
    update_features_icons(filtered_data)
    create_table(filtered_data, alias)
    visible, order = column_filter()
    filter_table(headers, visible, order)
    map_visible(filtered_data);
    header = update_header() + " (" + filtered_data.length + ")"
    document.getElementById('search_header').innerHTML = station + " Pubs"
    document.getElementById('list_header').style.display = 'block'
    /*
    //station = document.getElementById('station_identity').value
    //console.log(station)
    //console.log(icon_list)
    delete_table()

    filtered_data = populate_station(station)

    review_list = ['brunch','dart','entertain','favourite','garden','history','late','music','pool','quiz','roast','sport']
    for (let i = 0; i < review_list.length; i++) {
        var image = document.getElementById(review_list[i] + "_img_2");
        var caption = document.getElementById(review_list[i] + "_caption_2");
        var checkCol = document.getElementById(review_list[i] + "_col_2");
        var count = filtered_data.filter(function (el) {
            return el[review_list[i]] == true;
        }).length;
        if (count == filtered_data.length) {
            //image.style.opacity = "1"
            //caption.style.opacity = "1"
            checkCol.style.border = "thick solid #0275D8";
            checkCol.style.background = "#0275D8"
            caption.style.color = "white"
        } else if (count > 0) {
            checkCol.style.border = "thick solid #0275D8";
        } else {
            checkCol.style.border = "thick solid #BCBCBC";
            checkCol.style.background = "#BCBCBC"
            caption.style.color = "black"
        }
    }

    create_table(filtered_data, alias)

//    for (let i = 0; i < diary_headers.length; i++) {
//            visible[diary_headers[i]] = true
//            }
        //visible.rank = false
    visible.station_name = false
    const isIndex = (element) => element == 'rank';
    order = headers.findIndex(isIndex);
    Search(headers, visible, order)

    map_visible(filtered_data);

    document.getElementById('x_station').value = station

    document.getElementById("direction_2").value = document.getElementById("x_direction").value;
    document.getElementById("station_2").value = document.getElementById("x_station").value;

    var ele = document.getElementsByName('radio');
    for (i = 0; i < ele.length; i++) {
        if (ele[i].checked)
            day = ele[i].value;
    }
    var base_url = window.location.hostname
    //console.log('base_url')
    //console.log(base_url)
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub/list/"
    } else {
        var url = "http://" + base_url + ":5000/pub/list/"
    }

    const myUrlWithParams = new URL(url);
    //myUrlWithParams.searchParams.append('area', document.getElementById('area').value)
    myUrlWithParams.searchParams.append('direction', 'all');
    myUrlWithParams.searchParams.append('station', station);
    myUrlWithParams.searchParams.append('day', day);
    for (var i = 0; i < icon_list.length; i++) {
        console.log(icon_list[i])
        console.log(document.getElementById(icon_list[i]).checked)
        myUrlWithParams.searchParams.append(icon_list[i], 'false');
    }
    window.location.replace(myUrlWithParams.href);
    */
}
