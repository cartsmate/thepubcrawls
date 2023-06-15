function featureClick(check_item, auto_exec) {
    console.log("featureClick")
    console.log(check_item)
    console.log(auto_exec)
    var checkBox = document.getElementById(check_item);
    console.log(checkBox)
    var image = document.getElementById(check_item + "_img");
    var caption = document.getElementById(check_item + "_caption");
    var checkCol = document.getElementById(check_item + "_col");
    if (checkBox.checked == true){
        console.log(checkBox.checked)
        //window.location.replace("/pub/list/" + check_item + "/True");
        image.style.opacity = "1.00"
        caption.style.opacity = "1.00"
        caption.style.color = "white"
        checkCol.style.background = "#0275D8"
    } else {
        console.log(checkBox.checked)
        image.style.opacity = "1.0"
        caption.style.opacity = "1.0"
        caption.style.color = "black"
        checkCol.style.background = "#CDCDCD"
    }
    if (auto_exec == 'on') {
        featureSearch()
    }
}
