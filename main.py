from sensor import Sensor
import numpy
import time
import sqlite3
import os
import sys
import db

DB_NAME = 'database.db'
os.chdir(os.path.dirname(sys.argv[0]))

SOIL_CHANNEL = 0
TEMP_CHANNEL = 1

soil_readings = []
temp_readings = []
stop_time = time.time() + 5

while time.time() < stop_time:
    try:
        soil_reading = Sensor(SOIL_CHANNEL)
        soil_readings.append(soil_reading.percentage)
    except Exception as e:
        print(e)

soil = {
    'time': stop_time,
    'mean': numpy.mean(soil_readings),
    'std': numpy.std(soil_readings),
    'min': numpy.min(soil_readings),
    'max': numpy.max(soil_readings)
}

air_temp = {}


def log_reading(reading):
    print('updating table with reading')
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO soil_readings values(?, ?, ?, ?, ?, ?)", (hash(tuple(reading.items())), reading['time'], reading['mean'], reading['std'], reading['min'], reading['max']))
    conn.commit()
    conn.close()

LOG_SOIL =  {
    'operation': "INSERT INTO soil_readings values(?, ?, ?, ?, ?, ?)",
    'args': (hash(tuple(reading.items())), reading['time'], reading['mean'], reading['std'], reading['min'], reading['max']))    
}

def __main__():
    #log_reading(soil)
    database = db.Database(DB_NAME)
    print(database)
    database.update(LOG_SOIL)
    
    
    soil_reading_count = database.query("select COUNT(mean) from soil_readings")
    print(soil_reading_count)
    
if __name__ == "__main__":
    __main__()