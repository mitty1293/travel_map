#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def edit_db(**data):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    EDIT_SQL = 'UPDATE travel_map_tbl SET date=%s, destination=%s, category=%s, spot_name=%s, address=%s, note=%s WHERE id=%s'
    cursor.execute(EDIT_SQL, (data['date'], data['destination'], data['category'], data['spot_name'], data['address'], data['note'], data['id']))

    cursor.close()
    connect.commit()
    connect.close()