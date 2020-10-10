#!/usr/bin/python3
# _*_ coding: utf-8 _*_

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/entry")
def entry():
    return render_template("entry.html")

@app.route("/edit")
def edit():
    return render_template("edit.html")

@app.route("/delete")
def delete():
    return render_template("delete.html")

if __name__ == '__main__':
    app.run()