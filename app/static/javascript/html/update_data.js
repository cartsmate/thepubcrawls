function update_features_icons(filtered_data) {
    console.log('update_features_icons')
    //console.log(filtered_data)
    review_list = ['brunch','dart','entertain','favourite','garden','history','late','music','pool','quiz','roast','sport']
    for (let i = 0; i < review_list.length; i++) {
        var image = document.getElementById(review_list[i] + "_img_2");
        var caption = document.getElementById(review_list[i] + "_caption_2");
        var checkCol = document.getElementById(review_list[i] + "_col_2");
        var count = filtered_data.filter(function (el) {
            return el[review_list[i]] == true;
        }).length;
        //console.log(count)
        if (count == filtered_data.length) {
            checkCol.style.border = "thick solid #0275D8";
            checkCol.style.background = "#0275D8"
            caption.style.color = "white"
        } else if (count > 0) {
            checkCol.style.border = "thick solid #0275D8";
            checkCol.style.background = "#BCBCBC"
            caption.style.color = "black"
        } else {
            checkCol.style.border = "thick solid #BCBCBC";
            checkCol.style.background = "#BCBCBC"
            caption.style.color = "black"
        }
    }
}
