"""
Module: sensorkit/dataio.py
Contributor: <Ernest Aleke>
Student ID: <86552029>
Date: <date>
Role: Load raw sensor readings from a text/CSV file, safely.

Uses pathlib for the file path and exceptions to handle problems.
Complete the TODOs below.
"""
from pathlib import Path


def load_readings(filepath):
    path = Path(filepath)
    readings = []  
    try:
        
        with open(f'{path}','r') as f:
            for line in f:
                #print(line)
                try:
                    readings.append(float(line.strip('\n')))
                    if not line:
                        continue
                except ValueError:
                    print(f"Skipping invalid line: {line.strip('\n')!r}")
        
    except FileNotFoundError:
        print('File not found')
    return readings

        
        
                
"""
    Read a file of raw numeric readings, one value per line, and return
    a list of floats.

    Rules:
      - If the file does not exist, raise FileNotFoundError.
      - Ignore blank lines.
      - If a line is not a valid number, skip it and print a short message
        instead of letting the program crash.
    """
    

    # TODO : if the path does not exist, raise FileNotFoundError
    #

    
    #TODO : Complete the loop to read in the file content
        # TODO : try to convert `line` to a float and append it to readings.
        #         If it raises ValueError, print:
        #         f"Skipping invalid line: {line!r}"

