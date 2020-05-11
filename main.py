from sensor import Sensor
import numpy
import time

SOIL_CHANNEL = 0
TEMP_CHANNEL = 1

soil_readings = []
temp_readings = []
stop_time = time.time() + 5

while time.time() < stop_time:
    soil_reading = Sensor(SOIL_CHANNEL)
    soil_readings.append(soil_reading.percentage)
    
print(len(soil_readings))
mean = numpy.mean(soil_readings)
std = numpy.std(soil_readings)
min = numpy.min(soil_readings)
max = numpy.max(soil_readings)
print(mean)
print(std)
print(min)
print(max)