#!/usr/bin/python3
# _*_ coding: utf-8 _*_

from flask import Flask, render_template, request
from models import entry_submit

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index_page():
    return render_template("index.html")

@app.route("/entry", methods=['GET'])
def entry_page():
    # ここにjavascriptからのPOSTを受ける文を書く
    lat_lng = request.form
    # その後、latlngを分ける必要がないのでわけない方向にしたい
    # debug用
    with open('/var/www/html/app/get_test.txt', mode="w", encoding='shift_jis') as f:
        f.write(str(type(lat_lng)))
        f.write(f'{lat_lng}\n')
    # ここまで
    # return render_template("entry.html",lat=35.706752,lng=139.762522)
    return render_template("entry.html")

@app.route("/entry_submit", methods=['POST'])
def entry_submit():
    entry_submit_value = request.form
    # debug用
    with open('/var/www/html/app/post_test.txt', mode="w", encoding='shift_jis') as f:
        for key,value in entry_submit_value.items():
            f.write(str(type(entry_submit_value)))
            f.write(f'{key}:{value}\n')
    # ここまで
    entry_submit.entry_submit(**entry_submit_value)
    return render_template("entry.html")

@app.route("/edit", methods=['GET'])
def edit_page():
    return render_template("edit.html")

@app.route("/edit", methods=['POST'])
def edit_post():
    return render_template("edit.html")

@app.route("/delete", methods=['GET'])
def delete_page():
    return render_template("delete.html")

@app.route("/delete", methods=['POST'])
def delete_post():
    return render_template("delete.html")

if __name__ == '__main__':
    app.run()