function camel_case(word) {
    return String(word['0']).toUpperCase() + String(word).substring(1)
}

function editClick(id) {
    window.alert(id)
}

function escape(htmlStr) {
   return htmlStr.replace(/&/g, "&amp;")
         .replace(/</g, "&lt;")
         .replace(/>/g, "&gt;")
         .replace(/"/g, "&quot;")
         .replace(/'/g, "&#39;");

}

function unEscape(htmlStr) {
    htmlStr = htmlStr.replace(/&lt;/g , "<");
    htmlStr = htmlStr.replace(/&gt;/g , ">");
    htmlStr = htmlStr.replace(/&quot;/g , "\"");
    htmlStr = htmlStr.replace(/&#39;/g , "\'");
    htmlStr = htmlStr.replace(/&amp;/g , "&");
    return htmlStr;
}

function create_table() {
    console.log("create_table")
    table_string = '<table id="pub_list" class="table table-striped" style="font-size:16px;">'
    for (let i=0; i<key_list.length; i++) {
        console.log(key_list[i])
        console.log("{{review_object}}"[key_list[i]])
    }

    table_string += '<thead><tr>' +
                        '<th>Id</th>' +
                        '<th>Name</th>' +
                        '<th>Category</th>' +
                        '<th>Station</th>' +
                        '<th>Area</th>' +
                        '<th>Rank</th>' +
                        '<th>Tv</th>' +
                        '<th>Garden</th>' +
                        '<th>Music</th>' +
                        '<th>Late</th>' +
                        '<th>Meals</th>' +
                        '<th>Toilets</th>' +
                        '<th>Cheap</th>' +
                        '<th>Games</th>' +
                        '<th></th>' +
                        '<th></th>' +
                        '</tr></thead>'
   for (var key in pubs_reviews) {
        if (pubs_reviews[key].rank == 0) {
            str_reviewed =
             '<td>None</a></td>' +
             '<td>None</a></td>'
        } else {
            str_reviewed =
            '<td><a href="/pub/list/star/' + pubs_reviews[key].rank + '">' + camel_case(pubs_reviews[key].rank) + '</a></td>' +
            '<td><a href="../review/' + pubs_reviews[key].pub_identity + '">Review</a></td>'
        }
        table_string += '<tr>' +
            '<td><a href="/pub/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].pub_identity + '</a></td>' +
            '<td><a href="/pub/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].name + '</a></td>' +
            '<td><a href="/pub/list/category/' + pubs_reviews[key].category + '">' + camel_case(pubs_reviews[key].category) + '</a></td>' +
            '<td><a href="/pub/list/station/' + pubs_reviews[key].station + '">' + pubs_reviews[key].station + '</a></td>' +
            '<td><a href="/pub/list/area/' + pubs_reviews[key].area + '">' + pubs_reviews[key].area + '</a></td>' +
            '<td><a href="/pub/list/area/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].rank + '</a></td>' +
            str_reviewed
            if (pubs_reviews[key].rank != '0') {
                table_string +=
                    '<td>' +
                        '<div class="star_container">' +
                            '<img src="/static/icons/star.png" style="width:30px;height:30px;opacity:1.0;">' +
                            '<div class="star_centre">' + pubs_reviews[key].rank + '</div>' +
                        '</div>' +
                    '</td>'
            } else {
                table_string +=
                    '<td>' +
                        '<div class="star_container">' +
                            '<img src="/static/icons/star.png" style="width:25px;height:25px;opacity:0.25;">' +
                            '<div class="star_centre"></div>' +
                        '</div>' +
                    '</td>'
            }
            table_string +=
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].sport + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].garden + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].music + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].late + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].brunch + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].history + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].pool + '</a></td>' +
            '<td><a href="/review/' + pubs_reviews[key].pub_identity + '">' + pubs_reviews[key].dart + '</a></td>' +
            '<td><a href="/pub/edit/' + pubs_reviews[key].pub_identity + '"><img src="/static/icons/buttons/edit.png" style="width:25px;height:25px; padding:0px; margin:0px"></a></td>' +
            '<td><a href="/pub/delete/' + pubs_reviews[key].pub_identity + '"><img src="/static/icons/buttons/delete.png" style="width:25px;height:25px; padding:0px; margin:0px"></a></td>' +
            '</tr>'
    }
    table_string += '</table>'
    return table_string;
}
