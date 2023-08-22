function click_list() {
    console.log("CLICK_LIST")

    page_layout('list')
    document.getElementById('auto_exec').value = 'on'
    update_list_station()

    filtered_data = populate_test(all_data)

    update_data(filtered_data)

    update_icons_list(filtered_data)

    var day = document.getElementById('x_day').value
    if (day != 'all') {
        var checkBox = document.getElementById("btn_" + day + "_2")
        checkBox.checked == true
        var imageBox = document.getElementById(day + "_img_2")
        imageBox.style.opacity = "1"
    }

}


const groupBy = (arr, key) => arr.reduce((acc, item) => ((acc[item[key]] = [...(acc[item[key]] || []), item]), acc), {});
