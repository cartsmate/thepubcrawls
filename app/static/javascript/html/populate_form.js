function populate_form(form){
    console.log('populate form')
    for (i = 0; i < fields_list.length; i++) {
        //console.log(fields_list[i])
        //console.log(check_list)
        if (dropdown_list.includes(fields_list[i])) {
            //console.log('dropdown')
            var dropdown_str = String(pubs_selection[0][fields_list[i]]['0']).toUpperCase() + String(pubs_selection[0][fields_list[i]]).substring(1)
            document.getElementById(fields_list[i]).value = dropdown_str
        } else if (check_list.includes(fields_list[i])) {
            //console.log('checklist')
            if (pubs_selection[0][fields_list[i]] == true) {
                //console.log('true')
                document.getElementById(fields_list[i]).checked = true;
                document.getElementById(fields_list[i]).style.hidden = "none";
                var feature_img = fields_list[i] + "_img"
                var feature_col = fields_list[i] + "_col"
                var feature_caption = fields_list[i] + "_caption"
                document.getElementById(feature_col).style.background = "#0275D8";
                document.getElementById(feature_caption).style.color = "white";
            } else {
                //console.log('false')
            }
        } else if (star_list.includes(fields_list[i])) {
            shadeStars(fields_list[i], pubs_selection[0][fields_list[i]], 'populate')
            /*
            star_num = 30
            star_size = star_num + "px"
            document.getElementById(fields_list[i]).value = pub_review[0][fields_list[i]];
            num = pub_review[0][fields_list[i]]
            if (num >= 0 && num <1) {
                console.log('between 0 and 1')
                document.getElementById("img_rank1").style.width = star_size
                document.getElementById("img_rank2").style.width = "0px"
                document.getElementById("img_rank3").style.width = "0px"
                document.getElementById("img_rank4").style.width = "0px"
                document.getElementById("img_rank5").style.width = "0px"
            } else if (num >= 1 && num <2) {
                console.log('between 1 and 2')
                document.getElementById("img_rank1").style.width = star_size
                document.getElementById("img_rank2").style.width = star_size
                document.getElementById("img_rank3").style.width = "0px"
                document.getElementById("img_rank4").style.width = "0px"
                document.getElementById("img_rank5").style.width = "0px"
            } else if (num >= 2 && num <3) {
                console.log('between 2 and 3')
                document.getElementById("img_rank1").style.width = star_size
                document.getElementById("img_rank2").style.width = star_size
                document.getElementById("img_rank3").style.width = star_size
                document.getElementById("img_rank4").style.width = "0px"
                document.getElementById("img_rank5").style.width = "0px"
            } else if (num >= 3 && num <4) {
                console.log('between 3 and 4')
                document.getElementById("img_rank1").style.width = star_size
                document.getElementById("img_rank2").style.width = star_size
                document.getElementById("img_rank3").style.width = star_size
                document.getElementById("img_rank4").style.width = star_size
                document.getElementById("img_rank5").style.width = "0px"
            } else {
                console.log('greater than 4')
                document.getElementById("img_rank1").style.width = star_size
                document.getElementById("img_rank2").style.width = star_size
                document.getElementById("img_rank3").style.width = star_size
                document.getElementById("img_rank4").style.width = star_size
                console.log('num: ' + num)
                var fraction = num - 4
                console.log('fraction: ' + fraction)
                var section = star_num * fraction
                console.log('section: ' + section)
                document.getElementById("img_rank5").style.width = section + "px"
            }
            */
        } else {
            document.getElementById(fields_list[i]).value = pubs_selection[0][fields_list[i]];
        }
    }
}
