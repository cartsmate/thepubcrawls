function home_station_changed() {
    console.log('station dropdown changed')
    var station_selection = document.getElementById('station').value
    //console.log(document.getElementById('station').value)
    //console.log(document.getElementById('station').text)
    var e = document.getElementById("station");
    var value = e.value;
    var text = e.options[e.selectedIndex].text;
    //console.log(text)
    document.getElementById("x_station").value = value
    document.getElementById("x_station_name").value = text
}
