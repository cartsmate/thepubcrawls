function go_week() {
    console.log("go_week")
    /*
    //console.log(direction)
    //console.log(station)
    var base_url = window.location.hostname
    if (config2['env'] == 'prod') {
        var url = "http://" + base_url + "/pub/list/"
    } else {
        var url = "http://" + base_url + ":5000/pub/list/"
    }
    const myUrlWithParams = new URL(url);
    myUrlWithParams.searchParams.append('direction', document.getElementById('direction').value);
    myUrlWithParams.searchParams.append('station', document.getElementById('station').value);
    myUrlWithParams.searchParams.append('day', document.getElementById('day').value);
    for (var i = 0; i < icon_list.length; i++) {
        console.log(icon_list[i])
        console.log(document.getElementById(icon_list[i]).checked)
        myUrlWithParams.searchParams.append(icon_list[i], document.getElementById(icon_list[i]).checked);
    }
    window.location.replace(myUrlWithParams.href);
    */
    document.getElementById('home_page').style.display = "none"
    document.getElementById('header_page').style.display = "block"
    document.getElementById('list_page1').style.display = "block"
    document.getElementById('list_page2').style.display = "block"

    document.getElementById('form_type').value = 'list'
    document.getElementById('auto_exec').value = 'on'

    review_list = ['brunch','dart','entertain','favourite','garden','history','late','music','pool','quiz','roast','sport']
    for (let i = 0; i < review_list.length; i++) {
        var image = document.getElementById(review_list[i] + "_img_2");
        //var caption = document.getElementById(review_list[i] + "_caption_2");
        var checkCol = document.getElementById(review_list[i] + "_col_2");
        if (document.getElementById("x_" + review_list[i]).value == 'true'){
            console.log(review_list[i] + ' : TRUE')
            image.style.opacity = "1"
            //caption.style.opacity = "1.0"
            //caption.style.color = "white"
            checkCol.style.background = "#0275D8"
            //checkCol.style.border = "thick solid #0275D8";
        } else {
            console.log(review_list[i] + ' : FALSE')
            image.style.opacity = "1"
            //caption.style.opacity = "1.0"
            //caption.style.color = "black"
            checkCol.style.background = "#CDCDCD"
        }
    }
    week_list = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    for (let i = 0; i < week_list.length; i++) {
        var image = document.getElementById(week_list[i] + "_img_2");
        if (document.getElementById(week_list[i] + "_2").value == document.getElementById("x_day").value) {
            console.log(week_list[i] + '_2 : TRUE')
            image.style.opacity = "1.0"
        } else {
            console.log(week_list[i] + '_2 : FALSE')
            image.style.opacity = "0.5"
        }
    }

    update_data()

}
