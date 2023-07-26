function check_week_list(value) {
    console.log('check_week')
    auto_exec = document.getElementById('auto_exec').value
    diary_headers = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    //diary_headers = {{diary_headers | tojson}}
    for (let i = 0; i < diary_headers.length; i++) {
        var checkBox = document.getElementById(diary_headers[i] + "_2")
        var imageBox = document.getElementById(diary_headers[i] + "_img_2")
        if (diary_headers[i] == value) {
            if (checkBox.checked == true) {
                imageBox.style.opacity = "1"
                document.getElementById('day_2').value = value
                document.getElementById('x_day').value = value
            } else {
                imageBox.style.opacity = "0.25"
                document.getElementById('day_2').value = 'all'
                document.getElementById('x_day').value = value
            }
        } else {
            checkBox.checked = false
            imageBox.style.opacity = "0.25"
        }
    }
    if (auto_exec == 'on') {
        console.log('auto_exec: on')
        update_data()
    }
}