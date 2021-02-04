Storage.prototype.setObj = function(key, value){
    return this.setItem(key, JSON.stringify(value));
}
Storage.prototype.getObj = function(key, value){
    return JSON.parse(this.getItem(key));
}


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
    let board_to_return = zeroArr(size*size);
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
    var boardArrString = get_board_as_string(boardArr);
    console.log("tyring to submit board info");
    $.get("/newroute", {a:boardArrString, b: board_size}).done(function(data){
        if (data.length > 0){
            if (data.charAt(0) == "!"){
                console.log("a message from server");
                console.log(data);
            }
            else{
                var sol_list = data.split("x");
                localStorage.setItem("current_board", boardArr);
                localStorage.setItem("board_state", boardArrString);
                localStorage.setItem("board_length", board_size);
                localStorage.setObj("sol_list", sol_list);
                localStorage.setItem("sol_length", sol_list.length);
                console.log(sol_list);
                show_solution_box();
            }
        }
        else {
            console.log("nothing returned from server");
        }
        
    });
}

function show_solution_box(){
    console.log("this function")
    var sol_len = localStorage.getItem("sol_length") 
    if (sol_len){
        if (sol_len == 1){
            var previous_board = localStorage.getItem("current_board");
            var solution_list = localStorage.getObj("sol_list")
            var unique_solution = solution_list[0];
            localStorage.setItem("previous_board", previous_board);
            localStorage.setItem("current_board", unique_solution);
            console.log(localStorage.getItem("board_length"))
            insert_values(unique_solution, localStorage.getItem("board_length"));
        }
        else if (sol_len > 1){// make tabs to switch between values
            console.log("box will show up")
            var textToInsert = [];
           
            var sol_size = localStorage.getItem("board_length")
            for(var i=0; i<sol_size; ++i){
                var input_str = '<td> <input type="button" value="show solution" onclick="fill_sol_num( '+i+')"/></td>'
              
                textToInsert.push('<tr>');
                textToInsert.push(input_str);
                textToInsert.push('</tr>');
                
            }
            console.log(textToInsert);
            $("#solutionList").append(textToInsert.join(''));
        }
        clear_solution();
    }
}
function clear_solution(){
    var textToInsert = [];
    textToInsert.append('<td> <input type="button" value="hide solution" onclick="fill_sol_num(-1)"/></td>')
    $("#solutionList").append(textToInsert.join(''))
}



function fill_sol_num(numstr){
    var num = parseInt(numstr)
    var sol_list = localStorage.getObj("sol_list")
    var sol_size = localStorage.getItem("board_length")

    if (num < 0){
        var previous_board = localStorage.getItem("current_board");
        insert_values(previous_board, sol_size)
    }
    else{
        var sol = sol_list[num].split("n")
        insert_values(sol, sol_size)
    }
}
    

function clear_board(){
    var board_val = get_board_value();
    var board_size = get_size();
    var clear = false;
    // first check if there is a value thats non-zero
    for (var i = 0; i < board_size*board_size; ++i){
       if (board_val[i] != 0){
           clear = true;
       }
    }
    // if the user says yes, clean the board
    if (clear && confirm("Are you sure you want to clear the board?")){
        insert_values(zeroArr(board_size*board_size), board_size)
    }
}

function delete_board(){
    // deletes the whole table
    $("#sudoku_board").empty();
}

function insert_values(numArray, board_size){
    console.log("trying to insert:")
    console.log(numArray)
    console.log(board_size)
    console.log(numArray.length)
    if (numArray.length != board_size * board_size){
        console.log("the number sequence and the board doesnt match");
        return 0;
    }
    var board_obj = document.getElementById("sudoku_board");
        for (var i = 0; i < board_size; ++i){ // modify the current rows and extend them
            var curr_row = board_obj.rows[i];
            for (var j = 0; j < board_size; ++j){
                var curr_cell = curr_row.cells[j];
                curr_cell.getElementsByClassName("sudoku_cell")[0].value = numArray[i*board_size + j];
        }}
}

function zeroArr(n){
    let board_to_return = new Array(n);
    for (let i=0; i< n; ++i){board_to_return[i] = 0;}
    return board_to_return
}



