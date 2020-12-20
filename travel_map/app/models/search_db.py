#!/usr/bin/python3
# _*_ coding: utf-8 _*_

import mysql.connector

def search_db(**data):
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor(dictionary=True)

    SEARCH_SQL = '''SELECT * FROM travel_map_tbl
    WHERE
    id = CASE
        WHEN %s <> '' THEN
            %s
        ELSE
            id
    END
    AND
    date BETWEEN CASE
        WHEN %s <> '' THEN
            %s
        ELSE
            '1900-01-01'
    END
    AND CASE
        WHEN %s <> '' THEN
            %s
        ELSE
            '9999-12-31'
    END
    AND
    destination = CASE
        WHEN %s <> '' THEN
            %s
        ELSE
            destination
    END
    AND
    category = CASE
        WHEN %s <> '' THEN
            %s
        ELSE
            category
    END
    '''
    cursor.execute(SEARCH_SQL, (data['id'], data['id'], data['date_from'], data['date_from'], data['date_to'], data['date_to'], data['destination'], data['destination'], data['category'], data['category']))
    results = cursor.fetchall()
    cursor.close()
    connect.commit()
    connect.close()
    return results

def search_category():
    # 登録されているデータからcategoryのリストを重複無しで作成し返す
    connect = mysql.connector.connect(host="travel_map_db", port="3306", user="user", password="password", database="travel_map_db")
    cursor = connect.cursor(dictionary=True)

    SEARCH_SQL = 'SELECT * FROM travel_map_tbl'
    cursor.execute(SEARCH_SQL)
    results = cursor.fetchall()
    connect.commit()
    connect.close()

    init_category_list = []
    for row in results:
        init_category_list.append(row['category'])
    init_category_list = list(set(init_category_list))

    return init_category_list
