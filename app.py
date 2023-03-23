from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "2e8d325bb6efd3c9"

@app.route("/main")
def index():
    return render_template("index.html")
    