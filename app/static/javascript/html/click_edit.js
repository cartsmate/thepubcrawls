function click_edit(id) {
    console.log("click_edit")
    form_type = 'edit'
    document.getElementById('form_type').value = form_type

    //document.getElementById('station_button').classList.remove("hide_button");
    //document.getElementById('station_button').classList.add("show_button");

    document.getElementById('edit_button').classList.remove("show_button");
    document.getElementById('edit_button').classList.add("hide_button");
    /*
    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub//"
    } else {
        var url = "http://" + base_url + ":5000/pub//"
    }
    const myUrlWithParams = new URL(url);
    myUrlWithParams.searchParams.append('pub_id', pub);
    window.location.replace(myUrlWithParams.href);
    */

    for (let i = 0; i < icon_list.length; i++) {
        document.getElementById(icon_list[i] + '_edit').setAttribute("onclick", "feature_click_edit('" + icon_list[i] + "')")
    }
    for (let i = 0; i < fields_list.length; i++) {
        if (!icon_list.includes(fields_list[i])) {
            if (form_visible_list.includes(fields_list[i])) {
                //document.getElementById(fields_list[i]).setAttribute("readonly", "false")
                document.getElementById(fields_list[i]).removeAttribute("readonly");
            }
        }
    }
    for (let i = 0; i < diary_headers.length; i++) {
        //document.getElementById(diary_headers[i]).setAttribute('readonly', 'false')
        document.getElementById(diary_headers[i]).removeAttribute("readonly");
    }

    document.forms["pub_form"].action="/pub/?pub_id=" + id
    //{{pubs_selection[0]['pub_identity']}}"

    elem_submit_btn.setAttribute("style","display:block;");
    elem_submit_msg.setAttribute("style","display:none;");
    elem_submit_lnk.setAttribute("style","color:#d9534f;");
    /*
    document.getElementById('list_header').style.display = "block"
    document.getElementById('list_page1').style.display = "block"
    document.getElementById('list_page2').style.display = "none"
    document.getElementById('pub_read').style.display = "block"
    console.log(form_type)
    //document.getElementById('station_button').removeClass = 'hide_button'
    //document.getElementById('station_button').addClass = 'show_button'
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
    */
}
