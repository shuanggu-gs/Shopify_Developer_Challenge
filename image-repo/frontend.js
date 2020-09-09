var data;

function create_table(startRow, endRow, columnSize) {
    var num = endRow - startRow;
    var rows = parseInt(num / columnSize);

    if (document.getElementById("review_table")) {
        document.getElementById("review_table").remove();
    }

    var table = document.createElement('table');
    table.setAttribute('id', 'review_table');
    table.setAttribute('class', 'table');

    for(var i = 0; i < rows; i++ ) {
        var row = table.insertRow();
        for (var j = 0; j < columnSize; j++ ) {
              var cell = row.insertCell();
              var index = startRow + i*columnSize + j;
              if (index < data['url'].length) {
                    var img = document.createElement('img');
                    img.setAttribute('class', 'grid_image');
                    img.src = data['url'][index];
                    cell.appendChild(img);
              }
        }
    }
    return table
}

function goPage(pno, psize=20, columnSize=5) {

    var keys = Object.keys(data);
    var values = Object.values(data);
    var num = data[keys[0]].length; // number of records

    if (num == 0) {
        alert("Sorry! Nothing Found!")
    } else {
        var totalPage = 0; // number of pages
        var pageSize = psize; // number of records shown on each page

        if (num / pageSize > parseInt(num / pageSize)) {
            totalPage = parseInt(num / pageSize) + 1;
        } else {
            totalPage = parseInt(num / pageSize);
        }

        var currentPage = pno;
        var startRow = (currentPage - 1) * pageSize; // first page start from 0
        var endRow = currentPage * pageSize; // first page end with psize=25
        endRow = (endRow > num) ? num : endRow;



        var maintext = document.getElementById("maintext");
        var table = create_table(startRow, endRow, columnSize)
        maintext.innerHTML = '';
        maintext.appendChild(table);

        var tempStr = "";
        tempStr += "<button onClick=\"goPage(" + 1 + "," + psize + ")\">First</button>";
        if (currentPage == 1) {
            tempStr += "<button onClick=\"goPage(" + (currentPage) + "," + psize + ")\" disabled>< Prev</button>";
        } else {
            tempStr += "<button onClick=\"goPage(" + (currentPage - 1) + "," + psize + ")\">< Prev</button>";
        }

        tempStr += "<a>" + currentPage + "/" + totalPage + "</a>";
        if (currentPage == totalPage) {
            tempStr += "<button onClick=\"goPage(" + (currentPage) + "," + psize + ")\" disabled>Next ></button>";
        } else {
            tempStr += "<button onClick=\"goPage(" + (currentPage + 1) + "," + psize + ")\">Next ></button>";
        }
        tempStr += "<button onClick=\"goPage(" + totalPage + "," + psize + ")\"> Last</button>";

        document.getElementById("barcon").innerHTML = tempStr;
    }
}


function sumbit_form() {
    var form = document.getElementById("form");
    var formData = new FormData(form);
    console.log(formData.getAll)

    xmlHttpRqst = new XMLHttpRequest()
    xmlHttpRqst.open('post', '/upload');

    xmlHttpRqst.onload = function(e) {
        data =  JSON.parse(xmlHttpRqst.response);
        goPage(pno=1, psize=20)
    }
    xmlHttpRqst.send(formData);
    form.reset();
}


