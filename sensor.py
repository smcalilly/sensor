import spidev
from numpy import interp

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 1000000

class Sensor:
    def __init__(self, channel):
        self.channel_reading = self._read_channel(channel)
        self.percentage = self.get_percentage()
        self.volts = self._convert_volts()
    
    def get_percentage(self):
        return interp(self.channel_reading, [0, 1023], [100, 0])
    
    def _read_channel(self, channel):
        adc = spi.xfer2([1, (8 + channel) << 4, 0])
        data = ((adc[1] & 3) << 8) + adc[2]
        return data
    
    def _convert_volts(self):
        volts = (self.channel_reading * 3.3) / float(1023)
        volts = round(volts, 2)
        return volts
    


