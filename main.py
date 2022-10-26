#Zodiac sign
#DIfferent information about the zodiac signs
#Programmers:
#Laurence Jade Javier
#Ernest Sacdal
#John Ken Talusan
#October 27 2022
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/home")
def home():
   return render_template("index.html")

@app.route("/pageOne")
def pageOne():
   return render_template("page1.html")

@app.route("/pageTwo")
def pageTwo():
   return render_template("page2.html")

@app.route("/pageThree")
def pageThree():
   return render_template("page3.html")

@app.route("/pageFour")
def pageFour():
   return render_template("page4.html")

@app.route("/about")
def about():
   return render_template("about.html")

@app.route("/members")
def members():
   return render_template("members.html")


if __name__ == "__main__":
   app.run()