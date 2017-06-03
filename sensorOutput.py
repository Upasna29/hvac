from env import environment
from firebase import firebase
import serial
import json
import requests
import time
import uuid

ser = serial.Serial(environment["SERIAL_PORT"], baudrate = 9600)
firebase_url = environment["DATABASE_URL"]
firebase = firebase.FirebaseApplication(firebase_url, None)
fixed_interval = 10

while 1:
    data = ser.readline()
    print data
    temp, lux = data.split()
    temp = float(temp)
    lux = float(lux)
    print 'temp: ', temp
    print 'lux: ', lux
    location = '/room-1'
    data = {'temperature':temp, 'luminosity': lux}

    try:
        response = firebase.get(location, None)
        if response:
            key, value = response.popitem()
            firebase.delete(location, key)
        
        result = firebase.post(location, data)
        print result                
    except Exception as e:
        print e

    time.sleep(fixed_interval)
