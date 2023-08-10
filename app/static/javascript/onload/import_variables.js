function import_variables() {
    console.log("import_variables")
    pub_id = {{ pub_id | tojson }}
    icon_list = {{ icon_list | tojson }}
    config2 = {{ config2 | tojson }}
    areas = {{ areas | tojson }}
    all_data = {{ all_data | tojson }}
    alias = {{ alias | tojson }}
    headers = {{ headers | tojson }}
    visible = {{ visible | tojson }}
    all_data = {{ all_data | tojson }}
    review_obj = "{{ review_obj }}"
    review_obj2 = "{{ review_obj2 }}"
    key = {{ google_key | tojson }}
    stations_directions_list = {{ stations_directions_list | tojson }}
    fields_list = {{ fields_list | tojson }}
    form_visible_list = {{ form_visible_list | tojson }}
    alias_list = {{ alias_list | tojson }}
    required_list = {{ required_list | tojson }}
    input_list = {{ input_list | tojson }}
    dropdown_list = {{ dropdown_list | tojson }}
    slider_list = {{ slider_list | tojson }}
    check_list = {{ check_list | tojson }}
    date_controls = {{ date_list | tojson }}
    star_list = {{ star_list | tojson }}
    counter = {{ counter | tojson }}
}
