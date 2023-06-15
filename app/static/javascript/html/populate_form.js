function populate_form(form){
    for (i = 0; i < fields_list.length; i++) {
        //console.log(pub_review_fields[i])
        if (document.getElementById(fields_list[i])) {
            if (fields_list[i] in dropdown_list) {
                //console.log('dropdown')
                var dropdown_str = String(pub_review[0][fields_list[i]]['0']).toUpperCase() + String(pub_review[0][fields_list[i]]).substring(1)
                document.getElementById(fields_list[i]).value = dropdown_str
            } else if (fields_list[i] in check_list) {
                //console.log('check')
                if (pub_review[0][fields_list[i]] == true) {
                    //console.log('true')
                    document.getElementById(fields_list[i]).checked = true;
                    document.getElementById(fields_list[i]).style.hidden = "none";
                    var feature_img = fields_list[i] + "_img"
                    var feature_col = fields_list[i] + "_col"
                    var feature_caption = fields_list[i] + "_caption"
                    document.getElementById(feature_col).style.background = "#0275D8";
                    document.getElementById(feature_caption).style.color = "white";
                }
            } else if (fields_list[i] in star_list) {
                document.getElementById(fields_list[i]).value = pub_review[0][fields_list[i]];
                check_item = pub_review[0][fields_list[i]]
                switch(check_item) {
                    case 1:
                        //console.log('1')
                        document.getElementById("img_rank1").style.opacity = "1.0"
                        document.getElementById("img_rank2").style.opacity = "0.25"
                        document.getElementById("img_rank3").style.opacity = "0.25"
                        document.getElementById("img_rank4").style.opacity = "0.25"
                        document.getElementById("img_rank5").style.opacity = "0.25"
                        break;
                    case 2:
                        //console.log('2')
                        document.getElementById("img_rank1").style.opacity = "1.0"
                        document.getElementById("img_rank2").style.opacity = "1.0"
                        document.getElementById("img_rank3").style.opacity = "0.25"
                        document.getElementById("img_rank4").style.opacity = "0.25"
                        document.getElementById("img_rank5").style.opacity = "0.25"
                        break;
                    case 3:
                        //console.log('3')
                        document.getElementById("img_rank1").style.opacity = "1.0"
                        document.getElementById("img_rank2").style.opacity = "1.0"
                        document.getElementById("img_rank3").style.opacity = "1.0"
                        document.getElementById("img_rank4").style.opacity = "0.25"
                        document.getElementById("img_rank5").style.opacity = "0.25"
                        break;
                    case 4:
                        //console.log('4')
                        document.getElementById("img_rank1").style.opacity = "1.0"
                        document.getElementById("img_rank2").style.opacity = "1.0"
                        document.getElementById("img_rank3").style.opacity = "1.0"
                        document.getElementById("img_rank4").style.opacity = "1.0"
                        document.getElementById("img_rank5").style.opacity = "0.25"
                        break;
                    case 5:
                        //console.log('5')
                        document.getElementById("img_rank1").style.opacity = "1.0"
                        document.getElementById("img_rank2").style.opacity = "1.0"
                        document.getElementById("img_rank3").style.opacity = "1.0"
                        document.getElementById("img_rank4").style.opacity = "1.0"
                        document.getElementById("img_rank5").style.opacity = "1.0"
                        break;
                }
            } else {
                console.log(fields_list[i])
                console.log(pub_review[0][fields_list[i]])
                document.getElementById(fields_list[i]).value = pub_review[0][fields_list[i]];
            }
        } else {
            continue;
        }
    }

}
