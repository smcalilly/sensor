# Soil Sensor
This repo has three things:
1) Code for a Raspberry Pi to read soil moisture levels based on capacitance measurement of the soil.
2) A flask app to display the sensor data on a webpage.
3) A shell script to execute the sensor code (need to update the paths based on your system).

The sensor code must be ran as a cron job on the RPi.

I'm saving my work without refactoring or writing much documentation, so anybody who tries to use this repo might have a hard time (myself included)! 

## hardware
- raspberry pi
- breadboard
- jumper cables
- capacitative touch sensor
- SPI
