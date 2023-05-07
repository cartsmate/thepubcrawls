function mapSetup2() {
    crawl = { start, walk, favourite, stops, criteria }
    var stop_offs = []
    if ( crawl.favourite = 'all' ) {
        crawl.score = pub[0]['score']
        crawl.score_name = 'Rating'
    } else {
        crawl.score = pub[0][favourite]
        crawl.score_name = favourite
    }
    pub_first_stop = {
        name: pub[0]['name'],
        distance_from_first: 0,
        distance_next: 0,
        score: pub[0]['score'],
        star: pub[0]['star'],
        star_score: pub[0][pub[0]['star']],
        lat: pub[0]['latitude'],
        lng: pub[0]['longitude'],
        place: pub[0]['place'],
        pub_identity: pubs[0]['pub_identity']
    }
    pubs = pubs.filter (obj => !(obj.place == pub_first_stop.place))
    if ( crawl.favourite != 'all' ) {
        pubs = pubs.filter (obj => (obj[crawl.favourite] === true))
    }
    if (pubs.length > 0 ) {
        stop_offs.push(pub_first_stop)
        for (let i=0; i<crawl.stops; i++) {
            list_got = distancing(pub_first_stop, stop_offs[i], pubs, crawl)
            if ( list_got === undefined ) {
                break;
            } else {
                stop_offs.push(list_got)
                pubs = pubs.filter (obj => !(obj.place == list_got.place))
            }
        }
        displayCrawl(stop_offs, 'map');
    } else {
        displayNone(pub_first_stop);
    }
    var myOptions = {
        zoom: 14,
        center: new google.maps.LatLng(52.0, -0.02),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zoomControl: false,
        streetViewControl: false,
        disableDefaultUI: true
    }
    map2 = new google.maps.Map(document.getElementById("map2"), myOptions)
    map2.addListener("click", (event) => {
        console.log('you clicked on the map')
        event.stop();
        window.location.href = "/pub/map/all"
    });
}
