function update_icons_pub(filtered_data) {
    console.log('UPDATE_ICONS_PUB')
    //console.log('filtered_data')
    //console.log(filtered_data)
    review_list = ['brunch','dart','entertain','favourite','garden','history','late','music','pool','quiz','roast','sport']
    for (let i = 0; i < review_list.length; i++) {
        //console.log('review_list[i]')
        //console.log(review_list[i])
        var image = document.getElementById(review_list[i] + "_img");
        var caption = document.getElementById(review_list[i] + "_caption");
        var checkCol = document.getElementById(review_list[i] + "_col");
        var count = filtered_data.filter(function (el) {
            return el[review_list[i]] == 'true';
        }).length;
        console.log(review_list[i] + " : " + count)
        document.getElementById(review_list[i]).setAttribute("onclick", "feature_click_list('" + review_list[i] + "')")
        if (count == filtered_data.length) {
            //console.log('all')
            checkCol.style.border = "thick solid #0275D8";
            checkCol.style.background = "#0275D8"
            caption.style.color = "white"
        } else if (count > 0) {
            //console.log('some')
            checkCol.style.border = "thick solid #0275D8";
            checkCol.style.background = "#BCBCBC"
            caption.style.color = "black"
        } else {
            //console.log('none')
            checkCol.style.border = "thick solid #BCBCBC";
            checkCol.style.background = "#BCBCBC"
            caption.style.color = "black"
        }
    }
}
