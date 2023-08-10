function page_layout(page) {

    if (page == 'home') {
        console.log('page layout - home')
        document.getElementById('form_type').value = 'home'
        document.getElementById('home_page').style.display = 'block'
        document.getElementById('home_button').style.display = 'none'
        document.getElementById('list_header').style.display = 'none'
        document.getElementById('list_page1').style.display = 'none'
        document.getElementById('list_page2').style.display = 'none'
        document.getElementById('pub_read').style.display = 'none'
    } else if (page == 'list') {
        document.getElementById('form_type').value = 'list'
        document.getElementById('home_page').style.display = 'none'
        document.getElementById('list_header').style.display = 'block'
        document.getElementById('list_page1').style.display = 'block'
        document.getElementById('list_page2').style.display = 'block'
        document.getElementById('home_button').style.display = 'block'
    } else if (page == 'read') {
        console.log('page layout - read')
        document.getElementById('form_type').value = 'read'
        document.getElementById('home_page').style.display = 'none'
        document.getElementById('home_button').style.display = 'block'
        document.getElementById('list_header').style.display = 'none'
        document.getElementById('list_page1').style.display = 'none'
        document.getElementById('list_page2').style.display = 'none'
        document.getElementById('pub_read').style.display = 'block'
    } else if (page == 'edit') {
        console.log('page layout - edit')
        document.getElementById('form_type').value = 'edit'
        document.getElementById('home_page').style.display = 'none'
        document.getElementById('home_button').style.display = 'block'
        document.getElementById('list_header').style.display = 'none'
        document.getElementById('list_page1').style.display = 'none'
        document.getElementById('list_page2').style.display = 'none'
        document.getElementById('pub_read').style.display = 'block'
    } else {
        console.log('page layout - else/error')
        document.getElementById('form_type').value = 'error'
        document.getElementById('home_page').style.display = 'none'
        document.getElementById('home_button').style.display = 'none'
        document.getElementById('list_header').style.display = 'none'
        document.getElementById('list_page1').style.display = 'none'
        document.getElementById('list_page2').style.display = 'none'
        document.getElementById('pub_read').style.display = 'none'
    }
}
