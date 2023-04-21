function populate_form(form){
    for (i = 0; i < pub_review_fields.length; i++) {

        if (document.getElementById(pub_review_fields[i])) {
            if (dropdown_controls.includes(pub_review_fields[i])) {
                console.log('dropdown: ' + pub_review_fields[i])
                var dropdown_str = String(pub_review[0][pub_review_fields[i]]['0']).toUpperCase() + String(pub_review[0][pub_review_fields[i]]).substring(1)
                document.getElementById(pub_review_fields[i]).value = dropdown_str
            } else if (check_controls.includes(pub_review_fields[i])) {
                console.log('check: ' + pub_review_fields[i])
                if (pub_review[0][pub_review_fields[i]] == true) {
                    document.getElementById(pub_review_fields[i]).checked = true;
                    document.getElementById(pub_review_fields[i]).style.hidden = "none";
                    var text = "img_" + pub_review_fields[i]
                    document.getElementById(text).style.opacity = "1"
                }
            } else if (star_controls.includes(pub_review_fields[i])) {
                console.log('star: ' + pub_review_fields[i])
                console.log('star controls..........')
                console.log(pub_review[0][pub_review_fields[i]])
                if (pub_review[0][pub_review_fields[i]] >= 1) {
                    console.log('got a five !!!!!')
                    document.getElementById(pub_review_fields[i]).className = "fa fa-star fa-3x checked"
                }
                if (pub_review[0][pub_review_fields[i]] >= 2) {
                    console.log('got a five !!!!!')
                    document.getElementById(pub_review_fields[i]+"2").className = "fa fa-star fa-3x checked"
                }
                if (pub_review[0][pub_review_fields[i]] >= 3) {
                    console.log('got a five !!!!!')
                    document.getElementById(pub_review_fields[i]+"3").className = "fa fa-star fa-3x checked"
                }
                if (pub_review[0][pub_review_fields[i]] >= 4) {
                    console.log('got a five !!!!!')
                    document.getElementById(pub_review_fields[i]+"4").className = "fa fa-star fa-3x checked"
                }
                if (pub_review[0][pub_review_fields[i]] >= 5) {
                    console.log('got a five !!!!!')
                    document.getElementById(pub_review_fields[i]+"5").className = "fa fa-star fa-3x checked"
                }
            } else {
                console.log('else: ' + pub_review_fields[i])
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
