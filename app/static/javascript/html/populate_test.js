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


    /*
    if (document.getElementById('x_search').value != '') {
//        var loc_lat = 0
//        var loc_lng = 0
        get_coordinates(inputAddress, function(location){
            //alert(location.lat()); // this is where you get the return value
            //alert(location.lng())

            //filtered_data.forEach((element) => {
            //    element.distance = (Math.abs(element.pub_latitude - location.lat())) + (Math.abs(element.pub_longitude - location.lng()))
            //});
            var loc_lat = location.lat()
//            alert('loc_lat: in: ' + loc_lat)
            var loc_lng = location.lng()
//            alert('loc_lng: in: ' + loc_lng)
            filtered_data = do_complete(loc_lat, loc_lng)
        });
        //while (loc_lat == 0 && loc_lng == 0) {
        //}

        for(const element of filtered_data) {
            console
            console.log(element.pub_latitude)
            console.log(loc_lat)
            console.log(element.pub_longitude)
            console.log(loc_lng)
            element['distance'] = (Math.abs(element.pub_latitude - loc_lat)) + (Math.abs(element.pub_longitude - loc_lng))
        }
        */
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
        console.log('NO STATION & NO DIRECTION & NO SEARCH')
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

    if (document.getElementById('x_search').value != '') {
        console.log('sort by distance')

        //filtered_data = filtered_data.sort(compare);
        let sortedDates = filtered_data.sort((p1, p2) => (p1.distance > p2.distance) ? 1 : (p1.distance < p2.distance) ? -1 : 0);

        filtered_data = sortedDates
        /*
        filtered_data = filtered_data.sort((a, b) => {
            if (a.distance > b.distance) {
                return -1;
                }
            });
        */
        //filtered_data = filtered_data.slice(0, 10);
    } else {
        console.log('sort by rank')
        filtered_data = filtered_data.sort((a, b) => {
            if (a.rank < b.rank) {
                return -1;
                }
            });
    }
    console.log('filtered_data')
    console.log(filtered_data)
    return filtered_data
}

function compare(a, b) {
    if (a < b) {
        return -1;
    } else if (a > b) {
        return 1;
    } else {
        return 0;
    }
}
