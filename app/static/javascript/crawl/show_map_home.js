
function show_map_home(locator) {
    console.log('show_map_home')
    var map = new google.maps.Map(document.getElementById(locator), {
        zoom:7,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: false,
        streetViewControl: false
    });
}
