#!/usr/bin/python3
# _*_ coding: utf-8 _*_

from flask import Flask, render_template, request, flash, redirect, url_for
from models import register_db, search_db, delete_db
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
    return render_template("entry.html", lat=lat, lng=lng)

@app.route("/entry_submit", methods=['POST'])
def entry_submit():
    entry_submit_data = request.form
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
    show_submit_data = {'id':id, 'date_from':'', 'date_to':'', 'destination':'', 'category':''}
    show_results = search_db.search_db(**show_submit_data)
    return render_template("show.html", show_results=show_results)

@app.route("/delete", methods=["POST"])
def delete():
    delete_id = request.form
    delete_db.delete_db(**delete_id)
    flash("削除処理が完了しました。")
    return redirect(url_for('index'))

@app.route("/edit/<int:id>", methods=['GET'])
def edit(id):
    edit_submit_data = {'id':id, 'date_from':'', 'date_to':'', 'destination':'', 'category':''}
    edit_results = search_db.search_db(**edit_submit_data)
    return render_template("edit.html", edit_results=edit_results)

@app.route("/edit_submit", methods=['POST'])
def edit_submit():
    edit_submit_data = request.form
    flash("編集処理が完了しました。")
    return redirect(url_for('show', id=edit_submit_data['id']))

if __name__ == '__main__':
    app.run()