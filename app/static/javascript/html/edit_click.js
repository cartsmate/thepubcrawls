function editClick(edit_item) {
    console.log(edit_item)
    document.getElementById(edit_item).setAttribute("readonly", "false")
    var editElement = document.getElementById('edit_' + edit_item);
    console.log(editElement)
    editElement.src = "/static/icons/footer/plus.png"

    document.getElementById(edit_item).removeAttribute("readonly");
    console.log(inputElement)

}
