from flask import Flask, render_template, request
import exact_cover_solver as ecs


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/solution", methods=["GET", "POST"])
def solution():
    if request.method == "POST":
        print(request.form, type(request.form))
        return request.form
    return "hello world"

@app.route("/sudoku")
def sudoku():
	return "hello return"

@app.route("/newroute")
def newroute():
    # retrive info as a query, if the query contains both variable a and b, then it proceeds to check the 
    # input and then trys to solve the board
    board_values = request.args.get("a", None)
    board_size =  request.args.get("b", None)
    
    """if board_values != None and board_size!= None:
        root_n = 0
        board_size = int(board_size)
        if board_size > 100:
            return "board is too big"
        
        board_list = board_values.split("n")
        invalid_input = True
        for _ in range(0, int(board_size/2)+1):
            root_n+=1  
            if root_n*root_n == board_size:
                invalid_input = False
                break
        
        if (board_size * board_size != len(board_list)) or invalid_input:
            return "invalid input"
        
        # input is valid and, everything seems ok
        board = [[int(board_list[i*board_size + j]) for j in range(board_size)] for i in range(board_size)]
        solutionExist = False
        maxSolCount = 5
        currSolCount = 0
        solutions = []
   
        # now we have both small_n, n, and the board      
        for sol in ecs.Knuth_exact_cover_solver(root_n, board_size, board):
            solutionExist = True
            currSolCount+=1
            if currSolCount == maxSolCount:
                break
            return_sol = ""
            for row in sol:
                for val in row:
                    return_sol+=str(val)
            return return_sol
            solutions.append(sol)
            break

        if not solutionExist:
            return "no solution"
        return solutions[0][:]        
        # solution_str is a string that represent the board, the string is made from the value and
        
        return esc.convert_board_to_string(solutions)
    """
    #return board_values
    #stuff = "5n3n0n0n7n0n0n0n0n6n0n0n1n9n5n0n0n0n0n9n8n0n0n0n0n6n0n8n0n0n0n6n0n0n0n3n4n0n0n8n0n3n0n0n1n7n0n0n0n2n0n0n0n6n0n6n0n0n0n0n2n8n0n0n0n0n4n1n9n0n0n5n0n0n0n0n8n0n0n7n9"
    stuff = board_values
    
    board_list = stuff.split("n")
    board_size = 9
    root_n = 3
    board = [[int(board_list[i*board_size + j]) for j in range(board_size)] for i in range(board_size)]
    solution_count = 0
    for sol in ecs.Knuth_exact_cover_solver(root_n, board_size, board):
        solution_count+=1
        return_sol = ""
        for row in sol:
            for val in row:
                return_sol+=str(val)
        return return_sol
        
        break

    return "nothing was filled"


@app.route("/page")
def page():
    #stuff = "5n3n0n0n7n0n0n0n0n6n0n0n1n9n5n0n0n0n0n9n8n0n0n0n0n6n0n8n0n0n0n6n0n0n0n3n4n0n0n8n0n3n0n0n1n7n0n0n0n2n0n0n0n6n0n6n0n0n0n0n2n8n0n0n0n0n4n1n9n0n0n5n0n0n0n0n8n0n0n7n9"
    stuff = "1n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0n0"
    board_list = stuff.split("n")
    board_size = 9
    root_n = 3
    board = [[int(board_list[i*board_size + j]) for j in range(board_size)] for i in range(board_size)]
    solution_count = 0
    for sol in ecs.Knuth_exact_cover_solver(root_n, board_size, board):
        solution_count+=1
        return_sol = ""
        for row in sol:
            for val in row:
                return_sol+=str(val)
        return return_sol
        
        break
    