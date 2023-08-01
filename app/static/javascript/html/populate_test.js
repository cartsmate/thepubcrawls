function populate_test(filtered_data) {
    console.log('populate_test')
    //console.log('all data: ' + all_data.length)
    direction = document.getElementById("x_direction").value
    direction_name = document.getElementById("x_direction_name").value
    //console.log('direction: ' + direction)
    station = document.getElementById('x_station').value
    station_name = document.getElementById('x_station_name').value
    //console.log('station: ' + station)
    day = document.getElementById('x_day').value
    //console.log('day: ' + day)
    brunch = document.getElementById("x_brunch").value
    dart = document.getElementById("x_dart").value
    entertain = document.getElementById("x_entertain").value
    favourite = document.getElementById("x_favourite").value
    garden = document.getElementById("x_garden").value
    history = document.getElementById("x_history").value
    console.log('history: ' + history)
    late = document.getElementById("x_late").value
    console.log('late: ' + late)
    music = document.getElementById("x_music").value
    pool = document.getElementById("x_pool").value
    quiz = document.getElementById("x_quiz").value
    roast = document.getElementById("x_roast").value
    sport = document.getElementById("x_sport").value
    pre_header = ""
    //console.log('brunch: ' + brunch)
    //filtered_data = pubs_selection
    //console.log('filtered data before filters: ' + filtered_data.length)
    if (station != 'all') {
        //console.log('NOT ALL STATION')
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.station_identity == station
            });
        pre_header = station_name + " Pubs"
    } else if (direction != 'all') {
        //console.log(direction)
        //console.log('NOT ALL DIRECTION')
        var filtered_data =  filtered_data.filter(function(pub) {
            return pub.direction_identity == direction
            });
        pre_header = direction_name + " Pubs"
        }
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
        console.log('history true')
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.history == true
            });
    } else {
        console.log('history false')
        var filtered_data = filtered_data.filter(function(pub) {
            return (pub.history == true || pub.history == false)
            });
    }
    if (late == 'true') {
        console.log('late true')
        var filtered_data = filtered_data.filter(function(pub) {
            return pub.late == true
            });
    } else {
        console.log('late false')
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

    return filtered_data
}