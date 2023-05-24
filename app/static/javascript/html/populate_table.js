function populate_table(stop_offs) {
    const result = [];
    for (const stop of stop_offs) {
        var newArray = pubs.filter(function (el) {
              return el.place == stop.place_id;
            });
        const pub = pubs.filter (obj => (obj.place === stop.place_id))
        result.push({
            name: newArray.name,
            place: stop.place_id
        });
    }
    letters = ['A','B','C','D','E','F','G','H','I','J']
    table_string = '<table id="pub_list" class="table table-striped">'
    table_string += '<thead><tr>' +
                        '<th>Stop</th>' +
                        '<th>Name</th>' +
                        '<th>Rank</th>' +
                        '<th>Walk</th>' +
                        '</tr></thead>'
    for (let i=0; i< stop_offs.length; i++) {
        if (Math.ceil(stop_offs[i]['duration']/60) == 0) {
            min_calc = ''
        } else {
            min_calc = Math.ceil(stop_offs[i]['duration']/60) + 'min '
        }
        sec_calc = stop_offs[i]['duration'] - (Math.floor(stop_offs[i]['duration']/60))*60
        if (sec_calc == 0) {
            secs_calc = ''
        } else {
            secs_calc = (stop_offs[i]['duration'] - (Math.floor(stop_offs[i]['duration']/60))*60) + 'sec'
        }
        table_string += '<tr><td>' + letters[i] + '</td>' +
            '<td><a href="/pub/' + stop_offs[i]['pub_identity'] + '">' + stop_offs[i]['name'] + '</a></td>'

        if (stop_offs[i].rank != '0') {
            table_string +=
                '<td>' +
                    '<div class="star_container">' +
                        '<img src="/static/icons/star.png" style="width:30px;height:30px;opacity:1.0;">' +
                        '<div class="star_centre">' + stop_offs[i].rank + '</div>' +
                    '</div>' +
                '</td>'
        } else {
            table_string +=
                '<td>' +
                    '<div class="star_container">' +
                        '<img src="/static/icons/star.png" style="width:30px;height:30px;opacity:0.25;">' +
                        '<div class="star_centre"></div>' +
                    '</div>' +
                '</td>'
        }
        table_string += '<td>' + min_calc + '</td></tr>'
    }
    table_string += '</table>'
    document.getElementById('route').innerHTML = table_string
}
