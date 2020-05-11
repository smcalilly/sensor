import sqlite3 as sql
import sys

CONN = sql.connect('database.db')

with CONN:
        cursor = CONN.cursor()
        cursor.execute('DROP TABLE IF EXISTS soil_readings')
        cursor.execute('CREATE TABLE soil_readings(id integer PRIMARY KEY, timestamp DATETIME, mean INTEGER, std INTEGER, min_reading INTEGER, max_reading INTEGER)')