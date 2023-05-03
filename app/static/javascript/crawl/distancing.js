function distancing(first, current, pubs, crawl) {
    records = []
    for (let i = 0; i < pubs.length; i++) {
        lat_diff_0 = Math.abs(pubs[i]['latitude'] - first.lat)
        lng_diff_0 = Math.abs(pubs[i]['longitude'] - first.lng)
        tot_diff_0 = lat_diff_0 + lng_diff_0

        lat_diff = Math.abs(pubs[i]['latitude'] - current.lat)
        lng_diff = Math.abs(pubs[i]['longitude'] - current.lng)
        tot_diff = lat_diff + lng_diff
        if ( crawl.walk == 0 || tot_diff < crawl.walk * 0.000625 ) {
            var record = {
                name: pubs[i]['name'],
                distance_next: tot_diff,
                distance_from_first: tot_diff_0,
                score: pubs[i]['score'],
                star: pubs[i]['star'],
                star_score: pubs[i][pubs[i]['star']],
                lat: pubs[i]['latitude'],
                lng: pubs[i]['longitude'],
                place: pubs[i]['place'],
                pub_identity: pubs[i]['pub_identity'],
            }
            records.push(record);
        }
    }

    if ( crawl.criteria == 'NEAREST' ) {
        //console.log('nearest')
        records = records.sort((a, b) => {
            if (a.distance_next < b.distance_next) {
                return -1;
            }
        });
    } else {
        //console.log('score')
        records = records.sort((a, b) => {
            if (a.score > b.score) {
                return -1;
            }
        });
    }
    //console.log('records: ' + JSON.stringify(records))
    return records[0]
}
