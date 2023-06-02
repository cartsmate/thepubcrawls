function starClick(check_item) {
    console.log(check_item)
    var checkBox = document.getElementById('rank' + check_item);
    var texty = document.getElementById("img_rank" + check_item);
    document.getElementById('rank').value = check_item
    switch(check_item) {
        case 1:
            if (document.getElementById("img_rank1").style.opacity == "1" && document.getElementById("img_rank2").style.opacity != "1") {
                document.getElementById("img_rank1").style.opacity = "0.25"
            } else {
                document.getElementById("img_rank1").style.opacity = "1.0"
            }
            console.log(document.getElementById("img_rank1").style.opacity)
            document.getElementById("img_rank2").style.opacity = "0.25"
            document.getElementById("img_rank3").style.opacity = "0.25"
            document.getElementById("img_rank4").style.opacity = "0.25"
            document.getElementById("img_rank5").style.opacity = "0.25"
            break;
        case 2:
            console.log('2')
            document.getElementById("img_rank1").style.opacity = "1.0"
            document.getElementById("img_rank2").style.opacity = "1.0"
            document.getElementById("img_rank3").style.opacity = "0.25"
            document.getElementById("img_rank4").style.opacity = "0.25"
            document.getElementById("img_rank5").style.opacity = "0.25"
            break;
        case 3:
            console.log('3')
            document.getElementById("img_rank1").style.opacity = "1.0"
            document.getElementById("img_rank2").style.opacity = "1.0"
            document.getElementById("img_rank3").style.opacity = "1.0"
            document.getElementById("img_rank4").style.opacity = "0.25"
            document.getElementById("img_rank5").style.opacity = "0.25"
            break;
        case 4:
            console.log('4')
            document.getElementById("img_rank1").style.opacity = "1.0"
            document.getElementById("img_rank2").style.opacity = "1.0"
            document.getElementById("img_rank3").style.opacity = "1.0"
            document.getElementById("img_rank4").style.opacity = "1.0"
            document.getElementById("img_rank5").style.opacity = "0.25"
            break;
        case 5:
            console.log('5')
            document.getElementById("img_rank1").style.opacity = "1.0"
            document.getElementById("img_rank2").style.opacity = "1.0"
            document.getElementById("img_rank3").style.opacity = "1.0"
            document.getElementById("img_rank4").style.opacity = "1.0"
            document.getElementById("img_rank5").style.opacity = "1.0"
            break;
    }
}
