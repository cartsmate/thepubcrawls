function feature_click_edit(check_item) {
    console.log("feature_click_edit")
    //console.log(check_item)

    //form_type = document.getElementById('form_type').value
    //auto_exec = document.getElementById('auto_exec').value

    //console.log(form_type)
    //console.log(auto_exec)
    console.log('form_type: ' + form_type)
    //if (form_type != 'read') {
    var checkBox = document.getElementById(check_item + "_edit")
    //console.log(checkBox)
    var image = document.getElementById(check_item + "_img_edit");
    var caption = document.getElementById(check_item + "_caption_edit");
    var checkCol = document.getElementById(check_item + "_col_edit");
    if (checkBox.checked == true){
        //console.log(checkBox.checked)
        document.getElementById("x_" + check_item).value = checkBox.checked
        //window.location.replace("/pub/list/" + check_item + "/True");
        image.style.opacity = "1.0"
        caption.style.opacity = "1.0"
        caption.style.color = "white"
        checkCol.style.background = "#0275D8"
        checkCol.style.border = "thick solid #0275D8";
    } else {
        //console.log(checkBox.checked)
        document.getElementById("x_" + check_item).value = checkBox.checked
        image.style.opacity = "1.0"
        caption.style.opacity = "1.0"
        caption.style.color = "black"
        checkCol.style.background = "#CDCDCD"
        checkCol.style.border = "thick solid #CDCDCD";
    }
    //}

    //var ele = document.getElementsByName('radio');
    //for (i = 0; i < ele.length; i++) {
    //    if (ele[i].checked)
    //        day = ele[i].value;
    //}
/*
    if (auto_exec == 'on') {
        console.log('auto_exec: on')
        //featureList(direction, station, day)
        update_data()
        //Delete_table()
        //filtered_data = populate_test(all_data, direction, station, day)
        //create_table(filtered_data, alias)
        //Search(headers, visible, order)
    }
    */
}
