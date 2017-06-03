import serial
import json
import requests
import time

ser = serial.Serial('/dev/tty.usbmodem1411', baudrate = 9600)
# firebase_url = 'https://homesensor-c98fb.firebaseio.com/'
firebase_url = 'https://hvac-8e1c5.firebaseio.com/'
fixed_interval = 10

while 1:
    data = ser.readline()
    temp, lux = data.split()
    temp = float(temp)
    lux = float(lux)
    print 'temp: ', temp
    print 'lux: ', lux
    location = 'room-1'
    data = {'temperature':temp, 'luminosity': lux}
    result = requests.post(firebase_url + '/' + location + '/temperature.json', data=json.dumps(data))

    print 'Record inserted. Result Code = ' + str(result.status_code) + ',' + result.text
    time.sleep(fixed_interval)
