from env import environment
from firebase import firebase
from threading import Thread, Lock
import serial
import time

ser = serial.Serial(environment["SERIAL_PORT"], baudrate = 9600)
firebase_url = environment["DATABASE_URL"]
firebase = firebase.FirebaseApplication(firebase_url, None)
fixed_interval = 10
mutex = Lock()
data = ""

def write_data():
    while True:
        global data
        mutex.acquire(0) # non-blocking
        try:
            data = ser.readline()
        finally:
            mutex.release()

def update_db():
    while True:
        global data 
        mutex.acquire(0)
        try:
            print "Thread 2:", data
            if data: 
                temp, lux = data.split()
                temp = float(temp)
                lux = float(lux)
                print 'temp: ', temp
                print 'lux: ', lux
                location = '/rooms/room-1'
                record = {'temperature':temp, 'luminosity': lux}

                try:
                    response = firebase.get(location, None)
                    if response:
                        key, value = response.popitem()
                        firebase.delete(location, key)
                    
                    result = firebase.post(location, record)
                    print result                
                except Exception as e:
                    print e

                time.sleep(fixed_interval)
        finally:
            mutex.release()

if __name__ == "__main__":
    t1 = Thread(target = write_data)
    t2 = Thread(target = update_db)
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    while True:
        pass
