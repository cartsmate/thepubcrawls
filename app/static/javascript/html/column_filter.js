function column_filter() {
    console.log('column_filter')

    diary_headers = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    station = document.getElementById('x_station').value
    if (document.getElementById('x_station').value != 'all' && document.getElementById('x_day').value != 'all') {
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = false
            }
        visible[day] = true
        visible['station_name'] = false
        visible['rank'] = true
        const isIndex = (element) => element == day
        order = headers.findIndex(isIndex);
        //filter_table(headers, visible, order)
    } else if (document.getElementById('x_station').value != 'all') {
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = false
            }
        visible['station_name'] = false
        visible['rank'] = true
        const isIndex = (element) => element == 'rank';
        order = headers.findIndex(isIndex);
        //filter_table(headers, visible, order)
    } else if (document.getElementById('x_day').value != 'all') {
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = false
            }
        visible[day] = true
        visible['station_name'] = true
        visible['rank'] = false
        const isIndex = (element) => element == day;
        order = headers.findIndex(isIndex);
        //filter_table(headers, visible, order)
    } else {
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = false
            }
        visible['station_name'] = true
        visible['rank'] = true
        const isIndex = (element) => element == 'rank';
        order = headers.findIndex(isIndex);
        //filter_table(headers, visible, order)
    }
    //visible['pub_identity'] = true
    return visible, order
}
