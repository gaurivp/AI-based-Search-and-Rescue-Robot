'''
import PyLidar3
import time # Time module
#Serial port to which lidar connected, Get it from device manager windows
#In linux type in terminal -- ls /dev/tty* 
###port = input("Enter port name which lidar is connected:") #windows
#port = "/dev/ttyUSB0" #linux
Obj = PyLidar3.YdLidarX4('COM3') #PyLidar3.your_version_of_lidar(port,chunk_size) 
if(Obj.Connect()):
    print(Obj.GetDeviceInfo())
    gen = Obj.StartScanning()
    t = time.time() # start time 
    while (time.time() - t) < 30: #scan for 30 seconds
        print(next(gen))
        time.sleep(0.5)
    Obj.StopScanning()
    Obj.Disconnect()
else:
    print("Error connecting to device")
'''

from rplidar import RPLidar
lidar = RPLidar('COM3')

info = lidar.get_info()
print(info)
 
health = lidar.get_health()
print(health)
 
for i, scan in enumerate(lidar.iter_scans()):
  #print('%d: Got %d measurments' % (i, len(scan)))
  print('\n',i,':',scan)
  if i > 19:
     break

lidar.stop()
lidar.stop_motor()
lidar.disconnect()
