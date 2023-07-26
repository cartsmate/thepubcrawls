function populate_diary(){
    console.log('populate diary')
    for (i = 0; i < diary_headers.length; i++) {
        //console.log(diary_headers[i])
        //console.log(diary_body[0][diary_headers[i]])
        document.getElementById(diary_headers[i]).value = diary_body[0][diary_headers[i]];
        }
}
