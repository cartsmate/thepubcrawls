function check_week_list(value) {
    console.log('CHECK_WEEK_LIST')
    auto_exec = document.getElementById('auto_exec').value
    diary_headers = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    for (let i = 0; i < diary_headers.length; i++) {
        var checkBox = document.getElementById("btn_" + diary_headers[i] + "_2")
        var imageBox = document.getElementById(diary_headers[i] + "_img_2")
        if (diary_headers[i] == value) {
            if (checkBox.checked == true) {
                imageBox.style.opacity = "1"
                document.getElementById('day_2').value = value
                document.getElementById('x_day').value = value
            } else {
                imageBox.style.opacity = "0.25"
                document.getElementById('day_2').value = 'all'
                document.getElementById('x_day').value = 'all'
            }
        } else {
            checkBox.checked = false
            imageBox.style.opacity = "0.25"
        }
    }
    if (auto_exec == 'on') {

        console.log('auto_exec: on')
        update_data(filtered_data)
        update_icons_list(filtered_data)
        /*
        delete_table()
        filtered_data = populate_test(all_data)
        update_icons_pub(filtered_data)
        create_table(filtered_data, alias)
        visible, order = column_filter()
        filter_table(headers, visible, order)
        //map_visible(filtered_data);
        header = update_header() + " (" + filtered_data.length + ")"
        document.getElementById('search_header').innerHTML = header
        document.getElementById('list_header').style.display = 'block'
        */
    }
}
