function insert_line(which_list, toggle, name, type, list_required, date_controls, input_controls, dropdown_controls, slider_controls, check_controls, star_controls){
    var actual_width = window.innerWidth;
    if(actual_width < 480) {
        var slider_col = "col-sm-6"
    } else {
        var slider_col = "col-sm-6"
    }
    const form_node = document.createElement("div");
    form_node.setAttribute("class", "form-group row");
    id_row = "row_" + name
    form_node.setAttribute("id", id_row);
    document.getElementById(which_list).appendChild(form_node);
    const label_node = document.createElement("label");
    label_node.setAttribute("class", "col-sm-3 col-form-label");
    label_node.setAttribute("for", name);
    if (type != "hidden") {
        label_node.setAttribute("style", "margin: auto; visibility: visible; display: block;");
    } else {
        label_node.setAttribute("style", "margin: auto; display: none;");
    }
    const textnode = document.createTextNode(name);
    label_node.appendChild(textnode);
    document.getElementById(id_row).appendChild(label_node);
    console.log('name: ' + name)
    if (dropdown_controls.includes(name)) {
        console.log('dropdown')
        const div_node = document.createElement("div");
        div_node.setAttribute("class", "col-sm-9");
        id_div = "div_" + name
        div_node.setAttribute("id", id_div);
        document.getElementById(id_row).appendChild(div_node);
        const select_node = document.createElement("select");
        select_node.setAttribute("class", "form-control");
        select_node.setAttribute("id", name);
        select_node.setAttribute("name", name);
        document.getElementById(id_div).appendChild(select_node);
        var option = document.createElement("option");
        option.value = "";
        switch(name) {
            case 'category':
                var options = ['Bar', 'Restaurant', 'Other']
                option.text = "select category";
                break;
            case 'star':
                var options = ['Atmosphere', 'Cleanliness', 'Clientele', 'Decor', 'Entertainment', 'Food', 'Friendliness', 'Opening', 'Price', 'Selection']
                option.text = "select venue star quality";
                break;
            case 'reviewer':
                var options = ['Andy', 'Avni', 'Both', 'Other']
                option.text = "select reviewer";
                break;
            default:
                var options = ['1', '2', '3', '4']
                option.text = ".... error ....";
        }
        select_node.appendChild(option);
        for (var i = 0; i < options.length; i++) {
            var option = document.createElement("option");
            option.value = options[i];
            option.text = options[i];
            select_node.appendChild(option);
        }
    } else if (star_controls.includes(name)) {
        console.log('star')
        const div_node = document.createElement("div");
        div_node.setAttribute("class", "col-sm-9");
        id_div = "div_" + name
        div_node.setAttribute("id", id_div);
        document.getElementById(id_row).appendChild(div_node);

        var check_node = document.createElement("input");
        check_node.setAttribute("type", 'checkbox');
        check_node.setAttribute("id", name + "check1");
        check_node.setAttribute("name", name + "check1");
        check_node.setAttribute("style", "display: none;");
        check_node.setAttribute("onclick", "myStarFunction(name + 'check1'')")
        document.getElementById(id_div).appendChild(check_node);

        const input_node = document.createElement("input");
        input_node.setAttribute("name", name);
        input_node.setAttribute("type", "text");
        input_node.setAttribute("class", "form-control");
        input_node.setAttribute("id", name);
        input_node.setAttribute("style", "display: none;");
        document.getElementById(id_div).appendChild(input_node);
        const star_node1 = document.createElement("span");
        star_node1.setAttribute("class", "fa fa-star fa-3x");
        star_node1.setAttribute("id", name + "1");
        star_node1.setAttribute("name", name + "1");
        document.getElementById(id_div).appendChild(star_node1);
        const star_node2 = document.createElement("span");
        star_node2.setAttribute("class", "fa fa-star fa-3x");
        star_node2.setAttribute("id", name + "2");
        star_node2.setAttribute("name", name + "2");
        document.getElementById(id_div).appendChild(star_node2);
        const star_node3 = document.createElement("span");
        star_node3.setAttribute("class", "fa fa-star fa-3x");
        star_node3.setAttribute("id", name + "3");
        star_node3.setAttribute("name", name + "3");
        document.getElementById(id_div).appendChild(star_node3);
        const star_node4 = document.createElement("span");
        star_node4.setAttribute("class", "fa fa-star fa-3x");
        star_node4.setAttribute("id", name + "4");
        star_node4.setAttribute("name", name + "4");
        document.getElementById(id_div).appendChild(star_node4);
        const star_node5 = document.createElement("span");
        star_node5.setAttribute("class", "fa fa-star fa-3x");
        star_node5.setAttribute("id", name + "5");
        star_node5.setAttribute("name", name + "5");
        document.getElementById(id_div).appendChild(star_node5);
    } else if (slider_controls.includes(name)) {
        console.log('slider')
        const div_node = document.createElement("div");
        div_node.setAttribute("class", slider_col);
        id_div = "div_" + name
        div_node.setAttribute("id", id_div);
        div_node.setAttribute("style", "margin: auto;");
        document.getElementById(id_row).appendChild(div_node);
        const slide_node = document.createElement("div")
        slide_node.setAttribute("class", "slidecontainer");
        slide_node.setAttribute("style", "margin: auto; width: 100%");
        id_slider = "slider_div_" + name
        slide_node.setAttribute("id", id_slider);
        document.getElementById(id_div).appendChild(slide_node);
        const input_node = document.createElement("input");
        input_node.setAttribute("type", "range");
        input_node.setAttribute("min", "0");
        if (name == 'score') {
            input_node.setAttribute("max", "100");
        } else {
            input_node.setAttribute("max", "10");
        }
        input_node.setAttribute("value", "0");
        input_node.setAttribute("class", "slider");
        input_node.setAttribute("id", name);
        input_node.setAttribute("name", name);
        input_node.setAttribute("style", "width: 100%");
        if (toggle == 'read' || name == 'score') {
            input_node.setAttribute("disabled", "true");
        }
        document.getElementById(id_slider).appendChild(input_node);
        const value_div_node = document.createElement("div");
        value_div_node.setAttribute("class", "col");
        id_value_div = "value_div_" + name
        value_div_node.setAttribute("id", id_value_div);
        document.getElementById(id_row).appendChild(value_div_node);
        const value_node = document.createElement("div")
        value_node.setAttribute("class", "col score");
        value_node.setAttribute("style", "font-family:copperplate; font-size:40px; margin: auto");
        value_node.setAttribute("id", "value_" + name);
        document.getElementById(id_value_div).appendChild(value_node);
    } else if (date_controls.includes(name)) {
        console.log('date')
        const div_node = document.createElement("div");
        div_node.setAttribute("class", "col-sm-9");
        id_div = "div_" + name
        div_node.setAttribute("id", id_div);
        document.getElementById(id_row).appendChild(div_node);
        const date_node = document.createElement("input");
        date_node.setAttribute("type", "date");
        date_node.setAttribute("id", name);
        date_node.setAttribute("name", name);
        date_node.setAttribute("placeholder", "dd-mmm-yyyy");
        document.getElementById(id_div).appendChild(date_node);
    } else if (check_controls.includes(name)) {

    } else {
        console.log('else')
        const div_node = document.createElement("div");
        div_node.setAttribute("class", "col-sm-9");
        id_div = "div_" + name
        div_node.setAttribute("id", id_div);
        if (type != "hidden") {
            div_node.setAttribute("style", "visibility: visible; display: block;");
        } else {
            div_node.setAttribute("style", "display: none;");
        }
        document.getElementById(id_row).appendChild(div_node);
        const input_node = document.createElement("input");
        input_node.setAttribute("type", type);
        input_node.setAttribute("name", name);
        input_node.setAttribute("class", "form-control");
        input_node.setAttribute("id", name);
        if (type != "hidden") {
            input_node.setAttribute("style", "visibility: visible; display: block;");
        } else {
            input_node.setAttribute("style", "display: none;");
        }
        document.getElementById(id_div).appendChild(input_node);
        if (list_required.includes(name)) {
            document.getElementById(name).required = true;
        }
    }
    if (toggle == 'readonly') {
        document.getElementById(name).readOnly = true;
    }
}
