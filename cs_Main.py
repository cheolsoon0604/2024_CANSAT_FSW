from cs_Common import cs_BT
from cs_Common import cs_Camera
from cs_Common import cs_GPS
from cs_Common import cs_IMU
from cs_Common import cs_SD

def cs_setup() :
    print("CANSAT Setup")

    cs_Camera.Camera_SetUp()
    cs_GPS.GPS_Init()
    cs_IMU.IMU_Init()

def cs_loop() :
    print("hello world")

    cs_Camera.Camera_Op()
    cs_GPS.GPS_Op()
    cs_IMU.IMU_Op()

