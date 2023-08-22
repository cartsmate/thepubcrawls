function populate_form(pubs_selection){
    console.log('POPULATE_FORM')
    //console.log(pubs_selection)
    for (i = 0; i < fields_list.length; i++) {
        //console.log('fields_list[i]')
        //console.log(fields_list[i])
        //console.log(check_list)
        if (dropdown_list.includes(fields_list[i])) {
            //console.log('dropdown')
            var dropdown_str = String(pubs_selection[0][fields_list[i]]['0']).toUpperCase() + String(pubs_selection[0][fields_list[i]]).substring(1)
            document.getElementById(fields_list[i]).value = dropdown_str
        } else if (check_list.includes(fields_list[i])) {
            //console.log('checklist')
            if (pubs_selection[0][fields_list[i]] == 'true') {
                //console.log('true')
                document.getElementById(fields_list[i]).checked = 'true';
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
        } else {
            document.getElementById(fields_list[i]).value = pubs_selection[0][fields_list[i]];
        }
    }
}
