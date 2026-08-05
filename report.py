"""
Module: sensorkit/report.py
Contributor: Kobbeta Raymond
Student ID: 93602029
Date: 08/05/2026 
Role: Produce a printed summary of calibrated readings for one sensor.

This module ties together a sensor (from sensors.py) and the statistics
functions (from stats.py). Complete the TODOs below.
"""
from .stats import mean, minimum, maximum, spread


def summarise(sensor, raw_readings):
    if not isinstance(raw_readings, list):
        return 'Not valid'
    calibrated =[]
    """
    Given a sensor object and a list of raw readings:
      1. Calibrate every raw reading using sensor.read(...)
      2. Print a short summary using the stats functions.
    """
    
    # TODO : build a list `calibrated` containing sensor.read(r)
    #         for every r in raw_readings
    # TODO : get the unit string from sensor.units() and store it in `u`
    # TODO : print the report. Suggested lines (format numbers to 2 d.p.):
    #         Report for <sensor.name>
    #           count:   <how many readings>
    #           mean:    <mean> <u>
    #           min:     <minimum> <u>
    #           max:     <maximum> <u>
    #           spread:  <spread> <u>
    for readings in raw_readings:
        cal = sensor.read(readings)
        calibrated.append(cal)
    u = sensor.units()
    print(f'Report for {sensor.name}\n count:   {len(raw_readings)}\n mean:    {mean(calibrated):.2f} {u}\n min:     {minimum(calibrated):.2f} {u}\n max:     {maximum(calibrated):.2f} {u}\n spread:  {spread(calibrated):.2f} {u}\n')
    
