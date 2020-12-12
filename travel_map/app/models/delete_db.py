#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def delete_db(**data):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    DELETE_SQL = "DELETE FROM travel_map_tbl WHERE id=%s"
    cursor.execute(DELETE_SQL, (data['id'], ))

    cursor.close()
    connect.commit()
    connect.close()