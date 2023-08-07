function check_week_home(value) {
    console.log('check_week_home')
    console.log('value: ' + value)
    auto_exec = document.getElementById('auto_exec').value
    diary_headers = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    //diary_headers = {{diary_headers | tojson}}
    for (let i = 0; i < diary_headers.length; i++) {
        var checkBox = document.getElementById('btn_' + diary_headers[i])
        var imageBox = document.getElementById(diary_headers[i] + "_img")
        if (diary_headers[i] == value) {
            console.log('TRUE')
            if (checkBox.checked == true) {
                imageBox.style.opacity = "1"
                document.getElementById('day').value = value
                document.getElementById('x_day').value = value
            } else {
                imageBox.style.opacity = "0.25"
                document.getElementById('day').value = 'all'
                document.getElementById('x_day').value = value
            }
        } else {
            console.log('FALSE')
            checkBox.checked = false
            imageBox.style.opacity = "0.25"
        }
    }
}
