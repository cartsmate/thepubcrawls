function edit_item(edit_item) {
    console.log('edit_item')
    console.log(edit_item)
    document.getElementById(edit_item).setAttribute("readonly", "false")
    var editElement = document.getElementById('edit_' + edit_item);
    //console.log(editElement)
    //editElement.src = "/static/icons/footer/plus.png"

    //document.getElementById(edit_item).removeAttribute("readonly");
    //console.log(inputElement)
    /*
    elem_submit_btn.disabled = false
    elem_submit_msg.setAttribute("style","display:none;");
    elem_submit_lnk.setAttribute("style","color:#d9534f;");
    */
}
