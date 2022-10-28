from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>林琮耀個人網頁</h1>"
    homepage += "<a href=/Personal>Personal</a><br>"
    homepage += "<a href=/Profession>Profession</a><br>"
    homepage += "<a href=/UCAN>UCAN</a><br>"
    homepage += "<a href=/interest>interest</a><br>"
    return homepage

@app.route("/Personal")
def Personal():
    return render_template("Personal.html")

@app.route("/Profession")
def Profession():
    return render_template("Profession.html")

@app.route("/UCAN")
def UCAN():
    return render_template("UCAN.html")

@app.route("/interest")
def interest():
    return render_template("interest.html")


#if __name__ == "__main__":
#   app.run()
