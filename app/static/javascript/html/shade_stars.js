function shadeStars(star, num, where){
    console.log('shadeStars')
    //console.log('shade stars from ' + where)
    //console.log('rating: ' + num)
    //console.log(star)
    star_num = 30
    star_size = star_num + "px"
    document.getElementById(star).value = num;
    //num = pub_review[0][star]
    if (num > 0 && num <1) {
        //console.log('between 0 and 1')
        document.getElementById("img_rank1").style.width = star_size
        document.getElementById("img_rank2").style.width = "0px"
        document.getElementById("img_rank3").style.width = "0px"
        document.getElementById("img_rank4").style.width = "0px"
        document.getElementById("img_rank5").style.width = "0px"
    } else if (num >= 1 && num <2) {
        //console.log('between 1 and 2')
        document.getElementById("img_rank1").style.width = star_size
        document.getElementById("img_rank2").style.width = star_size
        document.getElementById("img_rank3").style.width = "0px"
        document.getElementById("img_rank4").style.width = "0px"
        document.getElementById("img_rank5").style.width = "0px"
    } else if (num >= 2 && num <3) {
        //console.log('between 2 and 3')
        document.getElementById("img_rank1").style.width = star_size
        document.getElementById("img_rank2").style.width = star_size
        document.getElementById("img_rank3").style.width = star_size
        document.getElementById("img_rank4").style.width = "0px"
        document.getElementById("img_rank5").style.width = "0px"
    } else if (num >= 3 && num <4) {
        //console.log('between 3 and 4')
        document.getElementById("img_rank1").style.width = star_size
        document.getElementById("img_rank2").style.width = star_size
        document.getElementById("img_rank3").style.width = star_size
        document.getElementById("img_rank4").style.width = star_size
        document.getElementById("img_rank5").style.width = "0px"
    } else {
        //console.log('greater than 4')
        document.getElementById("img_rank1").style.width = star_size
        document.getElementById("img_rank2").style.width = star_size
        document.getElementById("img_rank3").style.width = star_size
        document.getElementById("img_rank4").style.width = star_size
        //console.log('num: ' + num)
        var fraction = num - 4
        //console.log('fraction: ' + fraction)
        var section = star_num * fraction
        //console.log('section: ' + section)
        document.getElementById("img_rank5").style.width = section + "px"
    }
}
