#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def search_db(**data):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    # debug用
    with open('/var/www/html/app/search_db_test.txt', mode="w", encoding='shift_jis') as f:
        f.write(str(type(data)))
        f.write('\n')
        for key,value in data.items():
            f.write(str(type(value)))
            f.write(f'{key}:{value}\n')
        f.write(",".join(map(str,list(data.values()))))
    # ここまで

    SEARCH_SQL = 'SELECT * FROM travel_map_tbl WHERE category=%s'
    cursor.execute(SEARCH_SQL, (data['category'], ))
    results = cursor.fetchall()
    # debug用
    with open('/var/www/html/app/search_db_test2.txt', mode="w", encoding='shift_jis') as f:
        for result in results:
            f.write(f'{result}\n')
    # ここまで
    return results