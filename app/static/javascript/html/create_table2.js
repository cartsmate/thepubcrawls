function camel_case(word) {
    return String(word['0']).toUpperCase() + String(word).substring(1)
}

function create_table2() {
    console.log("create_table")
    table_string = '<table id="pub_list2" class="table table-striped">'
    table_string += '<thead><tr>' +
                        '<th>Name</th>' +
                        '<th>Category</th>' +
                        '<th>Station</th>' +
                        '<th>Area</th>' +
                        '<th>Star Quality</th>' +
                        '<th>Rev.</th>' +
                        '<th>Score</th>' +
                        '<th>Rank</th>' +
                        '<th>Tv</th>' +
                        '<th>Garden</th>' +
                        '<th>Music</th>' +
                        '<th>Late</th>' +
                        '<th>Meals</th>' +
                        '<th>Toilets</th>' +
                        '<th>Cheap</th>' +
                        '<th>Games</th>' +
                        '<th>E</th>' +
                        '<th>D</th>' +
                        '</tr></thead>'
   for (var key in pubs_reviews) {
        if (pubs_reviews[key].star == 0) {
            str_reviewed =
             '<td>None</a></td>' +
             '<td>None</a></td>'
        } else {
            str_reviewed =
            '<td><a href="/pub/list/star/' + pubs_reviews[key].star + '">' + camel_case(pubs_reviews[key].star) + '</a></td>' +
            '<td><a href="../review/' + pubs_reviews[key].pub_identity + '">Review</a></td>'
        }
        table_string += '<tr>' +
            '<td><a href="/pub/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].name + '</a></td>' +
            '<td><a href="/pub/list/category/' + pubs_reviews[key].category + '">' + camel_case(pubs_reviews[key].category) + '</a></td>' +
            '<td><a href="/pub/list/station/' + pubs_reviews[key].station + '">' + pubs_reviews[key].station + '</a></td>' +
            '<td><a href="/pub/list/area/' + pubs_reviews[key].area + '">' + pubs_reviews[key].area + '</a></td>' +
            str_reviewed +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].score + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].rank + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].tv + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].garden + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].music + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].late + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].meals + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].toilets + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].cheap + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].games + '</a></td>' +
            '<td><a href="/pub/' + pubs_reviews[key].pub_identity + '">EDIT</a></td>' +
            '<td><a href="/pub/delete/' + pubs_reviews[key].pub_identity + '">DEL</a></td>' +
            '</tr>'
    }
    table_string += '</table>'
    return table_string;
}
