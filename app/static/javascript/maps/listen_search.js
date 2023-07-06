function listen_search(map, searchBox) {
    console.log("listen_search")
    map.addListener("bounds_changed", () => {
        searchBox.setBounds(map.getBounds());
    });
}
