function populate_test() {
    console.log('POPULATE_TEST')

    filtered_data = all_data
    //console.log('filtered_data')
    //console.log(filtered_data)

    direction_name = document.getElementById("x_direction_name").value
    station_name = document.getElementById('x_station_name').value
    day = document.getElementById('x_day').value
    brunch = document.getElementById("x_brunch").value
    dart = document.getElementById("x_dart").value
    entertain = document.getElementById("x_entertain").value
    favourite = document.getElementById("x_favourite").value
    garden = document.getElementById("x_garden").value
    history = document.getElementById("x_history").value
    late = document.getElementById("x_late").value
    music = document.getElementById("x_music").value
    pool = document.getElementById("x_pool").value
    quiz = document.getElementById("x_quiz").value
    roast = document.getElementById("x_roast").value
    sport = document.getElementById("x_sport").value
    pre_header = ""

    if (document.getElementById('x_station').value != 'all') {
        console.log('NOT ALL STATION: ' + document.getElementById('x_station').value)
        var filtered_data = all_data.filter(function(pub) {
            return pub.station_identity == document.getElementById('x_station').value
            });
        pre_header = station_name + " Pubs"
    } else if (document.getElementById("x_direction").value != 'all') {
        console.log('NOT ALL DIRECTION: ' + document.getElementById('x_direction').value)
        var filtered_data =  all_data.filter(function(pub) {
            return pub.direction_identity == document.getElementById('x_direction').value
            });
        pre_header = direction_name + " Pubs"
    } else {
        console.log('ALL STATION & ALL DIRECTION')
    }
    console.log('filtered_data')
    console.log(filtered_data)

    var review_list = ['brunch', 'dart', 'entertain', 'favourite', 'garden', 'history', 'late', 'music', 'pool', 'quiz', 'roast', 'sport']
    for (let i = 0; i < review_list.length; i++) {
        console.log('review: ' + review_list[i])
        console.log(document.getElementById('x_' + review_list[i]).value)
        if (document.getElementById("x_" + review_list[i]).value == 'true') {
            console.log('true')
            var filtered_data = filtered_data.filter(function(pub) {
                return pub[review_list[i]] == 'true'
                });
        } else {
            console.log('false')
            var filtered_data = filtered_data.filter(function(pub) {
                return (pub[review_list[i]] == 'true' || pub[review_list[i]] == 'false' || pub[review_list[i]] == '')
                });
        }
    }
    /*
    console.log(filtered_data)
    if (brunch == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.brunch == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.brunch == true || pub.brunch == false)
            });
    }
    if (dart == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.dart == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.dart == true || pub.dart == false)
            });
    }
    if (entertain == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.entertain == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.entertain == true || pub.entertain == false)
            });
    }
    if (favourite == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.favourite == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.favourite == true || pub.favourite == false)
            });
    }
    if (garden == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.garden == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.garden == true || pub.garden == false)
            });
    }
    if (history == 'true') {
        //console.log('history true')
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.history == true
            });
    } else {
        //console.log('history false')
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.history == true || pub.history == false)
            });
    }
    if (late == 'true') {
        //console.log('late true')
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.late == true
            });
    } else {
        //console.log('late false')
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.late == true || pub.late == false)
            });
    }
    if (music == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.music == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.music == true || pub.music == false)
            });
    }
    if (pool == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.pool == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.pool == true || pub.pool == false)
            });
    }
    if (quiz == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.quiz == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.quiz == true || pub.quiz == false)
            });
    }
    if (roast == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.roast == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.roast == true || pub.roast == false)
            });
    }
    if (sport == 'true') {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.sport == true
            });
    } else {
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.sport == true || pub.sport == false)
            });
    }
    */
/*
    if (day != 'all' && document.getElementById('music').checked == 'true' && document.getElementById('quiz').checked == 'true') {
        console.log('day and music')
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub[day].contains('music') || pub[day].contains('music'))
            });
        pre_header += pre_header + " on " + day
    } else if (day != 'all' && document.getElementById('music').checked == 'false' && document.getElementById('quiz').checked == 'true') {
        console.log('day and quiz')
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub[day].contains('quiz'))
            });
        pre_header += pre_header + " on " + day
    } else if (day != 'all' && document.getElementById('music').checked == 'true' && document.getElementById('quiz').checked == 'false') {
        console.log('day and quiz')
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub[day].contains('music'))
            });
        pre_header += pre_header + " on " + day
    } else if (day != 'all') {
        console.log('no quiz & no music')
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub[day] !='Closed')
            });
        pre_header += pre_header + " on " + day
    } else {
        console.log('no day')
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub)
            });
    }
*/
    filtered_data = filtered_data.sort((a, b) => {
        if (a.rank < b.rank) {
            return -1;
            }
        });
    /*
    for (let i = 0; i < icon_list.length; i++) {
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.icon_list[i] == document.getElementById(icon_list[i]).checked
        });
        }
    */
    //console.log('filtered data after filters: ' + filtered_data.length)
    //document.getElementById("header_listing").innerHTML = pre_header + "(" + filtered_data.length + ")"
    console.log('filtered_data')
    console.log(filtered_data)
    return filtered_data
}