#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def register_db(**data):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    # debug用
    # latlngを分けて、それぞれfloatでST_GeomFromText("POINT(%s %s)")に投入するとできた。
    # googlemapからlatlngを取得できるようになったら修正する。
    data['lat'] = 35.713364036866
    data['lng'] = 139.80851431744384
    with open('/var/www/html/app/test2.txt', mode="w", encoding='shift_jis') as f:
        dict_type = str(type(data))
        f.write(f'{dict_type}\n')
        for key,value in data.items():
            f.write(str(type(value)))
            f.write(f'{key}:{value}\n')
            f.write()
        f.write(",".join(map(str,list(data.values()))))
    # ここまで

    INSERT_SQL = 'INSERT INTO travel_map_tbl (latlng, date, destination, category, spot_name, note) VALUES (ST_GeomFromText("POINT(%s %s)"), %s, %s, %s, %s, %s)'
    #cursor.execute(INSERT_SQL, (list(data.values())))
    cursor.execute(INSERT_SQL, (data["lng"], data["lat"], data["date"], data["destination"], data["category"], data["spot_name"], data["note"]))

    cursor.close()
    connect.commit()
    connect.close()
