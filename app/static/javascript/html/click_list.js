function click_list(stations_directions_list) {

    console.log("click_list")
    //console.log('stations_directions_list: ' + stations_directions_list)
    document.getElementById('home_page').style.display = "none"
    document.getElementById('list_header').style.display = "block"
    document.getElementById('list_page1').style.display = "block"
    document.getElementById('list_page2').style.display = "block"

    document.getElementById('form_type').value = 'list'
    document.getElementById('auto_exec').value = 'on'

    document.getElementById("direction_2").value = document.getElementById("x_direction").value;
    if (document.getElementById("direction_2").value == 'all') {
        document.getElementById("station_2").value = document.getElementById("x_station").value;
    } else {
        console.log('direction_changed_2')
        var directionSelect = document.getElementById("direction_2");
        var selectedText = directionSelect.options[directionSelect.selectedIndex].text;
        value = document.getElementById("direction_2").value
        //console.log(value)
        //console.log(selectedText)
        document.getElementById("station_2").selectedIndex = 0;

        var select = document.getElementById("station_2");
        removeOptions(document.getElementById('station_2'));
        var option = document.createElement("option");
        option.value = 'all'
        option.text = "the nearest station"
        select.add(option);
        if (value == 'all') {
            for(var i = 0; i < stations_directions_list.length; i++) {
                var opt = stations_directions_list[i][1];
                var el = document.createElement("option");
                el.textContent = stations_directions_list[i][1];
                el.value = stations_directions_list[i][0];
                select.appendChild(el);
            }
        } else {
            filteredArray = stations_directions_list.filter(item => item[2] == value);
            for(var i = 0; i < filteredArray.length; i++) {
                var opt = filteredArray[i][1];
                var el = document.createElement("option");
                el.textContent = filteredArray[i][1];
                el.value = filteredArray[i][0];
                select.appendChild(el);
            }
        }

        var e = document.getElementById("direction_2");
        var value = e.value;
        var text = e.options[e.selectedIndex].text;
        //console.log(text)
        document.getElementById("x_direction").value = value
        document.getElementById("x_direction_name").value = text
    }


    /*
    review_list = ['brunch','dart','entertain','favourite','garden','history','late','music','pool','quiz','roast','sport']
    for (let i = 0; i < review_list.length; i++) {
        var image = document.getElementById(review_list[i] + "_img_2");
        var caption = document.getElementById(review_list[i] + "_caption_2");
        var checkCol = document.getElementById(review_list[i] + "_col_2");
        if (document.getElementById("x_" + review_list[i]).value == 'true'){
            //console.log(review_list[i] + ' : TRUE')
            image.style.opacity = "1"
            caption.style.opacity = "1.0"
            caption.style.color = "white"
            checkCol.style.background = "#0275D8"
            //checkCol.style.border = "thick solid #0275D8";
        } else {
            //console.log(review_list[i] + ' : FALSE')
            image.style.opacity = "1"
            caption.style.opacity = "1.0"
            caption.style.color = "black"
            checkCol.style.background = "#CDCDCD"
        }
    }
    week_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    for (let i = 0; i < week_list.length; i++) {
        var image = document.getElementById(week_list[i] + "_img_2");
        if (document.getElementById(week_list[i] + "_2").value == document.getElementById("x_day").value) {
            //console.log(week_list[i] + '_2 : TRUE')
            image.style.opacity = "1.0"
        } else {
            //console.log(week_list[i] + '_2 : FALSE')
            image.style.opacity = "0.5"
        }
    }
    */
    delete_table()
    filtered_data = populate_test(all_data)
    update_features_icons(filtered_data)
    create_table(filtered_data, alias)
    visible, order = column_filter()
    filter_table(headers, visible, order)
    var markersArray = []
    map_visible(filtered_data, markersArray);
    header = update_header() + " (" + filtered_data.length + ")"
    document.getElementById('search_header').innerHTML = header
    document.getElementById('list_header').style.display = 'block'
}
