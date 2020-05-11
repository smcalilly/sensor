from sensor import Sensor
import numpy
import time

SOIL_CHANNEL = 0
TEMP_CHANNEL = 1

soil_readings = []
temp_readings = []
start_time = time.time()
stop_time = time.time() + 5

while start_time < stop_time:
    try:
        soil_reading = Sensor(SOIL_CHANNEL)
        soil_readings.append(soil_reading.percentage)
    except Exception as e:
        print(e)

print(len(soil_readings))
mean = numpy.mean(soil_readings)
std = numpy.std(soil_readings)
min = numpy.min(soil_readings)
max = numpy.max(soil_readings)
print(mean)
print(std)
print(min)
print(max)

file = open('readings.csv', 'a')
line = mean + "," + std + "," + min + "," + max + "," + stop_time
file.write(line)
file.close()