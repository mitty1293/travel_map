#!/usr/bin/python3
# _*_ coding: utf-8 _*_

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index_get():
    return render_template("index.html")

@app.route("/entry", methods=['GET'])
def entry_get():
    return render_template("entry.html")

@app.route("/entry", methods=['POST'])
def entry_post():
    return render_template("entry.html")

@app.route("/edit", methods=['GET'])
def edit_get():
    return render_template("edit.html")

@app.route("/edit", methods=['POST'])
def edit_post():
    return render_template("edit.html")

@app.route("/delete", methods=['GET'])
def delete_get():
    return render_template("delete.html")

@app.route("/delete", methods=['POST'])
def delete_post():
    return render_template("delete.html")

if __name__ == '__main__':
    app.run()