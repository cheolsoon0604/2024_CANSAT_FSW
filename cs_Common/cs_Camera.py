from picamera2 import Picamera2
import cs_Time
import os

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


def Is_Camera_Image_File(filename):

    if os.path.isfile(filename):
        return True

    else:
        return False


def Camera_SetUp():
    camera0_config = picamera0.create_still_configuration(main={"size": (4608, 2592)}, lores={"size": (4608, 2592)}, display="lores")
    camera1_config = picamera1.create_still_configuration(main={"size": (4608, 2592)}, lores={"size": (4608, 2592)}, display="lores")
    picamera0.start(camera0_config)
    picamera1.start(camera1_config)


def Cam0_Img_Cap() :

    now_time = cs_Time.Time_Return()
    camera_filename = f'Camera_Image/Camera_0/Camera0_{now_time}.jpg'

    if picamera0:
        picamera0.capture_file(camera_filename)
    else:
        print(f"[Error] {now_time} Cam0_Error")


def Cam1_Img_Cap() :

    now_time = cs_Time.Time_Return()
    camera_filename = f'Camera_Image/Camera_1/Camera1_{now_time}.jpg'

    if picamera1:
        picamera1.capture_file(camera_filename)
    else:
        print(f"[Error] {now_time} Cam1_Error")


def Camera_Op():
    Cam0_Img_Cap()
    Cam1_Img_Cap()


def Camera_Stop() :
    picamera0.stop()
    picamera1.stop()
