function populate_form(form){
    for (i = 0; i < pub_review_fields.length; i++) {

        if (document.getElementById(pub_review_fields[i])) {
            if (dropdown_controls.includes(pub_review_fields[i])) {
                var dropdown_str = String(pub_review[0][pub_review_fields[i]]['0']).toUpperCase() + String(pub_review[0][pub_review_fields[i]]).substring(1)
                document.getElementById(pub_review_fields[i]).value = dropdown_str
            } else if (check_controls.includes(pub_review_fields[i])) {
                if (pub_review[0][pub_review_fields[i]] == true) {
                    document.getElementById(pub_review_fields[i]).checked = true;
                    document.getElementById(pub_review_fields[i]).style.hidden = "none";
                    var text = "img_" + pub_review_fields[i]
                    document.getElementById(text).style.opacity = "1"
                }
            } else if (star_controls.includes(pub_review_fields[i])) {
                document.getElementById(pub_review_fields[i]).value = pub_review[0][pub_review_fields[i]];
                check_item = pub_review[0][pub_review_fields[i]]
                switch(check_item) {
                    case 1:
                        console.log('1')
                        document.getElementById("img_rank1").style.opacity = "1.0"
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
            } else {
                document.getElementById(pub_review_fields[i]).value = pub_review[0][pub_review_fields[i]];
            }
        } else {
            continue;
        }
    }
    slider = []
    output = []
    for (let i = 0; i < slider_controls.length; i++) {
        slider[i] = document.getElementById(slider_controls[i]);
        output[i] = document.getElementById("value_" + slider_controls[i]);
        output[i].innerHTML = slider[i].value;
        if (form == 'edit' || form == 'add') {
            slider[i].oninput = function() {
                output[i].innerHTML = document.getElementById(slider_controls[i]).value;
                sum_score()
            }
        }
    }
    sum_score()
}
