#!/usr/bin/python3
# _*_ coding: utf-8 _*_

from flask import Flask, render_template, request
from models import register_db

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index_page():
    return render_template("index.html")

@app.route("/entry", methods=['GET'])
def entry():
    lat = request.args.get('lat', type=float)
    lng = request.args.get('lng', type=float)
    # debug用
    with open('/var/www/html/app/get_test.txt', mode="w", encoding='shift_jis') as f:
        f.write(str(type(lat)))
        f.write(f'{lat}\n')
        f.write(str(type(lng)))
        f.write(f'{lng}\n')
    # ここまで
    return render_template("entry.html", lat=lat, lng=lng)

@app.route("/entry_submit", methods=['POST'])
def entry_submit():
    submitted_data = request.form
    # debug用
    with open('/var/www/html/app/post_test.txt', mode="w", encoding='shift_jis') as f:
        f.write(str(type(submitted_data)))
        f.write('\n')
        for key,value in submitted_data.items():
            f.write(str(type(value)))
            f.write(f'{key}:{value}\n')
    # ここまで
    register_db.register_db(**submitted_data)
    return render_template("entry.html")

@app.route("/edit", methods=['GET'])
def edit():
    return render_template("edit.html")

@app.route("/edit", methods=['POST'])
def edit_post():
    return render_template("edit.html")

@app.route("/delete", methods=['GET'])
def delete():
    return render_template("delete.html")

@app.route("/delete", methods=['POST'])
def delete_post():
    return render_template("delete.html")

if __name__ == '__main__':
    app.run()