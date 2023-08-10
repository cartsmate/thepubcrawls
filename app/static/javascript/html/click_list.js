function click_list(stations_directions_list, all_data, alias, headers) {
    console.log("click_list")
    console.log(stations_directions_list)
    console.log(all_data)
    page_layout('list')
    document.getElementById('auto_exec').value = 'on'
    update_list_station()
    filtered_data = populate_test(all_data)
    update_data(filtered_data, alias, headers);

}


const groupBy = (arr, key) => arr.reduce((acc, item) => ((acc[item[key]] = [...(acc[item[key]] || []), item]), acc), {});
