from sensor import Sensor
import numpy
import time
import os
import sys
import db

DB_NAME = 'database.db'
os.chdir(os.path.dirname(sys.argv[0]))
database = db.Database(DB_NAME)

SOIL_CHANNEL = 0
TEMP_CHANNEL = 1
STOP_TIME = time.time() + 5
temp_readings = []

def read_soil():
    return Sensor(SOIL_CHANNEL)


def read_sensors():
    soil_readings = []
    
    while time.time() < STOP_TIME:
        try:
            reading = read_soil()
            soil_readings.append(reading.percentage)
        except Exception as e:
            print('sensing went awry!')
            print(e)
            
    return soil_readings


def calculate_soil_moisture(readings):
    return {
        'time': STOP_TIME,
        'mean': numpy.mean(readings),
        'std': numpy.std(readings),
        'min': numpy.min(readings),
        'max': numpy.max(readings)
    }


def save_measurements(soil):
    params = {
        'operation': "INSERT INTO soil_readings values(?, ?, ?, ?, ?, ?)",
        'args': (hash(tuple(soil.items())), soil['time'], soil['mean'], soil['std'], soil['min'], soil['max']) 
    }
    
    database.update(params)


def __main__():
    # get readings
    readings = read_sensors()
    soil = calculate_soil_moisture(readings)
    save_measurements(soil)

    soil_reading_count = database.query("select COUNT(mean) from soil_readings")
    print(soil_reading_count)
    
if __name__ == "__main__":
    __main__()
    