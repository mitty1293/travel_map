#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def register_db(**data):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    data['lat'] = float(data['lat'])
    data['lng'] = float(data['lng'])

    INSERT_SQL = 'INSERT INTO travel_map_tbl (lat, lng, date, destination, category, spot_name, address, note) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
    cursor.execute(INSERT_SQL, (data["lat"], data["lng"], data["date"], data["destination"], data["category"], data["spot_name"], data["address"], data["note"]))

    cursor.close()
    connect.commit()
    connect.close()
