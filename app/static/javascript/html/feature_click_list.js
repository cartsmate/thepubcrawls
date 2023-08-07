function feature_click_list(check_item) {
    console.log("feature_click_list")
    console.log(check_item)
    var checkBox = document.getElementById(check_item + "_20");
    if (checkBox.checked == true) {
        document.getElementById("x_" + check_item).value = "true"
    } else {
        document.getElementById("x_" + check_item).value = "false"
    }



    //console.log(all_data)
    filtered_data = populate_test(all_data)
    //console.log(filtered_data)
    update_data(filtered_data)
    /*
    form_type = document.getElementById('form_type').value
    auto_exec = document.getElementById('auto_exec').value

    console.log(form_type)
    console.log(auto_exec)

    if (form_type != 'read') {
        console.log('inside: ' + check_item)

        var checkBox = document.getElementById(check_item + "_2");
        //console.log(checkBox)
        var image = document.getElementById(check_item + "_img_2");
        var caption = document.getElementById(check_item + "_caption_2");
        var checkCol = document.getElementById(check_item + "_col_2");
        if (checkBox.checked == true){
            console.log('true: ' + checkBox.checked)
            document.getElementById("x_" + check_item).value = checkBox.checked
            //window.location.replace("/pub/list/" + check_item + "/True");
            image.style.opacity = "1.0"
            caption.style.opacity = "1.0"
            caption.style.color = "white"
            checkCol.style.background = "#0275D8"
            checkCol.style.border = "thick solid #0275D8";
        } else {
            console.log('false: ' + checkBox.checked)
            document.getElementById("x_" + check_item).value = checkBox.checked
            image.style.opacity = "1.0"
            caption.style.opacity = "1.0"
            caption.style.color = "black"
            checkCol.style.background = "#CDCDCD"
            checkCol.style.border = "thick solid #CDCDCD";
        }
    }

    //var ele = document.getElementsByName('radio');
    //for (i = 0; i < ele.length; i++) {
    //    if (ele[i].checked)
    //        day = ele[i].value;
    //}

    if (auto_exec == 'on') {
        console.log('auto_exec: on')
        delete_table()
        filtered_data = populate_test(all_data)
        console.log('filtered_data')
        console.log(filtered_data)
        json_array = calculate_directions_count(filtered_data)
        update_features_icons(filtered_data)
        create_table(filtered_data, alias)
        visible, order = column_filter()
        filter_table(headers, visible, order)
        map_visible(filtered_data, json_array);
        header = update_header() + " (" + filtered_data.length + ")"
        document.getElementById('search_header').innerHTML = header
        document.getElementById('list_header').style.display = 'block'
    }
    */
}
