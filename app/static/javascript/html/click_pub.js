function pub_click(id) {
    console.log("pub_click")

    form_type = 'read'
    document.getElementById('list_header').style.display = "block"
    document.getElementById('list_page1').style.display = "block"
    document.getElementById('list_page2').style.display = "none"
    document.getElementById('pub_read').style.display = "block"
    console.log(form_type)

    document.getElementById('station_button').classList.remove("hide_button");
    document.getElementById('station_button').classList.add("show_button");

    document.getElementById('edit_button').classList.remove("hide_button");
    document.getElementById('edit_button').classList.add("show_button");

    document.getElementById('upload_button').classList.remove("hide_button");
    document.getElementById('upload_button').classList.add("show_button");

    document.getElementById('delete_button').classList.remove("hide_button");
    document.getElementById('delete_button').classList.add("show_button");

    filtered_data = populate_pub(all_data, id)

    console.log(filtered_data)
    populate_form(filtered_data);
    populate_diary(filtered_data);
    update_features_icons(filtered_data)
    map_visible(filtered_data);
    document.getElementById('search_header').innerHTML = filtered_data[0].pub_name
    document.getElementById('list_header').style.display = 'block'
}
