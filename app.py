from flask import Flask, render_template
#cd /path-to-repository
#github-linguist gem

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("hey.html")
