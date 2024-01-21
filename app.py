from flask import Flask
from flask import render_template
from flask import request
from flask import flash

app = Flask(__name__)
app.secret_key = "manwith2hands" ## To handle error of secret key, add secret key.


@app.route("/")
def index():
    flash("what is your name?")
    return render_template("index.html") ## Rendering the index.html


@app.route("/greet", methods = ["POST", "GET"])
def greet():
    flash("Hi " + str(request.form['name_input']) + ", great to see you!") ## Giving the final message
    return render_template("index.html")