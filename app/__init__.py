from flask import Flask



app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html" board_size=request)

@app.route("solution", methods=["GET", "POST"])
def solution():

    user_input = request.form.get()