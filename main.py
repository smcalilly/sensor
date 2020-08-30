from sensor import Sensor
import numpy
import time
import os
import sys
import db
from logger import setup_logger

DB_NAME = 'database.db'
os.chdir(os.path.dirname(sys.argv[0]))
database = db.Database(DB_NAME)

logger = setup_logger()

SOIL_CHANNEL = 0
TEMP_CHANNEL = 1
STOP_TIME = time.time() + 5
temp_readings = []

def read_soil():
    return Sensor(SOIL_CHANNEL)


def read_sensors():
    soil_readings = []
    
    logger.debug('reading sensors...')
    while time.time() < STOP_TIME:
        try:
            reading = read_soil()
            soil_readings.append(reading.volts)
        except Exception as e:
            logger.info('sensing went awry!')
            logger.info(e)
            
    return soil_readings


def calculate_soil_moisture(readings):
    logger.debug('calculating sensor readings...')
    return {
        'time': STOP_TIME,
        'mean': numpy.mean(readings),
        'std': numpy.std(readings),
        'min': numpy.min(readings),
        'max': numpy.max(readings),
    }


def save_calculations(soil):
    logger.debug('saving sensor calculations...')
    
    params = {
        'operation': "INSERT INTO soil_readings values(?, ?, ?, ?, ?, ?)",
        'args': (hash(tuple(soil.items())), soil['time'], soil['mean'], soil['std'], soil['min'], soil['max']) 
    }
    
    database.update(params)
    logger.info('sensor calculation successfully saved!')


def __main__():
    logger.info('initiliazing a sensor reading')
    readings = read_sensors()
    soil = calculate_soil_moisture(readings)
    save_calculations(soil)

    
if __name__ == "__main__":
    __main__()
    