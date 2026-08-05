"""
Module: sensorkit/sensors.py
Contributor: Bakialoge Emmanuel Mensah
Student ID: 51422029
Date: 5th August 2026
Role: Provide concrete sensor classes built on the Sensor base class.

Each class must implement both abstract methods: read() and units().
Complete the TODOs below.
"""
from .base import Sensor


class Thermocouple(Sensor):
    def read(self, raw):
        
        # TODO: `raw` is in millivolts. Return degrees Celsius using:
        #       raw * 24.9 - 0.4
        if not isinstance(raw, (float or int)):
            return
        C= raw*(24.9-0.4)
        return C
    def units(self):
        return 'C'

    #TODO Implement missing method that returns the string "C"


class PressureGauge(Sensor):
    def read(self, raw):
        # TODO: `raw` is in volts. Return bar using:
        #       raw * 2.5
        if not isinstance(raw, (int or float)):
            return
        p=raw*2.5
        return p
        pass

    def units(self):
        return f'bar'
        # TODO: return the string "bar"
        pass

class StrainGauge(Sensor):
    def read(self, raw):
        return f'{raw*1000}'
        pass
    def units(self):
        return f'microstrain'
        pass

# TODO (optional, only if you have time):
# Add a third class StrainGauge where read(raw) returns raw * 1000
# and units() returns "microstrain".
