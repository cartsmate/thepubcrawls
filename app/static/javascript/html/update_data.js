function update_data() {
    console.log('update_data')
    //console.log(pubs_selection)
    diary_headers = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = document.getElementById('x_day').value
    station = document.getElementById('x_station').value
    direction = document.getElementById('x_direction').value
    Delete_table()
    //console.log('all_data: ' + all_data.length)
    filtered_data = populate_test(all_data)
    console.log('filtered_data: ' + filtered_data.length)
    create_table(filtered_data, alias)
    if (day != 'all') {
        const isIndex = (element) => element == day;
        order = headers.findIndex(isIndex);
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = false
            }
        visible.rank = false
        visible[day] = true
        Search(headers, visible, order)
    } else {
        const isIndex = (element) => element == 'rank';
        order = headers.findIndex(isIndex);
        Search(headers, visible, order)
    }
    mapLoad('{{google_key}}');
}
