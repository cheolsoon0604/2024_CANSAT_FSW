import serial 
import time

'''
# make file and open
def Time_Return():
    now = time.localtime(time.time())
    nowtime = time.strftime("%Y%m%d_%I%M%S%_P", now)
    return nowtime

nowtime = Time_Return()
filePath = "Cansat_Log/cs_Log/"
fileName = f"{filePath}CANSAT_LOG_{nowtime}"

try:
    f = open(fileName, 'w')
    log = open(fileName,'w')
except:
    print("Failed to open file")
'''

global IMU_serial
global IMU_Buf

# ----------------- Default Setting -----------------
def IMU_Init() :
    # connect ebimu
    # IMU_serial = serial.Serial('/dev/ttyUSB0',115200, parity='N', timeout=0.001) #when connect to usb
    IMU_serial = serial.Serial('/dev/ttyAMA0', 115200, parity='N', timeout=0.001)  # when connect to GPIO pins (tx4,rx5)
    IMU_reset()

    IMU_Output_Rate_polling()
    IMU_Output_Code_ASCII()
    IMU_Output_Euler()

    IMU_Set_Acc_ON()
    IMU_Set_Gyro_ON()
    IMU_Set_Temp_ON()
    IMU_921600()

def IMU_Set_Baudrate(baudrate) :
    IMU_serial = serial.Serial('/dev/ttyAMA0', baudrate, parity='N', timeout=0.001)
def IMU_reset() :
    IMU_serial.write(b'<reset>\r\n')
def IMU_Cfg() :
    IMU_serial.write(b'<cfg>')
def IMU_Output_Rate_polling() :
    IMU_serial.write(b'<sor0>\r\n')
def IMU_115200() :
    IMU_serial.write(b'<sb5>\r\n')
def IMU_921600() :
    IMU_serial.write(b'<sb8>\r\n')

# --------------------- Sensor Setting ---------------------------

def IMU_Set_Acc_OFF() :
    IMU_serial.write(b'<soa0>\r\n')
def IMU_Set_Acc_ON() :
    IMU_serial.write(b'<soa1>\r\n')
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
def IMU_Output_Euler() :
    IMU_serial.write(b'<sof0>\r\n')
def IMU_Output_Code_ASCII() :
    IMU_serial.write(b'<soc1>\r\n')
def IMU_Output_Code_HEX() :
    IMU_serial.write(b'<soc2>\r\n')

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

def IMU_Op() :

    IMU_buf = "" # for ebimu

    # read ebimu value 
    while IMU_serial.inWaiting():

        IMU_Raw_data = str(IMU_serial.read()).strip()
        
        # print(data) # for debuging

        IMU_buf += IMU_Raw_data # buffering
        if IMU_Raw_data[3] == "n": # last data of one line is '\n' so when data[3] is n then do decode 
            IMU_buf = IMU_buf.replace("'","") # remove (') and (b) because data has (') and (b) like this b'10.55' 
            IMU_buf = IMU_buf.replace("b","") 

            # split each data
            try :
                roll, pitch, yaw, x, y, z = map(float, IMU_buf[1:-4].split(','))

            except Exception as e:
                print(list(map(float,IMU_buf[1:-4].split(','))))
                #log.write(str(e)+"\n")
                IMU_buf = ""
                continue
            
            try :
                IMU_data = [roll,pitch,yaw,x,y,z]
                writeString = "*"+str(IMU_data)[1:-1]+"\n"
                #f.write(writeString)

            except Exception as e:
                print("Error from file writing : ", e)
                #log.write(str(e)+"\n") # it also can make error but .. maybe.. i dont think so
                continue
            print(roll,pitch,yaw,x,y,z)
            IMU_buf = ""

    