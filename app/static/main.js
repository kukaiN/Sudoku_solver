
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
    /* get the length of the row on screen*/ 
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
    /*
    this function is depreciated, use change_board_size()
    */
    var sudoku_board = document.getElementById("sudoku_board");
    var new_size = document.getElementById("board_size").value**2;
    var errorlog = document.getElementById("errorlog");
    var current_size = get_size();

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
   
}

function change_board_size(){
    var new_size_input = document.getElementById("board_size").value;
    var new_size = new_size_input * new_size_input;
    if (get_size() != new_size){
        $("#sudoku_board").empty();
        create_board(new_size_input, new_size);
    }
}

function create_board(small_size, boardsize){
    var textToInsert = [];
    var maxstr = 'max="'+ String(boardsize)+'"';
    for(var i=0; i<boardsize; ++i){
        textToInsert.push('<tr>');
        for(var j =0; j<boardsize; ++j){
            if (i % small_size==0){
                if (j%small_size == 0 ){
                    textToInsert.push('<td> <input class="sudoku_cell leftborder topborder" type="number" min="1" '+ maxstr+'/></td>');
                }
                else if (j==boardsize-1){
                    textToInsert.push('<td> <input class="sudoku_cell topborder rightborder" type="number" min="1" '+ maxstr+'/></td>');
                }
                else{
                    textToInsert.push('<td> <input class="sudoku_cell topborder" type="number" min="1" '+ maxstr+'/></td>');
                }
            }
            else if (j%small_size==0 && i == boardsize-1){
                textToInsert.push('<td> <input class="sudoku_cell leftborder bottomborder" type="number" min="1" '+ maxstr+'/></td>');
            }
            else if (j%small_size==0){
                textToInsert.push('<td> <input class="sudoku_cell leftborder" type="number" min="1" '+ maxstr+'/></td>');
            }
            else if (j==boardsize-1 && i==boardsize-1){
                textToInsert.push('<td> <input class="sudoku_cell rightborder bottomborder" type="number" min="1" '+ maxstr+'/></td>');
            }
            else if (j==boardsize-1){
                textToInsert.push('<td> <input class="sudoku_cell rightborder" type="number" min="1" '+ maxstr+'/></td>');
            }
            else if (i==boardsize-1){
                textToInsert.push('<td> <input class="sudoku_cell bottomborder" type="number" min="1" '+ maxstr+'/></td>');
            }
            else{
                textToInsert.push('<td> <input class="sudoku_cell" type="number" min="1" '+ maxstr+'/></td>');
            }
        }
        textToInsert.push('</tr>');
    }
    $("#sudoku_board").append(textToInsert.join(''));
}

function get_board_value(){
    /*
    gets the value of the sudoku board as a 1D array, 
    the funcion also checks that the entries written into the array is valid
    the values stored in array are valid, but that doesn't mean the board is valid
    */
    var size = get_size();
    var board = document.getElementById("sudoku_board");
    // create a n*n array initialized with 0
    let board_to_return = new Array(size*size);
    for (let i=0; i< size*size; ++i){board_to_return[i] = 0;}
    // iterate over i, j coordinate of board
    for (var i = 0; i<size;++i){
        // get html element of table row
        var curr_row = board.rows[i];
        // iterate over each table cell in that row
        for (var j = 0; j<size; ++j){
            var stored_val = parseInt(curr_row.cells[j].getElementsByClassName("sudoku_cell")[0].value);
            // check if that cell is filled and its a valid input
            if (!isNaN(stored_val) && (stored_val > 0) && (stored_val < size+1)){
                board_to_return[(i*size)+j] = stored_val;
            }
        }
    }
    console.log("the value stored in the cells:")
    console.log(board_to_return)
    return board_to_return
}

function get_board_as_string(boardArr){
    var returnval = boardArr.join("n")
    console.log(returnval)
    return returnval
}

function submit_board(){
    // submit the current board to the server as a string, commas have a special meaning
    // in urls, so i use the letter n to separate the numbers
    var boardArr = get_board_value()
    var board_size = get_size();
    var boardArrString = get_board_as_string(boardArr)
    console.log("tyring to submit")
    $.get("/newroute", {a:boardArrString, b: board_size}).done(function(data){
        console.log(data)
        console.log("finished submmiting")
    });
}
