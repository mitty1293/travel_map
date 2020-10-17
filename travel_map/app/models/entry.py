#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def entry(**entry_post_value):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    # debug用
    with open('/var/www/html/app/test2.txt', mode="w", encoding='shift_jis') as f:
        for key,value in entry_post_value.items():
            f.write(str(type(entry_post_value)))
            f.write(f'{key}:{value}\n')
    # ここまで

    INSERT_SQL = 'INSERT INTO travel_map_tbl (latlang, date, destination, category, spot_name, note) VALUES (%s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(INSERT_SQL, (entry_post_value.values()))

    cursor.close()
    connect.commit()
    connect.close()
