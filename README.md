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

## thanks
to the combined knowledge of these people:
- http://foxbotindustries.com/raspberry-pi-soil-moisture-sensor/
- https://www.raspberrypi-spy.co.uk/2013/10/analogue-sensors-on-the-raspberry-pi-using-an-mcp3008/
- https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
