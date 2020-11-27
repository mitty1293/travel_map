#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def entry_submit(**entry_submit_value):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    # debug用
    # latlngを分けて、それぞれfloatでST_GeomFromText("POINT(%s %s)")に投入するとできた。
    # googlemapからlatlngを取得できるようになったら修正する。
    entry_submit_value['lat'] = 35.706752
    entry_submit_value['lng'] = 139.762522
    with open('/var/www/html/app/test2.txt', mode="w", encoding='shift_jis') as f:
        for key,value in entry_submit_value.items():
            f.write(str(type(entry_submit_value)))
            f.write(f'{key}:{value}\n')
        f.write(",".join(map(str,list(entry_submit_value.values()))))
    # ここまで

    INSERT_SQL = 'INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(%s %s)"), %s, %s, %s, %s, %s)'
    #cursor.execute(INSERT_SQL, (list(entry_submit_value.values())))
    cursor.execute(INSERT_SQL, (entry_submit_value["lng"], entry_submit_value["lat"],entry_submit_value["date"], entry_submit_value["destination"], entry_submit_value["category"], entry_submit_value["spot_name"], entry_submit_value["note"]))

    cursor.close()
    connect.commit()
    connect.close()
