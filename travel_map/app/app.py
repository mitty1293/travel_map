#!/usr/bin/python3
# _*_ coding: utf-8 _*_

from flask import Flask, render_template, request, flash, redirect, url_for
from models import register_db, search_db
import random, string

app = Flask(__name__)
app.secret_key = "".join([random.choice(string.ascii_letters + string.digits + '_' + '-' + '!' + '#' + '&') for i in range(12)])

@app.route("/", methods=['GET'])
def index():
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
    entry_submit_data = request.form
    # debug用
    with open('/var/www/html/app/post_test.txt', mode="w", encoding='shift_jis') as f:
        f.write(str(type(entry_submit_data)))
        f.write('\n')
        for key,value in entry_submit_data.items():
            f.write(str(type(value)))
            f.write(f'{key}:{value}\n')
    # ここまで
    register_db.register_db(**entry_submit_data)
    flash("登録処理が完了しました。")
    return redirect(url_for('index'))

@app.route("/search", methods=['GET'])
def search():
    search_submit_data = {'date_from':'', 'date_to':'', 'destination':'', 'category':''}
    return render_template("search.html", search_submit_data=search_submit_data)

@app.route("/search_submit", methods=['POST'])
def search_submit():
    search_submit_data = request.form
    search_results = search_db.search_db(**search_submit_data)
    # debug用
    with open('/var/www/html/app/search_db_test3.txt', mode="w", encoding='shift_jis') as f:
        f.write(str(type(search_results)))
        f.write('\n')
        for result in search_results:
            f.write(str(type(result)))
            f.write(f'{result}\n')
    # ここまで
    return render_template("search.html", search_submit_data=search_submit_data, search_results=search_results)

@app.route("/show/<int:id>", methods=['GET'])
def show(id):
    pass

if __name__ == '__main__':
    app.run()