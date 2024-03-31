from picamera2 import Picamera2
import time

picamera0 = Picamera2(0)
picamera1 = Picamera2(1)

'''
cam0_metadata = picamera0.capture_metadata()
cam0_controls = {c: cam0_metadata[c] for c in ["ExposureTime", "AnalogueGain", "ColourGains"]}

cam1_metadata = picamera1.capture_metadata()
cam1_controls = {c: cam0_metadata[c] for c in ["ExposureTime", "AnalogueGain", "ColourGains"]}

picamera0.set_controls(cam0_controls)
picamera1.set_controls(cam1_controls)
'''

def Camera_SetUp():
    camera_config = picamera0.create_still_configuration(main={"size": (4608, 2592)}, lores={"size": (4608, 2592)}, display="lores")
    camera_config = picamera1.create_still_configuration(main={"size": (4608, 2592)}, lores={"size": (4608, 2592)}, display="lores")
    picamera0.start()
    picamera1.start()

def Time_Return():
    now = time.localtime(time.time())
    nowtime = time.strftime("%Y%m%d_%I%M%S%_P", now)
    return nowtime

def Camera_Op():

    nowtime = Time_Return()

    if picamera0 :
        picamera0.capture_file(f'Camera_Image/Camera_0/Camera0_{nowtime}.jpg')
        
    else : 
        print (f"[Error] {nowtime} Cam0_Error")

    if picamera1 :
        picamera1.capture_file(f'Camera_Image/Camera_1/Camera1_{nowtime}.jpg')
        
    else :
        print (f"[Error] {nowtime} Cam1_Error")

    picamera0.stop()
    picamera1.stop()

Camera_SetUp()
Camera_Op()