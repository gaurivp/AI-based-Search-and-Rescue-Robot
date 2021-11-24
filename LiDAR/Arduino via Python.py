import serial
import time

serialdata = serial.Serial('COM5', '9600')
data =[]

while (t=10:
  if(serialdata.inWaiting() > 0):
      data.append(int(serialdata.readline()))
      print(data)
  t=+1
