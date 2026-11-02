from flask import Flask, render_template
from config import PROJECT

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", project=PROJECT)

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html", project=PROJECT)

@app.route("/story")
def story():
    return render_template("story.html", project=PROJECT)

if __name__ == "__main__":
    app.run(debug=True)
