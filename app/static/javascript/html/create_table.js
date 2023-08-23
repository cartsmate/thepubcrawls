function create_table(pubs_selection) {
    console.log('CREATE_TABLE')
    console.log('pubs_selection')
    console.log(pubs_selection)
    //console.log(pubs_selection[0]['address'])
    //console.log(pubs_selection[0]['distance'])
    console.log('visible')
    console.log(visible)
    //console.log('all_data')
    //console.log(all_data)
    //var tbl = document.getElementById('pub_list');
        //if(tbl) tbl.parentNode.removeChild(tbl);
  // creates a <table> element and a <tbody> element
    var tbl = document.createElement("table");
    tbl.setAttribute("id", "pub_list");
    tbl.style.cssText = 'font-size:14px;'
    tbl.className = "table table-striped";

    var tblBody = document.createElement("tbody");
    var header = tbl.createTHead();
    var row = header.insertRow(0);
    for (let k = 0; k < headers.length; k++) {
        var cell = row.insertCell(k);
        cell.innerHTML = "<b>" + alias[headers[k]] + "</b>";
        }

  // creating all cells
    for (let i = 0; i < pubs_selection.length; i++) {
    // creates a table row
        var row = document.createElement("tr");

        for (let j = 0; j < headers.length; j++) {
            /*
            if (headers[j] == 'distance') {
                console.log('headers[j]')
                console.log(headers[j])
                console.log(pubs_selection[i]['station_identity'])
                console.log(pubs_selection[i]['distance'])
            }
            */
      // Create a <td> element and a text node, make the text
      // node the contents of the <td>, and put the <td> at
      // the end of the table row
            const cell = document.createElement("td");
            const href = document.createElement("a");
            if (headers[j] == 'station_name') {
                href.setAttribute("href", "#");
                href.setAttribute("onclick", "click_station('" + pubs_selection[i]['station_identity'] + "')");
                text_ref = pubs_selection[i][headers[j]]
                const cellText = document.createTextNode(text_ref);
                href.appendChild(cellText);
                cell.appendChild(href)
                row.appendChild(cell);
                } else if (headers[j] == 'pub_name') {
                    href.setAttribute("href", "#");
                    href.setAttribute("onclick", "click_pub('" + pubs_selection[i]['pub_identity'] + "',)");
                    text_ref = pubs_selection[i][headers[j]]
                    const cellText = document.createTextNode(text_ref);
                    href.appendChild(cellText);
                    cell.appendChild(href)
                    row.appendChild(cell);
                } else {
                    text_ref = pubs_selection[i][headers[j]]
                    const cellText = document.createTextNode(text_ref);
                    cell.appendChild(cellText)
                    row.appendChild(cell);
                }
            }

    // add the row to the end of the table body
        tblBody.appendChild(row);
        }

  // put the <tbody> in the <table>
    tbl.appendChild(tblBody);
  // appends <table> into <body>
  //document.body.appendChild(tbl);
    document.getElementById('dynamic_table').appendChild(tbl)
  // sets the border attribute of tbl to '2'
    tbl.setAttribute("border", "2");

}