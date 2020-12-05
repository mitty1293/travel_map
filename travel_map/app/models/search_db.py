#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def search_db(**data):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor()

    SEARCH_SQL = 'SELECT'