import time
import serial

ser = serial.Serial('COM5',9600)
ogtime = (time.time())
time.sleep(3)
while True:
    counter = int(time.time()-ogtime)
    if counter%10 == 0:
        ser.write(b"r")
        time.sleep(3)
        
        data = ser.readline()
        print(data)

    
    