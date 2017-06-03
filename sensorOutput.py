import serial
import json
import requests
import time
import uuid
import os
from env import environment

ser = serial.Serial(environment["SERIAL_PORT"], baudrate = 9600)
firebase_url = environment["DATABASE_URL"]
fixed_interval = 10

while 1:
    data = ser.readline()
    temp, lux = data.split()
    temp = float(temp)
    lux = float(lux)
    print 'temp: ', temp
    print 'lux: ', lux
    location = str(uuid.uuid4())
    data = {'temperature':temp, 'luminosity': lux}
    result = requests.post(firebase_url + '/' + location + '.json', data=json.dumps(data))

    print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
    time.sleep(fixed_interval)
