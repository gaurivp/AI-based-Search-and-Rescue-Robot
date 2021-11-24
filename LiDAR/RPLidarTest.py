'''
from pyrplidar import PyRPlidar

lidar = PyRPlidar()
lidar.connect(port="COM3", baudrate=115200, timeout=3)
# Linux   : "/dev/ttyUSB0"
# MacOS   : "/dev/cu.SLAB_USBtoUART"
# Windows : "COM5"


info = lidar.get_info()
print("info :", info)

health = lidar.get_health()
print("health :", health)

samplerate = lidar.get_samplerate()
print("samplerate :", samplerate)


scan_modes = lidar.get_scan_modes()
print("scan modes :")
for scan_mode in scan_modes:
    print(scan_mode)


lidar.disconnect()
'''
from pyrplidar import PyRPlidar
import time

def simple_scan():

    lidar = PyRPlidar()
    lidar.connect(port="COM3", baudrate=115200, timeout=3)
    # Linux   : "/dev/ttyUSB0"
    # MacOS   : "/dev/cu.SLAB_USBtoUART"
    # Windows : "COM5"

                  
    lidar.set_motor_pwm(500)
    time.sleep(2)
    
    scan_generator = lidar.force_scan()
    
    for count, scan in enumerate(scan_generator()):
        print(count, scan)
        if count == 20: break

    lidar.stop()
    lidar.set_motor_pwm(0)

    
    lidar.disconnect()


if __name__ == "__main__":
    simple_scan()

