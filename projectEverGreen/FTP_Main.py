#!/usr/bin/python3

from FTP_Library import fileUpload_temp, fileUpload_humidity, fileUpload_pressure
from config import SERVER, USERNAME, PASSWORD
from bmetest import temp_read, humidity_read, pressure_read
import os
import time
import json

def main():
    temp_list = []
    humidity_list = []
    pressure_list = []
    i=0
    while True:
        i+=1
        temp_list.append(temp_read())
        humidity_list.append(humidity_read())
        pressure_list.append(pressure_read())
        print(temp_list)
        print(humidity_list)
        print(pressure_list)
        if i % 10 == 0:
            print(i)
            print('\n')
            temp_filename = 'temp' + str(i) + '.json'
            humidity_filename = 'humidity' + str(i) + '.json'
            pressure_filename = 'pressure' + str(i) + '.json'
            with open(temp_filename, 'w') as t:
                t.write(json.dumps(temp_list))
            fileUpload_temp(temp_filename, SERVER, USERNAME, PASSWORD)
            temp_list = []
            with open(humidity_filename, 'w') as t:
                t.write(json.dumps(humidity_list))
            fileUpload_humidity(humidity_filename, SERVER, USERNAME, PASSWORD)
            humidity_list = []
            with open(pressure_filename, 'w') as t:
                t.write(json.dumps(pressure_list))
            fileUpload_pressure(pressure_filename, SERVER, USERNAME, PASSWORD)
            pressure_list = []
            if i > 5000:
                i = 0
        time.sleep(1)
main()
