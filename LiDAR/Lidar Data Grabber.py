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
