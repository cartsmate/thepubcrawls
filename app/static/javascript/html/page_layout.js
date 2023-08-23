function page_layout(page) {
    console.log('PAGE_LAYOUT')
    if (page == 'home') {
        console.log('page layout - home')
        document.getElementById('form_type').value = 'home'
        document.getElementById('home_page').style.display = 'block'
        document.getElementById('home_button').style.display = 'none'
        document.getElementById('the_map').style.display = 'none'
        document.getElementById('map').style.display = 'none'
        document.getElementById('list_header').style.display = 'none'
        document.getElementById('list_page1').style.display = 'none'
        document.getElementById('list_page2').style.display = 'none'
        document.getElementById('pub_read').style.display = 'none'
        document.getElementById('edit_button').style.display = 'none'
        document.getElementById('station_button').style.display = 'none'
    } else if (page == 'list') {
        console.log('page layout - list')
        document.getElementById('form_type').value = 'list'
        document.getElementById('home_page').style.display = 'none'
        document.getElementById('home_button').style.display = 'block'
        document.getElementById('the_map').style.display = 'block'
        document.getElementById('map').style.display = 'block'
        document.getElementById('list_header').style.display = 'block'
        document.getElementById('list_page1').style.display = 'block'
        document.getElementById('list_page2').style.display = 'block'
        document.getElementById('pub_read').style.display = 'none'
        document.getElementById('edit_button').style.display = 'none'
        document.getElementById('station_button').style.display = 'none'
    } else if (page == 'read') {
        console.log('page layout - read')
        document.getElementById('form_type').value = 'read'
        document.getElementById('home_page').style.display = 'none'
        document.getElementById('home_button').style.display = 'block'
        document.getElementById('the_map').style.display = 'block'
        document.getElementById('list_header').style.display = 'none'
        document.getElementById('list_page1').style.display = 'none'
        document.getElementById('list_page2').style.display = 'none'
        document.getElementById('pub_read').style.display = 'block'
        document.getElementById('edit_button').style.display = 'block'
        document.getElementById('station_button').style.display = 'block'
    } else if (page == 'edit') {
        console.log('page layout - edit')
        document.getElementById('form_type').value = 'edit'
        document.getElementById('home_page').style.display = 'none'
        document.getElementById('home_button').style.display = 'block'
        document.getElementById('the_map').style.display = 'block'
        document.getElementById('list_header').style.display = 'none'
        document.getElementById('list_page1').style.display = 'none'
        document.getElementById('list_page2').style.display = 'none'
        document.getElementById('pub_read').style.display = 'block'
        document.getElementById('edit_button').style.display = 'none'
        document.getElementById('station_button').style.display = 'none'
    } else {
        console.log('page layout - else/error')
        document.getElementById('form_type').value = 'error'
        document.getElementById('home_page').style.display = 'none'
        document.getElementById('home_button').style.display = 'none'
        document.getElementById('the_map').style.display = 'none'
        document.getElementById('list_header').style.display = 'none'
        document.getElementById('list_page1').style.display = 'none'
        document.getElementById('list_page2').style.display = 'none'
        document.getElementById('pub_read').style.display = 'none'
        document.getElementById('edit_button').style.display = 'none'
        document.getElementById('station_button').style.display = 'none'
    }
}
