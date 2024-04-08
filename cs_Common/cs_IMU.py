import serial

global IMU_serial
#IMU_serial = serial.Serial('COM3', 921600, stopbits=1, parity='N', timeout=0.001)

# ----------------- Default Setting -----------------
def IMU_Init() :
    # connect ebimu
    # IMU_serial = serial.Serial('/dev/ttyUSB0',115200, parity='N', timeout=0.001) #when connect to usb
    IMU_serial = serial.Serial('/dev/ttyAMA0', 921600, parity='N', timeout=0.001)  # when connect to GPIO pins (tx4,rx5)
    #IMU_serial = serial.Serial('COM3', 115200, parity='N', timeout=0.001)

    IMU_reset()

    IMU_Output_Rate_polling()
    #print(IMU_serial.read(4))


    IMU_Output_Code_ASCII()
    IMU_Output_Euler()

    IMU_Set_Acc_ON() # or IMU_Set_Velo_Local() / IMU_Set_Velo_Global()
    IMU_Set_Gyro_ON()
    IMU_Set_Temp_ON()
    IMU_Set_Distance_Global()

    IMU_921600()

    IMU_Set_Baudrate(921600)


def IMU_Set_Baudrate(baudrate) :
    IMU_serial = serial.Serial('/dev/ttyAMA0', baudrate, parity='N', timeout=0.001)

def IMU_reset() :
    IMU_serial.write(b'<reset>\r\n')

def IMU_Cfg() :
    IMU_serial.write(b'<cfg>\r\n')

def IMU_Output_Rate_polling() :
    IMU_serial.write(b'<sor0>\r\n')

def IMU_Output_Rate_1() :
    IMU_serial.write(b'<sor1>\r\n')

def IMU_Output_Rate_10() :
    IMU_serial.write(b'<sor10>\r\n')

def IMU_Output_Rate_100() :
    IMU_serial.write(b'<sor100>\r\n')

def IMU_Output_Rate_1000() :
    IMU_serial.write(b'<sor1000>\r\n')

def IMU_Output_Rate_400() :
    IMU_serial.write(b'<sor400>\r\n')

def IMU_115200() :
    IMU_serial.write(b'<sb5>\r\n')

def IMU_921600() :
    IMU_serial.write(b'<sb8>\r\n')

def IMU_Output_Euler() :
    IMU_serial.write(b'<sof0>\r\n')

def IMU_Output_Quaternion() :
    IMU_serial.write(b'<sof1>\r\n')

def IMU_Output_Code_ASCII() :
    IMU_serial.write(b'<soc1>\r\n')

def IMU_Output_Code_HEX() :
    IMU_serial.write(b'<soc2>\r\n')

# --------------------- Sensor Setting ---------------------------

def IMU_Set_Acc_OFF() :
    IMU_serial.write(b'<soa0>\r\n')

def IMU_Set_Acc_ON() :
    IMU_serial.write(b'<soa1>\r\n')

def IMU_Set_Velo_Local() :
    IMU_serial.write(b'<soa4>\r\n')

def IMU_Set_Velo_Global() :
    IMU_serial.write(b'<soa5>\r\n')

def IMU_Set_Gyro_OFF() :
    IMU_serial.write(b'<sog0>\r\n')

def IMU_Set_Gyro_ON() :
    IMU_serial.write(b'<sog1>\r\n')

def IMU_Set_Temp_OFF() :
    IMU_serial.write(b'<sot0>\r\n')

def IMU_Set_Temp_ON() :
    IMU_serial.write(b'<sot1>\r\n')

def IMU_Set_Distance_OFF() :
    IMU_serial.write(b'<sod0>\r\n')

def IMU_Set_Distance_Local() :
    IMU_serial.write(b'<sod1>\r\n')

def IMU_Set_Distance_Global() :
    IMU_serial.write(b'<sod2>\r\n')

def IMU_Set_Magneto_OFF() :
    IMU_serial.write(b'<sem0>\r\n')

def IMU_Set_Magneto_ON() :
    IMU_serial.write(b'<sem1>\r\n')

# ------------------- Accelerometer Setting -------------------
def IMU_Set_Sens_Acc_2G() :
    IMU_serial.write(b'<ssa1>\r\n')

def IMU_Set_Sens_Acc_4G() :
    IMU_serial.write(b'<ssa2>\r\n')

def IMU_Set_Sens_Acc_8G() :
    IMU_serial.write(b'<ssa3>\r\n')

def IMU_Set_Sens_Acc_16G() :
    IMU_serial.write(b'<ssa4>\r\n')

# ------------------- Gyroscope Setting -------------------

def IMU_Set_Sens_Gyro_250dps() :
    IMU_serial.write(b'<ssg1>\r\n')

def IMU_Set_Sens_Gyro_500dps() :
    IMU_serial.write(b'<ssg2>\r\n')

def IMU_Set_Sens_Gyro_1000dps() :
    IMU_serial.write(b'<ssg3>\r\n')

def IMU_Set_Sens_Gyro_2000dps() :
    IMU_serial.write(b'ssg4>\r\n')

# ------------------------- Operation -------------------------

def IMU_Op():
    IMU_DATA = ""

    IMU_serial.write(b'*')

    if IMU_serial.in_waiting >= 100 :
        IMU_serial.cancel_read()

    IMU_DATA += str(IMU_serial.read(IMU_serial.in_waiting))
    IMU_DATA = IMU_DATA.replace("*", "")
    IMU_DATA = IMU_DATA.replace("'", "")
    IMU_DATA = IMU_DATA.replace("b", "")

    if IMU_DATA :
        print(IMU_DATA)