from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)

app.run(host="0.0.0.0")

@app.route("/")
def home():
    return render_template("index.html")