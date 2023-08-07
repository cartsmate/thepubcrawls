function station_click() {
    console.log("station_click")
    document.getElementById('pub_read').style.display = 'none'

    document.getElementById('brunch').value = 'false'
    document.getElementById('dart').value = 'false'
    document.getElementById('entertain').value = 'false'
    document.getElementById('favourite').value = 'false'
    document.getElementById('garden').value = 'false'
    document.getElementById('history').value = 'false'
    document.getElementById('late').value = 'false'
    document.getElementById('music').value = 'false'
    document.getElementById('pool').value = 'false'
    document.getElementById('quiz').value = 'false'
    document.getElementById('roast').value = 'false'
    document.getElementById('sport').value = 'false'

    document.getElementById('list_header').style.display = 'block'
    document.getElementById('list_page1').style.display = 'block'
    document.getElementById('list_page2').style.display = 'block'
    document.getElementById('station_button').style.display = 'none'
    filtered_data = populate_test(all_data)
    update_data(filtered_data)

    /*
    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/home/"
    } else {
        var url = "http://" + base_url + ":5000/home/"
    }
    */

    //document.getElementById("x_station").value = station_identity
    //var drop1 = document.getElementById("station");
    //drop1.value = station_identity
    /*
    for (iLoop = 0; iLoop< stations_directions_list.length; iLoop++)
    {
      if (stations_directions_list[iLoop][0] == station_identity)
      {
        // Item is found. Set its selected property, and exit the loop
        //document.getElementById('station_2').selectedIndex = (iLoop + 1)
        document.getElementById('station_2').value = station_identity
        //myDropdownList.options[iLoop].selected = true;
        break;
      }
    }
    */
    //document.getElementById("x_station_name").value = stations_directions_list[iLoop][1]

    /*
    delete_table()
    station_identity = document.getElementById("x_station").value
    filtered_data = populate_station(all_data, station_identity)
    json_array = calculate_directions_count(filtered_data)
    update_features_icons(filtered_data)
    create_table(filtered_data, alias)
    visible, order = column_filter()
    filter_table(headers, visible, order)
    map_visible(filtered_data, json_array);
    header = update_header() + " (" + filtered_data.length + ")"
    document.getElementById('search_header').innerHTML = header
    document.getElementById('list_header').style.display = 'block'
    */

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
