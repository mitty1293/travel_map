#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def entry(**entry_post_value):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    # debug用
    entry_post_value['latlng'] = "139.762522 35.706752"
    with open('/var/www/html/app/test2.txt', mode="w", encoding='shift_jis') as f:
        for key,value in entry_post_value.items():
            f.write(str(type(entry_post_value)))
            f.write(f'{key}:{value}\n')
        f.write(",".join(map(str,list(entry_post_value.values()))))
    # ここまで

    INSERT_SQL = 'INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(%s)"), %s, %s, %s, %s, %s)'
    #cursor.execute(INSERT_SQL, (list(entry_post_value.values())))
    cursor.execute(INSERT_SQL, (entry_post_value["latlng"], entry_post_value["date"], entry_post_value["destination"], entry_post_value["category"], entry_post_value["spot_name"], entry_post_value["note"]))

# latlangを緯度経度分けて2つのintつぃて作ってみる。entry.htmlで緯度経度2つにわけるところから

    cursor.close()
    connect.commit()
    connect.close()
