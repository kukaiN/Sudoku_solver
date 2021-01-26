
function checker(){
    var board = document.getElementById("sudoku_board");
    var curr_size = get_size();
    for (var i = 0; i<curr_size; ++i){
        var curr_row = board.rows[i];
        for (var j = 0; j < curr_size; ++j){
            var curr_cell = curr_row.cells[j];
            var stored_str = curr_cell.getElementsByClassName("sudoku_cell")[0].value;
            console.log(stored_str);
            if (!isNaN(stored_str)){
                var stored_num = parseInt(stored_str);
                if (stored_num > 0 && stored_num < get_size()+1) {curr_cell.style.background = document.body.style.background;}
                else {
                    curr_cell.style.backgroundColor = "rgba(255, 0, 0, 0.4)";
                    }
                }
}}}

function get_size(){
    return document.getElementById("sudoku_board").rows.length;
}


// table functions
function delete_row(table_object, curr_size, new_size){
    for (var i = new_size; i < curr_size; ++i){
        table_object.deleteRow(-1);
    }
}
function delete_cells(table_object, curr_size, new_size){
    // delete few extra cells in the current board
    for (var i = 0; i < new_size; ++i) {
        var curr_row = table_object.rows[i];
          for (var j = new_size; j<curr_size; ++j){
              curr_row.deleteCell(-1);
}}}

function add_row(table_object, curr_size, new_size){
    for (var i = curr_size; i < new_size; ++i){
        var curr_row = table_object.insertRow(-1);
        for (var j = 0; j<new_size; ++j){
            var new_cell = curr_row.insertCell(-1);
            new_cell.appendChild(make_input());
}}}

function make_input(){
    var newinput = document.createElement("input");
    newinput.type = "text";
    //newinput.value = "" + Math.floor(Math.random()*get_size());
    newinput.className = "sudoku_cell";
    return newinput;
}
function add_cells(table_object, curr_size, new_size) {
    for (var i = 0; i < curr_size; ++i){ // modify the current rows and extend them
        var curr_row = table_object.rows[i];
        for (var j = curr_size; j < new_size; ++j){
            var new_cell = curr_row.insertCell(-1);
            new_cell.appendChild(make_input());
}}}
function change_size(){// modify the board size on screen
    var sudoku_board = document.getElementById("sudoku_board");
    var new_size = document.getElementById("board_size").value**2;
    var errorlog = document.getElementById("errorlog");
    var current_size = get_size();


    console.log(current_size);
    if (current_size == 0){
        add_row(sudoku_board, 0, new_size);
    }
    if (new_size > current_size) {
        add_cells(sudoku_board, current_size, new_size);
        add_row(sudoku_board, current_size, new_size);
    }
    else if (current_size > new_size) {
        delete_cells(sudoku_board, current_size, new_size);
        delete_row(sudoku_board, current_size, new_size);
    }
    else{
        // pass, cause no need to modify board
    }
    change_size1();
}

function change_size1(){

    var textToInsert = [];
    var boardsize = 9;
    for(var i =0 ; i< boardsize; ++i){
        textToInsert.push('<tr>');
        for(var j =0; j<boardsize; ++j){
            textToInsert.push('<td>h</td>');
        }
        textToInsert.push('</tr>');
    }
    //$("#div1").append("hello");
    //$("#div1").append("<h1>hello</h1>");
    $("#div1").append(textToInsert.join(''));
}