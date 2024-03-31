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

# connect ebimu
#IMU_serial = serial.Serial('/dev/ttyUSB0',115200, parity='N', timeout=0.001) #when connect to usb
IMU_serial = serial.Serial('/dev/ttyAMA0', 115200, parity='N', timeout=0.001) #when connect to GPIO pins (tx4,rx5)


IMU_serial.isOpen()

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

    