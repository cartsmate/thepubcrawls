function column_filter() {
    console.log('COLUMN_FILTER')
    console.log('visible')
    console.log(visible)
    diary_headers = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    station = document.getElementById('x_station').value
    day = document.getElementById('x_day').value
    console.log('day')
    console.log(day)
    if (document.getElementById('x_station').value != 'all' && document.getElementById('x_day').value != 'all') {
        console.log('station and day selected')
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = 'false'
            }
        visible[day] = 'true'
        visible['station_name'] = 'false'
        visible['rank'] = 'true'
        visible['pub_name'] = 'true'
        const isIndex = (element) => element == day
        order = headers.findIndex(isIndex);
        //filter_table(headers, visible, order)
    } else if (document.getElementById('x_station').value != 'all') {
        console.log('station only selected')
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = 'false'
            }
        visible['station_name'] = 'false'
        visible['rank'] = 'true'
        visible['pub_name'] = 'true'
        const isIndex = (element) => element == 'rank';
        order = headers.findIndex(isIndex);
        //filter_table(headers, visible, order)
    } else if (document.getElementById('x_day').value != 'all') {
        console.log('day only selected')
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = 'false'
            }
        visible[day] = 'true'
        visible['station_name'] = 'true'
        visible['rank'] = 'false'
        visible['pub_name'] = 'true'
        const isIndex = (element) => element == day;
        order = headers.findIndex(isIndex);
        //filter_table(headers, visible, order)
    } else {
        for (let i = 0; i < diary_headers.length; i++) {
            visible[diary_headers[i]] = 'false'
            }
        visible['station_name'] = 'true'
        visible['rank'] = 'true'
        visible['pub_name'] = 'true'
        const isIndex = (element) => element == 'rank';
        order = headers.findIndex(isIndex);
        //filter_table(headers, visible, order)
    }
    //visible['pub_identity'] = true
    console.log('visible')
    console.log(visible)
    console.log('order')
    console.log(order)
    return [visible, order]
}
