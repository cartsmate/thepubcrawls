function populate_diary(filtered_data){
    console.log('POPULATE_DIARY')
    diary_headers = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    for (i = 0; i < diary_headers.length; i++) {
        //console.log('diary_headers[i]')
        //console.log(diary_headers[i])
        //console.log(diary_body[0][diary_headers[i]])
        document.getElementById(diary_headers[i]).value = filtered_data[0][diary_headers[i]];
        }
}
