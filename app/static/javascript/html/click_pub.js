function click_pub(id) {
    console.log("CLICK_PUB")
    console.log('id: ' + id)
    form_type = 'read'
    page_layout('read')

    filtered_data = populate_pub(id)
    pubs_selection = filtered_data
    //update_data(filtered_data)
    //console.log(filtered_data)

    populate_form(filtered_data);
    populate_diary(filtered_data);
    update_icons_pub(filtered_data)
    map_visible(filtered_data);

    document.getElementById('x_pub_identity').value = id
    document.getElementById('search_header').innerHTML = filtered_data[0].pub_name
    document.getElementById('list_header').style.display = 'block'

    document.getElementById('list_features').style.display = 'none'

    for (let i = 0; i < icon_list.length; i++) {
        document.getElementById(icon_list[i]).setAttribute("onclick", "return false;")
    }
    for (let i = 0; i < fields_list.length; i++) {
        if (!icon_list.includes(fields_list[i])) {
            if (form_visible_list.includes(fields_list[i])) {
                document.getElementById(fields_list[i]).setAttribute("readonly", "true")
            }
        }
    }
    for (let i = 0; i < diary_headers.length; i++) {
        document.getElementById(diary_headers[i]).setAttribute('readonly', 'true')
    }
    document.getElementById("x_station").value = document.getElementById("station_identity").value;
    document.getElementById("x_station_name").value = document.getElementById("station_name").value;
    document.getElementById("station_2").value = document.getElementById("x_station").value;

}
