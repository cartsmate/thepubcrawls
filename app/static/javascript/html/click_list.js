function click_list() {
    console.log("CLICK_LIST")

    page_layout('list')
    document.getElementById('auto_exec').value = 'on'
    update_list_station()

    filtered_data = populate_test(all_data)

    update_data(filtered_data)

    update_icons_list(filtered_data)
}


const groupBy = (arr, key) => arr.reduce((acc, item) => ((acc[item[key]] = [...(acc[item[key]] || []), item]), acc), {});
