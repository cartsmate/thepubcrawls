function pub_click(id) {
    console.log("pub_click")

    form_type = 'read'
    document.getElementById('form_type').value = form_type
    document.getElementById('list_page2').style.display = "none"

    document.getElementById('list_header').style.display = "block"
    document.getElementById('list_page1').style.display = "block"

    document.getElementById('pub_read').style.display = "block"
    document.getElementById('station_button').style.display = "block"

    console.log(fields_list)
    console.log(icon_list)
    //console.log(form_visible_list)
    //document.getElementById('monday').setAttribute("readonly", "true")




    //}

    document.getElementById('station_button').classList.remove("hide_button");
    document.getElementById('station_button').classList.add("show_button");
/*
    document.getElementById('edit_button').classList.remove("hide_button");
    document.getElementById('edit_button').classList.add("show_button");

    document.getElementById('upload_button').classList.remove("hide_button");
    document.getElementById('upload_button').classList.add("show_button");

    document.getElementById('delete_button').classList.remove("hide_button");
    document.getElementById('delete_button').classList.add("show_button");
*/
    filtered_data = populate_pub(all_data, id)
    //update_data(filtered_data)
    console.log(filtered_data)

    populate_form(filtered_data);
    populate_diary(filtered_data);
    update_features_icons(filtered_data)
    map_visible(filtered_data);
    document.getElementById('x_pub_identity').innerHTML = id
    document.getElementById('search_header').innerHTML = filtered_data[0].pub_name
    document.getElementById('list_header').style.display = 'block'

    for (let i = 0; i < icon_list.length; i++) {
        console.log('for icon loop: ' + icon_list[i])
        document.getElementById(icon_list[i] + '_20').setAttribute("onclick", "return false;")
        //var icon_id = icon_list[i] + '_20'
        //console.log(icon_id)
        //document.getElementById(icon_id).removeAttribute("onclick")
    }

    //if (document.getElementById('form_type').value == 'read') {
    console.log('read form')
    for (let i = 0; i < fields_list.length; i++) {
        if (!icon_list.includes(fields_list[i])) {
            if (form_visible_list.includes(fields_list[i])) {
                console.log('for form loop: ' + fields_list[i])
                document.getElementById(fields_list[i]).setAttribute("readonly", "true")
            }
        }
    }
    for (let i = 0; i < diary_headers.length; i++) {
        console.log('for diary loop: ' + diary_headers[i])
        document.getElementById(diary_headers[i]).setAttribute('readonly', 'true')
    }
    document.getElementById("x_station").value = document.getElementById("station_identity").value;
    document.getElementById("x_station_name").value = document.getElementById("station_name").value;
    document.getElementById("station_2").value = document.getElementById("x_station").value;

}
